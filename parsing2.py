import re
import csv
import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

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
        for i in range(len(slicers)-1):
            g_arr=[s for s in posts[slicers[i]:slicers[i+1]]]
            g_arr.pop(0)
            if g_arr:
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
        self.duplicates=[]
        for i,x in enumerate(vectors):
            for v,c in enumerate(vectors):
                if i!=v:
                    vec1=x.reshape(1,-1)
                    vec2=c.reshape(1,-1)
                    csim=cosine_similarity(vec1,vec2)[0][0]
                    
                    if csim>=0.97 and csim<1.0:
                        self.duplicates.append(self.sweep[v])
                        print(csim,i,v,len(self.duplicates))

        self.remove_duplicates()

    def remove_duplicates(self):
        # removing the duplicates from the posts list 
        for i in self.duplicates:
            if i in self.ga[:]:
                self.ga.remove(i)
                
        self.csv_export()

    def csv_export(self):
        #Exporting them to a csv file
        zipped=zip(self.ga)
        with open("/home/bigpenguin/predictions and datasets/datasets/posts.csv","w") as Output_csv:
            CSVWriter = csv.writer(Output_csv,dialect='excel')
            for i in zipped:
                CSVWriter.writerow(i)

if __name__=='__main__':
    obj=parsing()
    obj.vector()