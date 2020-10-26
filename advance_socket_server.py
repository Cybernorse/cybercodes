import socket
import time
binded_ip='0.0.0.0'
binded_port=5555
binded_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
while True:
    print("#Binding the ip adress and port....")
    time.sleep(3)
    break
binded_client.bind((binded_ip,binded_port))
while True:
    print("#listening to the request....")
    time.sleep(2)
    break
binded_client.listen(5)
conn,addr=binded_client.accept()
while True:
    print("#Connection info : ",conn )
    time.sleep(2)
    print("#Binded ip address and port : ",addr )
    time.sleep(2)
    print("#Sending data to the client....")
    time.sleep(1)
    break
while True:
    
    clients_data=conn.recv(4065)
    if not clients_data:break
    conn.send(clients_data)
while True:
    print("#Closing the connection....")
    time.sleep(1)
    break
conn.close()
