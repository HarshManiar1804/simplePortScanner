import socket
#object of socket 
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#host on which we need to know about port
host = "192.168.6.1"
#port number
port = 443

def portScan(port):
    #if this coondicion is right then the port is closed else the port is open
    if(sock.connect_ex((host,port))):
        print("connection closed")
    else:
        print("connection open")
        
portScan(port)