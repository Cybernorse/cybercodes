from bs4 import BeautifulSoup
import requests 
import urllib
import sys
url = 'www.tuf.edu.pk'
url2="www.tuf.edu.pk/"
r  = requests.get("http://" +url) 
data = r.text 
print(data)
soup = BeautifulSoup(data,features='lxml') 
for link in soup.find_all('a'):
       weblinks=(link.get('href'))
       print(weblinks)
       
       if weblinks and 'http' and 'https' not in weblinks:
              try:
                  weblink_repair="https://www.tuf.edu.pk/"+weblinks
                  linkbots=urllib.request.urlopen(weblink_repair).read().decode('utf-8')
                  for linkrobots in linkbots:
                      sys.stdout.write(linkrobots)
                  print('\n')
              except:
                  try:
                      linkbots=urllib.request.urlopen(weblinks).read().decode('utf-8')
                      for linkrobots in linkbots:
                          sys.stdout.write(linkrobots)
                  except:
                      try:
                          weblink_repair="https://www.tuf.edu.pk/"+weblinks
                          linkbots=urllib.request.urlopen(weblink_repair).read().decode('utf-8')
                          for linkrobots in linkbots:
                              sys.stdout.write(linkrobots)
                      except:
                          print("Internel Server Error !")
                  
       else:
              if weblinks!='None':
                  try:
                      if weblinks is not None and 'http' or 'https' in weblinks:
                          try:
                               geturl=requests.get(weblinks)
                               parseurl=geturl.text
                               linkbots=BeautifulSoup(parseurl,features='lxml')
                               linktext=linkbots.get_text(' ')
                               for linkrobots in linktext:
                                   sys.stdout.write(linkrobots)
                               print('\n')
                          except:
                               print("Invalid URL format - Skipping...")
                               print('\n')
                  except TypeError:
                     print("Unsupported URL encountered")
                  
              else:
                   print("Unknown URL (Unsupported format)")
                
            