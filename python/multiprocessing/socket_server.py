import socket
from fib import fib
from threading import Thread
def _server(address):
    
    # Set up code to create 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    sock.bind(address)
    sock.listen(5)

    while True:
        client, addr = sock.accept()
        print("Connect to {}".format(addr))
        t = Thread(target= _handler, args=(client, ))
        t.start()
        

def _handler(client):
    request =''

    while True:
        value = 0
        request += client.recv(1024).decode("utf-8") 
        if not request:
            break
        if not request.endswith("\n"):
            continue

        try:
            value = int(request)
        except:
            print("issue")
        res = fib(value)
        result = b'\n' + str(res).encode('ascii') + b'\n'
        client.send(result)
        request =''
    
    print("Done")

_server(("", 25000))
   