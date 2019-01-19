import requests
from bs4 import BeautifulSoup
import os

'''designed new algorithm for a botnet to extract data from the web''' 

def Cyber_norse_bot():              #extracting the websites data for links and saving them into the file 
    global cyber_filter
    global cyber_file
    cyber_url="https://darkwebnews.com"
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
    global cyber_filter2                    #reading the file for each link and and extracting links for each URL
    cyber_file= open ("/root/bot_data_testing/Cyber Norse Botnet.txt","r") 
    for cyber_index in cyber_file.readlines():
        cyber_session2=requests.Session()
        cyber_request2=cyber_session2.get(cyber_index)
        cyber_text2=cyber_request2.text
        cyber_link2=BeautifulSoup(cyber_text2,features='lxml')
        for cyber_links2 in cyber_link2.find_all('a'):
            cyber_crawl2=str(cyber_links2.get('href'))
            if "https" in cyber_crawl2:
                cyber_filter2=cyber_crawl2
            if "http" in cyber_crawl2:
                cyber_filter2=cyber_crawl2
                print(cyber_filter2)
            else:
                print("invalid Url can't be processed : "+cyber_crawl2)
        cyber_file.close()
    with open("/root/bot_data_testing/Cyber Norse Botnet.txt","w") as cyber_file:
        cyber_norse_bot_3()                 #opening the file in write mode to write results of the read file process 
        cyber_norse_bot_2()             #indirect and direct recursion
                                        #once the results of the file has been written the cyber_norse_bot_2() will called again 
                                       #and the new urls will be processed.
        
def cyber_norse_bot_3():

        cyber_file.write(str(cyber_filter2))
        cyber_file.flush()
        os.fsync(cyber_file.fileno())
    
if __name__=="__main__":     
    Cyber_norse_bot()
    cyber_norse_bot_2()