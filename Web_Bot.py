import urllib
import requests
import lxml.html
from lxml.html import fromstring
from bs4 import BeautifulSoup
query_file=open('/root/cyber crime.txt','w')
def Link_Bot(max_pages):
    pages=1
    while pages <= max_pages:
        try:
            query_file=open('/root/cyber crime.txt','w')
            query_file.write("cyber crime")
            query_file=open('/root/cyber crime.txt','r')
            for query_line in query_file.readlines():
                google_url="https://www.google.com/search?q=<"+ query_line +">"
                url_source=requests.get(google_url)
                web_text=url_source.text
                text_source=fromstring(web_text)
                for result in text_source.cssselect('.r a'):
                    url=result.get('href')
                    if url.startswith('/url?'):
                        url=urllib.parse.parse_qs(urllib.parse.urlparse(url).query)['q']
                        urls=url[0]
                        print(urls)
                        deep_bot(urls)
                        print('\n')
                    pages=pages+1
                query_file.close()
        except:
            print("\nUnidentified Query Encountered")
            query_file.close()
            
def deep_bot(big_link):
    big_title=BeautifulSoup(urllib.request.urlopen(big_link),features='lxml')
    print(big_title.title.string + '\n')
    big_source=requests.get(big_link)
    big_text=big_source.text
    big_para=BeautifulSoup(big_text,features='lxml')
    for web_links in big_para.find_all('a'):
        big_links=str(web_links.get('href'))
        if 'https' in big_links:
            org_links=big_links
        if 'http' in big_links:
            org_links=big_links
            print(org_links)
            query_file.write(org_links+'\n')
            print('\n')
        #for para in big_para.p.find_all(text=True,recursive=True):
         #   print(para)
Link_Bot(1)
     
  
    