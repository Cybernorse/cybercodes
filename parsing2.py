import re
import csv
import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import numpy as np

            # gender=re.compile(r'(\d+[/]\d+[/]\d.*\:) ([a-zA-Z0-9].*)')
            # matches=gender.finditer(g_arr[0])
            # for i in matches:
            #     g_arr.insert(1,i.group(2))

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
            g=g_arr[0].split(": ")
            g_arr.insert(1,g[-1])
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
        # removing the duplicates from the posts list 
        uniq_dup=sorted(set(self.dup))
        dict_dup={}
        for i in uniq_dup:
            dict_dup[i]=[]
        
        for i,z in zip(self.dup,self.cdup):
            for key,val in dict_dup.items():
                if i==key:
                    val.append(z)
                    if key not in val:
                        val.append(key)
                        
        # dict_dup={7: [95], 8: [468], 18: [155], 19: [288], 27: [106], 30: [304], 31: [403, 453], 33: [221], 34: [222], 35: [233, 254], 39: [339], 47: [124], 48: [79, 207], 52: [320], 53: [122, 149], 55: [116], 57: [305], 62: [84], 63: [211], 68: [208], 69: [120, 239], 77: [282], 79: [48, 207], 81: [192], 84: [62], 86: [316], 87: [317], 90: [158, 264], 91: [126], 94: [205], 95: [7], 98: [324], 99: [292], 100: [143], 106: [27], 116: [55, 139], 119: [145], 120: [69, 239], 122: [53, 149], 124: [47], 126: [91], 128: [182], 137: [156, 181], 139: [116], 143: [100], 144: [253], 145: [119], 149: [53, 122], 153: [367], 155: [18], 156: [137, 181], 157: [184], 158: [90, 264], 162: [275], 163: [417, 482], 165: [216], 166: [307], 180: [200], 181: [137, 156], 182: [128], 184: [157], 189: [220, 303], 192: [81], 194: [326], 195: [280], 197: [246], 200: [180], 205: [94], 207: [48, 79], 208: [68], 210: [289], 211: [63], 216: [165], 218: [286], 220: [189, 303], 221: [33], 222: [34], 223: [269, 302], 232: [276], 233: [35, 254], 237: [454], 239: [69, 120], 241: [337], 245: [301], 246: [197], 252: [380], 253: [144], 254: [35, 233], 264: [90, 158], 265: [306], 269: [223, 302], 275: [162], 276: [232], 278: [365], 279: [366], 280: [195, 323], 282: [77], 286: [218], 288: [19], 289: [210], 292: [99], 301: [245], 302: [223, 269], 303: [189, 220], 304: [30], 305: [57], 306: [265], 307: [166], 313: [399, 416], 314: [350], 315: [372], 316: [86], 317: [87], 319: [462], 320: [52], 322: [415], 323: [280], 324: [98], 326: [194], 330: [473], 334: [364, 428, 486], 337: [241], 339: [39], 340: [424], 349: [442], 350: [314], 353: [354], 354: [353], 355: [460], 364: [334, 428, 486], 365: [278], 366: [279], 367: [153, 489], 371: [379], 372: [315], 373: [476], 378: [432], 379: [371], 380: [252], 399: [313, 416], 402: [491], 403: [31, 453], 408: [475], 413: [457], 415: [322], 416: [313, 399], 417: [163, 482], 418: [435, 494], 424: [340], 428: [334, 364, 486], 432: [378], 435: [418, 494], 436: [495], 439: [463], 442: [349], 447: [488], 451: [471], 452: [470], 453: [31, 403], 454: [237], 457: [413], 460: [355], 462: [319], 463: [439], 468: [8], 470: [452], 471: [451], 473: [330], 475: [408], 476: [373], 482: [163, 417], 486: [334, 364, 428], 488: [447], 489: [367], 491: [402], 494: [418, 435], 495: [436]}      
    
        for i in dict_dup.values():
            if len(i)>1:
                i.pop(0)

        app_dup=[]
        for i in dict_dup.values():
            for x in i:
                app_dup.append(self.sweep[x])
        
        for i in app_dup:
            if i in self.ga[:]:
                self.ga.remove(i)
                
        self.csv_export()
    def csv_export(self):
        #Exporting them to a csv file

        with open("/home/bigpenguin/predictions and datasets/datasets/posts.csv","w") as Output_csv:
            CSVWriter = csv.writer(Output_csv,dialect='excel')
            CSVWriter.writerow(['posts','Hijabi','Name','Age','Height','Residence','Status','Ethnicity','Profession'])
            for i in self.ga:
                patt=re.findall(r'LOOKING FOR',i)
                if patt:
                    # print(i[:i.index(patt[0])])

                    hijabi=re.findall(r'Hijabi.*',i[:i.index(patt[0])])
                    name=re.findall(r'Name.*',i[:i.index(patt[0])])
                    age=re.findall(r'Age.*',i[:i.index(patt[0])])
                    height=re.findall(r'Height.*',i[:i.index(patt[0])])
                    residence=re.findall(r'Residence.*',i[:i.index(patt[0])])
                    profession=re.findall(r'Profession.*',i[:i.index(patt[0])])
                    lstatus=re.findall(r'Legal Status.*',i[:i.index(patt[0])])
                    mstatus=re.findall(r'Marital status.*',i[:i.index(patt[0])])
                    ethnicity=re.findall(r'Ethnicity.*',i[:i.index(patt[0])]) 

                    if not lstatus or not mstatus:
                        status=lstatus+mstatus
                    else:
                        status=[lstatus[0]+' '+mstatus[0]]
                    data=[i]+hijabi+name+age+height+residence+status+ethnicity+profession

                    CSVWriter.writerow(data)
                
if __name__=='__main__':
    obj=parsing()
    obj.vector()
