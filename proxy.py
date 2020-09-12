import proxyscrape
import requests

''' Splinter is a module that can be used to interact with website anonymously by the help of stem module ---- 
 here is the code ---- http://www.thedurkweb.com/automated-anonymous-interactions-with-websites-using-python-and-tor/''' 
 
class alter_proxy:
    def __init__(self,*args,**kwargs):
        
        headers = {
                    "Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain",
                    "User-agent":"Mozilla/5.0 (Linux NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0",
                }
        cookies={'enwiki_session': '17ab96bd8ffbe8ca58a78657a918558'}
        
        self.proxy_app=[]
        self.proxy_dict={}
        protocol='https'
        self.collect_proxy=proxyscrape.create_collector('proxy',[protocol])
            
        self.getproxy=self.collect_proxy.get_proxy({'code':('us','uk'),'anonymous':True})
        
        for i in self.getproxy:
            self.proxy_app.append(i)
        
        self.proxy_dict[self.proxy_app[len(self.proxy_app)-2]]=self.proxy_app[0]+':'+self.proxy_app[1]
        
        print(self.proxy_dict)
        
        # cyber_url="https://www.funimation.com"
        
        # request_session=requests.Session()
        # request_session.proxies=self.proxy_dict
        # out_req=request_session.get(cyber_url,headers=headers,cookies=cookies).text
        
        # print(out_req)

if __name__=='__main__':

    alter=alter_proxy()
    