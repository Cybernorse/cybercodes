import requests
from bs4 import BeautifulSoup
import os
import difflib
import csv

'''designed new algorithm for a botnet to extract data from the web'''
os.remove("/root/bot_data_testing/botnet_webmining_data.csv")

def Cyber_norse_bot():              #extracting the websites data for links and saving them into the file 
    global cyber_filter
    global cyber_file
    global cyber_url
    cyber_url="https://en.wikipedia.org/wiki/Dark_web"
    
    cyber_session=requests.Session()
    cyber_request=cyber_session.get(cyber_url)
    cyber_text=cyber_request.text
    cyber_file= open ("/root/bot_data_testing/Cyber Norse Botnet.txt","w")
    cyber_link=BeautifulSoup(cyber_text , features='lxml')
    for cyber_links in cyber_link.find_all('a'):
        cyber_crawl=str(cyber_links.get('href'))            #filtering out the valid URLs 
        if "https" in cyber_crawl:
            cyber_filter=cyber_crawl
        if "http" in cyber_crawl:
            cyber_filter=cyber_crawl
            print(cyber_filter)
            cyber_file.write(cyber_filter+'\n')
        else :
            print("Invalid Url can't be processed : "+cyber_crawl)
    cyber_file.close()
    
def cyber_norse_bot_2():
    global cyber_filter2 
    global csv_file  
    global cyber_link2  
    global cyber_title               #reading the file for each link and and extracting links for each URL
    cyber_file= open ("/root/bot_data_testing/Cyber Norse Botnet.txt","r") 
    for cyber_index in cyber_file.readlines():
        cyber_session2=requests.Session()
        cyber_request2=cyber_session2.get(cyber_index)
        cyber_text2=cyber_request2.text
        cyber_link2=BeautifulSoup(cyber_text2,features='lxml')
        cyber_title=cyber_link2.title.string
        for cyber_links2 in cyber_link2.find_all('a'):
            cyber_crawl2=str(cyber_links2.get('href'))
            try:
                if "https" in cyber_crawl2:
                    cyber_filter2=cyber_crawl2
                elif "http" in cyber_crawl2:
                    cyber_filter2=cyber_crawl2            
                else: 
                    cyber_filter2= cyber_url+cyber_crawl2
                print(cyber_filter2)
            except:
                print("invalid Url can't be processed : "+cyber_crawl2)
            with open("/root/bot_data_testing/botnet_webmining_data.csv","a") as csv_file:
#                csv_file.seek(0)
#                csv_file.truncate()
                botnet_webmining_data()
        cyber_file.close()
    with open("/root/bot_data_testing/Cyber Norse Botnet.txt","a") as cyber_file:
        cyber_norse_bot_3()                 #opening the file in write mode to write results of the read file process 
        cyber_norse_bot_2()             #indirect and direct recursion
                                                #once the results of the file has been written the cyber_norse_bot_2() will called again 
                                               #and the new urls will be processed.
                
def cyber_norse_bot_3():

        cyber_file.write(str(cyber_filter2))
        cyber_file.flush()
        os.fsync(cyber_file.fileno())

def botnet_webmining_data():
        
        cyber_words='Hacker Lexicon : What Is the Dark Web ? | WIRED'
        str_cyber_title=str(cyber_title)
      #  for para in cyber_link2.find_all('p',text=True,recursive=True):
        web_iter=[text_iter for text_iter in str_cyber_title]
        rep_web=str(web_iter)
        rep_seq=rep_web.replace('[','').replace(']','').replace("'",'').replace(',','').replace(' ','')
        diff_seq=difflib.SequenceMatcher()
        diff_seq.set_seqs(rep_seq,cyber_words)
        seq_ratio=diff_seq.ratio()
               
        print(seq_ratio)
                
        if seq_ratio >= 0.6 :
            csv_text=csv.writer(csv_file,dialect='excel')
            csv_text.writerow(str_cyber_title.strip('\n'))
            
                
#        for spans in cyber_link2.find_all('spans',text=True,recursive=True):
#             if not spans:
#                print("Text does not exit in " + cyber_link2)
#             else :
#                csv_file.write(str(spans) + '\n')

def count_links():
    links = sum(1 for line in open("/root/bot_data_testing/Cyber Norse Botnet.txt"))
    print("\n\n"+ str(links) +"\n\n" )
    links_count=open("/root/bot_data_testing/links.txt","a") 
    links_count.write(str(links)+'\n')
    links_count.close()
    
if __name__=="__main__":
   # try:     
        Cyber_norse_bot()
        cyber_norse_bot_2()
#    except:
#        print("\n\n#### Unidentified Encounter #### Dropping the Bot ")
#        count_links()
    
 