import socket
import time
import sys

server_ip='0.0.0.0'
server_port=6666
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
while True:
    print("#connecting with the IP and port....")
    time.sleep(2)
    break
server.connect((server_ip,server_port))
data="encoded data is moving around the socket"
while True:
    print("#sending data to the server....")
    time.sleep(3)
    break
server.send(data.encode("UTF-8"))
while True:
    print("#Recieving data from the server....")
    time.sleep(2)
    print("#Data retrieved....")
    time.sleep(1)
    break
raw_data=(server.recv(6000).decode('UTF-8'))
data_show=input("enter y to confirm the data or n to exit >> : ")
if (data_show=="y" or data_show=="Y"):
	while True:
		print("Data recieved from the server : ")
		print(raw_data)
		break
elif (data_show=="n" or data_show=="N"):
	while True:
		print("Exiting the session....")
		time.sleep(2)
		break
sys.exit()
        





