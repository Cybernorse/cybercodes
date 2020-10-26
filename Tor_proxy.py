from stem.control import Controller
from stem import Signal
from stem import process
import os
import subprocess
import time
import socks
import socket
# import signal
import requests
import signal
from selenium import webdriver
from webbot import Browser
# from selenium.webdriver.firefox.options import Options
# import splinter 

''' Selenium, splinter and webbot are modules that can be used to interact with website anonymously by the help of stem module ---- 
 ----  Selenium,webbot are working only'''

class Tor_Proxy:
    def tor_call(self):
    
        location = 'Downloads/tor-browser-linux64-9.0.1_en-US/tor-browser_en-US/Browser'
        
        for file in os.listdir(location):
            if file=='start-tor-browser':
            
                tor=os.path.join(location, file)
                self.tor_invoke=subprocess.Popen(['bash',str(tor)],stdout=subprocess.PIPE, preexec_fn=os.setsid)

    
    def proxy_for_pirate(self):
        
        ######################################################################################################
        
        cyber_url="http://icanhazip.com/"
        
        time.sleep(5)
        
        with Controller.from_port(port=9151) as controller:
            controller.authenticate()  # provide the password here if you set one
            controller.signal(Signal.NEWNYM)
            
            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150)
            socket.socket = socks.socksocket
        
            self.request_session=requests.Session()
            out_req=self.request_session.get(cyber_url).text.strip()
            print(out_req)
            
        # self.kill_tor()
    
    def kill_tor(self):
        os.killpg(os.getpgid(self.tor_invoke.pid), signal.SIGTERM)
    
    
if __name__=='__main__':
    # global tor_process
    proxy_obj=Tor_Proxy()

    # proxy_obj.tor_call()
    # proxy_obj.proxy_for_pirate()
    
    # time.sleep(5)
    
    proxy_obj.test_selenium()
