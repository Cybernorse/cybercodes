import urllib
import bs4
import sys
import time
#request attribute is not recognized by terminal but it is by the spyder3 Python IDE
url='http://ww1.haikyuu3.com/'
url1=urllib.request.urlopen(url).read().decode('utf-8','gbk')
for webdata in url1:
    sys.stdout.write(webdata)
print('\n\n\n\n\n\n')
while True:
    print("Generating second Script from the Specified URl : " +  url  )
    time.sleep(5)
    break
    print('\n\n\n\n\n\n')
parsing_web_data=bs4.BeautifulSoup(url1,features='xml')
retrieve_web_script=parsing_web_data.get_text(' ')
print(retrieve_web_script)
print('\n\n\n\n\n\n')
while True:
    print("Generating web server information from the Specified URL : "+ url)
    time.sleep(5)
    break
print('\n\n\n\n\n\n')
url2=urllib.response.addinfo(headers='Content-Type==text/html',fp=url1)
print(url2)
print('\n\n\n\n\n\n')
while True:
    print("Retrieving the webpage from the Specified URL : "+ url)
    time.sleep(5)
    break
print('\n\n\n\n\n\n')
urllib.request.urlretrieve(url,'/root/webretrieval.html')
