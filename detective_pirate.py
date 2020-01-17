import requests
from bs4 import BeautifulSoup
from urllib.request import urlparse,urljoin
import sys
import re 

class crptjack_detection:
    
    def __init__(self, *args, **kwargs):    #creating session
        self.session=requests.Session()
        self.internal_links=set()
        self.external_links=set()
        self.visited_links=[]
        self.url_count=1
        self.parent_url="http://gogoanime.io/kiratto-prichan-2nd-season-episode-25"    

    def send_request(self):          #sending request and getting a domain 
        self.entry_point=self.parent_url 
        self.s_requests=self.session.get(self.entry_point)
        self.domain_name = urlparse(self.entry_point).netloc

        if self.domain_name.count('.')==2:
            self.dom1=self.domain_name[1+self.domain_name.index('.'):]
            self.dom2=self.dom1[:self.dom1.index('.')]
            
        if self.domain_name.count('.')==1:
            self.dom2=self.domain_name[:self.domain_name.index('.')]

    def extract_urls(self):   
        self.list_urls=[]                                #extracting links
        self.links=BeautifulSoup(self.s_requests.text,"lxml")
        for link in self.links.find_all('a'):
            self.urls=link.attrs.get('href')
            self.urls=urljoin(self.entry_point,self.urls)
            self.list_urls.append(self.urls)
    
    def evaluate_links(self):               #evaluate the internal and external links  
        for eval_url in self.list_urls:
            self.domains=urlparse(eval_url).netloc
            
            if self.domains.count('.')==2:
                doma1=self.domains[1+self.domains.index('.'):]
                self.sub_domains=doma1[:doma1.index('.')]
            
            if self.domains.count('.')==1:
                self.sub_domains=self.domains[:self.domains.index('.')]
                
            # print(self.dom2,'\t',self.sub_domains)

            if self.dom2==self.sub_domains:
                self.internal_links.add(eval_url)
            else :
                self.external_links.add(eval_url)

        self.internal_links.discard('javascript:void(0)')
        self.internal_links.discard('javascript:;')
        
    def crawler_unleashed(self):
        self.parent_url=''
        self.parent_url=self.internal_links.pop()
        self.url_count+=1
        print(self.internal_links)
        # print(self.url_count,sum(1 for i in self.internal_links))

        self.visited_links.append(self.parent_url)
        for i in self.visited_links:
            if i in self.internal_links:
                self.internal_links.discard(i)
        
        if not self.internal_links:
            print("Exiting")
            sys.exit()
    
if __name__=='__main__':
    crypt_obj=crptjack_detection()

    while True:
	    crypt_obj.send_request()
	    crypt_obj.extract_urls()
	    crypt_obj.evaluate_links()
	    crypt_obj.crawler_unleashed()  
