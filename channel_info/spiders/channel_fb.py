import scrapy 
from scrapy.selector import Selector
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys
from urllib.request import urlparse
import re
from scrapy.exceptions import CloseSpider

class channel_about_info(scrapy.Spider):
    name='ycfi'
    allowed_domain=['www.facebook.com']
    def __init__(self,*args, **kwargs):
        super(channel_about_info, self).__init__(*args, **kwargs)
        self.count=0
        self.nasty_duplicates=[]
        with open('/home/linuxw/Downloads/channel_names.csv','r') as f:
            self.channels_name=[i for i in f.readlines()]

    def start_requests(self):
        start_urls=['https://www.google.com/']
        yield SeleniumRequest(
            url=start_urls[0],
            callback=self.parse,
            wait_time=10,
            screenshot=True
            )
    
    def parse(self,response):
        self.driver = response.request.meta['driver']
        self.count+=1
        channel_link=[]

        print("############",self.channels_name[self.count],self.count,"############")
        # self.channels_name[self.count]
        query=self.channels_name[self.count]+" "+"facebook"
        search=self.driver.find_element_by_name('q')
        search.send_keys(query)
        search.send_keys(Keys.RETURN)
        search.clear()
        
        try:
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.ID,"pnnext")))
        except:
            time.sleep(10)

        results=Selector(text=self.driver.page_source).response.xpath('//div[@class="r"] /a/@href').getall()
        print(results)
        for i in results:
            if "www.facebook.com"==urlparse(i).netloc.lower():
                channel_link.append(i)
        
        if len(channel_link)==0:
            yield SeleniumRequest(
                url='https://www.google.com/',
                callback=self.parse,
                wait_time=10,
                screenshot=True,
                dont_filter=True
            )

        self.driver.save_screenshot('image1.png')

        if channel_link[0] in self.nasty_duplicates:
            yield SeleniumRequest(
                url='https://www.google.com/',
                callback=self.parse,
                wait_time=10,
                screenshot=True,
                dont_filter=True
            )

        self.nasty_duplicates.append(channel_link[0])

        try:
            yield SeleniumRequest(
                url=channel_link[0],
                callback=self.likes_follow,
                wait_time=10,
                # wait_until= EC.presence_of_element_located((By.CLASS_NAME,"_2yav")),
                screenshot=True,
                dont_filter=True
                )
        except:
            yield SeleniumRequest(
                url='https://www.google.com/',
                callback=self.parse,
                wait_time=10,
                screenshot=True,
                dont_filter=True
            )

    def likes_follow(self,response):
        self.channel_type=[]
        self.pc=[]
        self.l_f=[]
        if response.xpath('//div[@class="_4bl9"]/ div//text()').getall()[0:2]:
            self.l_f=response.xpath('//div[@class="_4bl9"]/ div//text()').getall()[0:2]

        if response.xpath('//div[@class="_3qn7 _61-0 _2fyi _3qnf _2pi9 _3-95"]/span/text()').getall():
            self.pc=response.xpath('//div[@class="_3qn7 _61-0 _2fyi _3qnf _2pi9 _3-95"]/span/text()').getall()

        if response.xpath('//a[@class="_81ge"]/text()').getall():
            self.path1=response.xpath('//a[@class="_81ge"]/text()').getall()
            self.channel_type=[self.path1[len(self.path1)-1]]

        try:
            set_url=''
            set_url=self.driver.current_url
            if not str(set_url).endswith('/'):
                set_url+='/'
            self.aboutc=urlparse(self.driver.current_url).scheme+"://"+urlparse(self.driver.current_url).netloc+"/pg"+urlparse(self.driver.current_url).path+"about/?ref=page_internal"
            # get_aboutc=self.driver.find_element_by_xpath('//div[@class="_2yaa"]')
            # get_aboutc.click()
            # try:
            #     WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.CLASS_NAME,"_50f7")))
            # except:
            #     time.sleep(10)

        except Exception as e:
            print(e)
            yield SeleniumRequest(
            url='https://www.google.com/',
            callback=self.parse,
            wait_time=10,
            screenshot=True,
            dont_filter=True
            )

        self.driver.save_screenshot('image2.png')
        print(self.aboutc)

        yield SeleniumRequest(
            url=self.aboutc,
            callback=self.get_about,
            wait_time=10,
            screenshot=True,
            dont_filter=True
            )
    
    def get_about(self,response):
        ids=[]
        description=response.xpath('//div[@class="_3-8w"]/text()').getall()+response.xpath('//div[@class="text_exposed_root"]/text()').getall()+response.xpath('//span[@class="text_exposed_show"]/text()').getall()
        for i in response.xpath('//meta/@content').getall():
            if "?id" in i :
                search=re.findall(r"(=)(.*)",i)         
                ids.append(search[0][1])

        print(self.channel_type)

        if not self.channel_type:
            self.channel_type=response.xpath('//div[@class="_4bl9 _5m_o"] //a/text()').getall()

        yield{
            'id':ids,
            'channel name':self.channels_name[self.count],
            'type of channel':self.channel_type,
            'likes and follows':[' '.join(self.l_f)],
            'page creation date':self.pc,
            'description':[' '.join(description)],
            
        }

        if self.channels_name[len(self.channels_name)-1] == self.channels_name[self.count]:
            raise CloseSpider('{!}{!}{!}{!}	Extraction Complete	{!}{!}{!}{!}')

        yield SeleniumRequest(
            url='https://www.google.com/',
            callback=self.parse,
            wait_time=10,
            screenshot=True,
            dont_filter=True
            )

