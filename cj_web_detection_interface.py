import wx
import multiprocessing
import requests
from bs4 import BeautifulSoup
from urllib.request import urlparse,urljoin
import sys
import time 

class crypto_engine:
    
    def __init__(self,*args,**kwargs):    #creating session
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

            if self.dom2==self.sub_domains:
                self.internal_links.add(eval_url)
            else :
                self.external_links.add(eval_url)

        self.internal_links.discard('javascript:void(0)')
        self.internal_links.discard('javascript:;')

    def iframe_ads(self):
        iframe=BeautifulSoup(self.s_requests.text,'lxml')
        for i in iframe.find_all('iframe'):
            ads=i.attrs.get('src')
            ads=urljoin(self.entry_point,ads)
            self.external_links.add(ads)

    def videos_ads(self):
        v_ads=BeautifulSoup(self.s_requests.text,'lxml')
        for i in v_ads.find_all('video'):
            va=i.attrs.get('src')
            va=urljoin(self.entry_point,va)
            self.external_links.add(va)

    def image_ads(self):
        i_ads=BeautifulSoup(self.s_requests.text,'lxml')
        for i in i_ads.find_all('img'):
            ia=i.attrs.get('src')
            ia=urljoin(self.entry_point,ia)
            self.external_links.add(ia)

    def next_url(self):
        self.parent_url=''
        self.parent_url=self.internal_links.pop()
        self.url_count+=1
        
        # print(self.url_count,sum(1 for i in self.internal_links))

        self.visited_links.append(self.parent_url)
        for i in self.visited_links:
            if i in self.internal_links:
                self.internal_links.discard(i)
        
        if not self.internal_links:
            print("Exiting")
            sys.exit()

    def write_visited_links(self):
        with open("/home/bigpenguin/files/visited_links.txt","w") as self.v_file:
            self.v_file.write(self.parent_url)
            
    def Core_process(self):

        while True:
            crypt_obj.send_request()
            crypt_obj.extract_urls()
            crypt_obj.evaluate_links()
            crypt_obj.iframe_ads()
            crypt_obj.videos_ads()
            crypt_obj.image_ads()
            crypt_obj.next_url() 
            crypt_obj.write_visited_links()

class crypto_engine_ui(wx.Frame,crypto_engine):
    def visit_file(self):
        def read_link():
            with open("/home/bigpenguin/files/visited_links.txt","r") as self.read_file:
                self.have_link=self.read_file.read()
                print(self.have_link)
            self.url_text.SetLabel(label=str(self.have_link))
            wx.CallLater(1000,read_link)
            
        read_link()

    def __init__(self,parent,*args,**kwargs):
        super(crypto_engine_ui,self).__init__(parent,*args,**kwargs)
        
        self.cj_web_panel=wx.Panel(self,-1)
        self.SetBackgroundColour((36 , 40 , 36))
        self.Refresh()

        obj=crypto_engine()

        self.url_text=wx.StaticText(self.cj_web_panel,-1,label=obj.parent_url)
        self.url_text.SetForegroundColour((2,255,6))
        
        self.visit_file()

if __name__=='__main__':
    crypt_obj=crypto_engine()
    process1=multiprocessing.Process(target=crypt_obj.Core_process)
    process1.start()

    app = wx.App()
    frm = crypto_engine_ui(None,title="Eminuses",style=wx.DEFAULT_FRAME_STYLE)
    frm.SetSize(1900,800)
    frm.Maximize(True)
    frm.Show()
    app.MainLoop()


