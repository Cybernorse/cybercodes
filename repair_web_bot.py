import urllib
import requests
import lxml.html
from lxml.html import fromstring
from bs4 import BeautifulSoup
import os

query_file=open("/root/bot_data_testing/Cyber Bot.txt","w")
def main_bot():
    #creating file for the query 
    query_file=open("/root/bot_data_testing/Cyber Bot.txt","w")
    query_file.write("cyber crime")
    query_file=open("/root/bot_data_testing/Cyber Bot.txt","r") 
    while True:
        try:                                                            #giving the initial query to the bot
            for query_line in query_file.readlines():                    #reading each line for the query 
                gen_query="https://www.google.com/search?q=<"+ query_line +">"            #searching the query 
                url_source=requests.get(gen_query)                     
                web_text=url_source.text                           #getting the content converting it into text and string
                string_web=fromstring(web_text)
                for query_link in string_web.cssselect('.r a'):                         #extracting all the URLs of the website from the searched query 
                    url_link=query_link.get('href')
                    if url_link.startswith('/url?'):
                        url_link=urllib.parse.parse_qs(urllib.parse.urlparse(url_link).query)['q']
                        post_url=url_link[0]
                        print(post_url)
                        twin_bot(post_url)
                        print('\n')
                        query_file.close()
                        query_file.close()
                            
        except:
                #query_file.close()
            query_file=open("/root/bot_data_testing/Cyber Bot.txt","r")
            for deep_query in query_file.readlines():
                twin_bot(deep_query)
                query_file.close()
def twin_bot(big_link):
    crime_keys="crime"                                 #'''keywords : Owlcity : silk road : drug vendor : shadow web'''
    power_bot=requests.get(big_link)
    power_text=power_bot.text
    big_title=BeautifulSoup(power_text,features='lxml')
    print(big_title.title.string + '\n')
    big_source=requests.get(big_link)
    big_text=big_source.text
    big_para=BeautifulSoup(big_text,features='lxml')
    for web_links in big_para.find_all('a'):
        big_links=str(web_links.get('href'))
        if crime_keys in big_links:
            if 'https' in big_links:
               org_links=big_links
            if 'http' in big_links:
               org_links=big_links
               query_file.write(org_links+'\n')
               query_file.flush()
               os.fsync(query_file.fileno())
               print(org_links)
               for para in big_para.p.find_all(text=True,recursive=True):
                    cyber_crime=open("/root/bot_data_testing/cyber criminal data.txt","w")
                    cyber_crime.write(para+'\n')
                    cyber_crime.flush()
                    os.fsync(cyber_crime.fileno())
                    cyber_crime.close()
                
        #query_file.close()
    
    
main_bot()
               
               
        