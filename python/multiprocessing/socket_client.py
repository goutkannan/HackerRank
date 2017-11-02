"""
Client to test micro service 
""" 


import socket
import time
 
 
TCP_IP = '127.0.0.1'
TCP_PORT = 25000
BUFFER_SIZE = 1024
MESSAGE = "12"
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while True:
    start = time.time()
    s.send(MESSAGE.encode('utf-8'))
    end =time.time()
    time.sleep(0.50)
    print(end - start)

#data = s.recv(BUFFER_SIZE)
s.close()

 
#print("received data:", data)
