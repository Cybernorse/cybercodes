import urllib
import requests
import lxml.html
from lxml.html import fromstring
from bs4 import BeautifulSoup
def Link_Bot(max_pages):
    pages=1
    while pages <= max_pages:
        try:
            google_url="https://www.google.com/search?q=<dark web>"
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
        except:
            print("\nUnidentified Query Encountered")
            
def deep_bot(big_link):
    big_title=BeautifulSoup(urllib.request.urlopen(big_link),features='lxml')
    print(big_title.title.string + '\n')
    big_source=requests.get(big_link)
    big_text=big_source.text
    big_para=BeautifulSoup(big_text,features='lxml')
    for para in big_para.p.find_all(text=True,recursive=True):
        print(para)
    
Link_Bot(1)  
    