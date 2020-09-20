import socket
host_target='www.google.com'
port_target=80
send_pac=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
send_pac.connect((host_target,port_target))
send_pac.send('POST / HTTP/1.1\r\nHost: google.com\r\n\r\n'.encode('utf-8'))
data=send_pac.recv(1024)
send_pac.close()
print('recieved: ',repr(data))