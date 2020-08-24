import re
import csv
import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import numpy as np
'''
modules to be installed:
#   slearn
#   nltk    (download the stopwords database with | >>>nltk.download('stopwords') | in the python3.7 interpreter)
#   numpy==1.18.5
numpy must have that version or else it will prompt you an error.
'''
class parsing:
    def __init__(self,*args,**kwargs):
        with open('/home/bigpenguin/Downloads/WhatsApp Export.txt','r') as fi:
            export=[i.rstrip() for i in fi.readlines()]
    
        #removing the unneeded timestamps
        cleaner=[]
        for i,z in enumerate(export):
            pattern1=re.findall(r'\d+[/]\d+[/]\d.* ',z)
            if pattern1:
                if pattern1[0].count(':') == 1:
                    cleaner.append(z)     
        for i in cleaner:
            if i in export[:]:
                export.remove(i)
        
        #containering all the posts in a single list 
        posts=[]
        for i in export:
            posts.append(i)
    
        #getting posts timestamps indexes from the list
        slicers=[]
        for i,z in enumerate(posts):
            patterns=re.findall(r'\d+[/]\d+[/]\d.*:\ .*',z)
            if patterns:
                slicers.append(i)
        
        #slicing all the posts with the help of timestamps index 
        self.grand_arr=[]
        self.timestamps=[]
        for i in range(len(slicers)-1):
            g_arr=[s for s in posts[slicers[i]:slicers[i+1]]]
            g=g_arr[0].split(": ")
            g_arr.insert(1,g[-1])
            if len(g_arr)>1:
                self.timestamps.append('\n'.join(g_arr))
            g_arr.pop(0)
            if len(g_arr)>1:
                self.grand_arr.append('\n'.join(g_arr))
        
        #removing the completely same posts 
        self.sweep=[]
        for i in self.grand_arr:
            if i not in self.sweep:
                self.sweep.append(i)
    
        self.ga=self.sweep
    
    def clean(self,text):
        #removing the puntuations and stopwords from each post
        sw=stopwords.words('english')
        p=[]
        for i in text:
            p.append(''.join(i.split('\n')))
        
        text=''.join([word for word in text if word not in string.punctuation])
        text=text.lower()
        text=' '.join([word for word in text.split('\n') if word not in sw])
        
        return text 

    def vector(self):
        #calling the clean method and passing the post list
        cleaned=list(map(self.clean,self.sweep))
        
        #Extracting features out of posts strings and converting the posts to 2D array vectors  
        vectorizer=CountVectorizer().fit_transform(cleaned)
        vectors=vectorizer.toarray()
        
        #calculating the cousine similarity of posts and getting the duplicates with accordance to the defined threshold
        self.dup=[]
        self.cdup=[]
        for i,x in enumerate(vectors):
            for v,c in enumerate(vectors):
                if i!=v:
                    vec1=x.reshape(1,-1)
                    vec2=c.reshape(1,-1)
                    csim=cosine_similarity(vec1,vec2)[0][0]
                    
                    if csim>=0.97:
                        
                        self.dup.append(i)
                        self.cdup.append(v)
                        vectors=np.delete(vectors,c,0)
                        print(csim,i,v)
        
        self.remove_duplicates()

    def remove_duplicates(self):
        # initializing the dict with unique values contained in the self.dup list 
        uniq_dup=sorted(set(self.dup))
        dict_dup={}
        for i in uniq_dup:
            dict_dup[i]=[]
         
        # getting multiple duplicate values from self.cdup mapped to single key of self.dup, and putting the key in the values if not in there already.
        ''' 
            2345    45
            2345    56
            2345    67
            getting above form into :
            {
                2345:[45,56,67,2345]
            }
        ''' 
        for i,z in zip(self.dup,self.cdup):
            for key,val in dict_dup.items():
                if i==key:
                    val.append(z)
                    if key not in val:
                        val.append(key)

        # removing first value from each dict values list
        for i in dict_dup.values():
            if len(i)>1:
                i.pop(0)
        
        # getting duplicates posts from the indexes 
        app_dup=[]
        for i in dict_dup.values():
            for x in i:
                app_dup.append(self.sweep[x])
        
        # removing the duplicate post from the original list
        for i in app_dup:
            if i in self.ga[:]:
                self.ga.remove(i)
                
    def csv_export(self):
        # getting the dates and phone numbers for each posts from the relative timestamps
        post_time=[]
        asc=[]
        for x in self.ga:
            for i in self.timestamps:
                if '\n'.join(i.split('\n')[1:]) not in asc:
                    if x == '\n'.join(i.split('\n')[1:]):
                        post_time.append(i.split('\n')[0])
                        asc.append('\n'.join(i.split('\n')[1:]))

        # creating file in the write mode 
        with open("/home/bigpenguin/predictions and datasets/datasets/posts.csv","w") as Output_csv:
            CSVWriter = csv.writer(Output_csv,dialect='excel')

            # wrting headers in the file 
            CSVWriter.writerow(['Date','Phone Numbers','posts','Hijabi','Name','gender','Age','Height','Residence','Legal Status','Marital Status','Ethnicity','Profession','Education','Religion',
            'LFAge','LFHeight','LFResidence','LFLegal Status','LFMarital Status','LFEthnicity','LFProfession','LFEducation','LFReligion','LFContact'])

            # checking for "looking for" in the posts if not look for hobbies
            for i,time in zip(self.ga,post_time):
                patt=re.findall(r'LOOKING\s?FOR',i,re.IGNORECASE)
            
                if not patt:
                    patt=re.findall(r'Hobbies',i,re.IGNORECASE)
                
                # print(i[:i.index(patt[0])])
                # print(i[i.index(patt[0]):])

                # if found, use it to get the index in the post split the post in two take everythin above "LOOKING FOR" and extract the following with the regular expressions 
                if patt:
                
                    date=re.findall(r'\d[/]\d+[/]\d+, \d+:\d+',time,re.IGNORECASE)
                    phone_number=re.findall(r'-.*[+1]\s?[(]\d{3}[)]?\s?\d{3}-\d{4}',time,re.IGNORECASE)
                    hijabi=re.findall(r'Hijabi.*',i[:i.index(patt[0])],re.IGNORECASE)
                    name=re.findall(r'Name.*',i[:i.index(patt[0])],re.IGNORECASE)
                    age=re.findall(r'Age.*',i[:i.index(patt[0])],re.IGNORECASE)
                    height=re.findall(r'He?ight.*',i[:i.index(patt[0])],re.IGNORECASE)
                    residence=re.findall(r'Residence.*',i[:i.index(patt[0])],re.IGNORECASE)
                    profession=re.findall(r'Profession.*',i[:i.index(patt[0])],re.IGNORECASE)
                    lstatus=re.findall(r'Legal status.*',i[:i.index(patt[0])],re.IGNORECASE)
                    mstatus=re.findall(r'Marital status.*',i[:i.index(patt[0])],re.IGNORECASE)
                    ethnicity=re.findall(r'Ethnicity.*',i[:i.index(patt[0])],re.IGNORECASE) 
                    gender=re.findall(r'male|female.*',i[:i.index(patt[0])],re.IGNORECASE) 
                    education=re.findall(r'Education.*',i[:i.index(patt[0])],re.IGNORECASE)
                    rel=re.findall(r'Religion?.*',i[:i.index(patt[0])],re.IGNORECASE)
                
                    # take everything down the "LOOKING FOR" and extract the following 
                    lfage=re.findall(r'Age\s?:?\s?.*',i[i.index(patt[0]):],re.IGNORECASE)
                    lfresidence=re.findall(r'Residence.*',i[i.index(patt[0]):],re.IGNORECASE)
                    lfheight=re.findall(r'He?ight.*',i[i.index(patt[0]):],re.IGNORECASE)
                    lfprofession=re.findall(r'Profession.*',i[i.index(patt[0]):],re.IGNORECASE)
                    lflstatus=re.findall(r'Legal status.*',i[i.index(patt[0]):],re.IGNORECASE)
                    lfmstatus=re.findall(r'Marital status.*',i[i.index(patt[0]):],re.IGNORECASE)
                    lfethnicity=re.findall(r'Ethnicity.*',i[i.index(patt[0]):],re.IGNORECASE)
                    lfeducation=re.findall(r'Education.*',i[i.index(patt[0]):],re.IGNORECASE)
                    lfcontact=re.findall(r'Contact.*',i[i.index(patt[0]):],re.IGNORECASE)
                    lfrel=re.findall(r'Religion?.*',i[i.index(patt[0]):],re.IGNORECASE)
                
                # cleaning all the information ectracted and filling up the nulls 
                if hijabi:
                    hijabi=re.findall(r':\s?.*',hijabi[0])
                if not hijabi:
                    hijabi.append('N/A')
                
                if name:
                    name=re.findall(r'\s? .+',name[0])
                if not name:
                    name.append('N/A')
                
                if age:
                    age=re.findall(r'\s? .+',age[0])
                if not age:
                    age.append('N/A')
            
                if height:
                    height=re.findall(r'\s? .+',height[0])
                if not height:
                    height.append('N/A')
                
                if residence:
                    residence=re.findall(r'\s? .+',residence[0])
                if not residence:
                    residence.append('N/A')
                
                if profession:
                    profession=re.findall(r'\s? .+',profession[0])
                if not profession:
                    profession.append('N/A')
                
                if lstatus:
                    lstatus=re.findall(r'\:|-?\s.*',lstatus[0])
                if not lstatus:
                    lstatus.append('N/A')
                
                if mstatus:
                    mstatus=re.findall(r':|-?\s.*',mstatus[0])
                if not mstatus:
                    mstatus.append('N/A')
                
                if ethnicity:
                    ethnicity=re.findall(r'\s? .+',ethnicity[0])
                if not ethnicity:
                    ethnicity.append('N/A')
                
                if education:
                    education=re.findall(r'\s? .+',education[0])
                if not education:
                    education.append('N/A')

                if rel:
                    rel=re.findall(r': .+',rel[0])
                if not rel:
                    rel.append('N/A')

                if not gender:
                    gender.append('N/A')

                    ################################################################################

                if lfage:
                    lfage=re.findall(r'\s?:?\s? .+',lfage[0])
                if not lfage:
                    lfage.append('N/A')
            
                if lfheight:
                    lfheight=re.findall(r'\s? .+',lfheight[0])
                if not lfheight:
                    lfheight.append('N/A')
                
                if lfresidence:
                    lfresidence=re.findall(r'\s? .+',lfresidence[0])
                if not lfresidence:
                    lfresidence.append('N/A')
                
                if lfprofession:
                    lfprofession=re.findall(r'\s? .+',lfprofession[0])
                if not lfprofession:
                    lfprofession.append('N/A')
                
                if lflstatus:
                    lflstatus=re.findall(r'\:|-?\s.*',lflstatus[0])
                if not lflstatus:
                    lflstatus.append('N/A')
                
                if lfmstatus:
                    lfmstatus=re.findall(r':|-?\s.*',lfmstatus[0])
                if not lfmstatus:
                    lfmstatus.append('N/A')
                
                if lfethnicity:
                    lfethnicity=re.findall(r'\s? .+',lfethnicity[0])
                if not lfethnicity:
                    lfethnicity.append('N/A')
                
                if lfeducation:
                    lfeducation=re.findall(r'\:?.+',lfeducation[0])
                if not lfeducation:
                    lfeducation.append('N/A')

                if lfrel:
                    lfrel=re.findall(r':\s?.+',lfrel[0])
                if not lfrel:
                    lfrel.append('N/A')

                if lfcontact:
                    lfcontact=re.findall(r':\s?.*',lfcontact[0])
                if not lfcontact:
                    lfcontact.append('N/A')
                # concatenate all the lists 
                data=date+phone_number+[i]+hijabi+name+gender+age+height+residence+lstatus+mstatus+ethnicity+profession+education+rel+lfage+lfheight+lfresidence+lflstatus+lfmstatus+lfethnicity+lfprofession+lfeducation+lfrel+lfcontact

                # write it to the csv file
                CSVWriter.writerow(data)
            
            # if "LOOKING FOR" or "Hobbies" not found concatenate only the dates, phone numbers and post and write to the file
            else:
                elses=date+phone_number+[i]
                CSVWriter.writerow(elses)
                
if __name__=='__main__':
    obj=parsing()
    obj.vector()
    obj.csv_export()
