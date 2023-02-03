import socket
import threading

def ste(msg, sockets):
    for soc in sockets:
        soc.send(msg.encode())

def sendmsg(client, clients):
    while True:
        msg = client.socket.recv(9000).decode()
        for c in clients:
            try:
                c.socket.send(f"[{client.name}] {msg}".encode())
            except:
                pass

class Client():
    def __init__(self,name,soc):
        self.socket = soc
        self.name = name

addr1 = socket.gethostbyname(socket.gethostname())
#print(addr1)
addr2 = '2600:1700:4be0:1a40:455c:9d7e:d566:4c7b'

sock = socket.socket(family= socket.AF_INET6)
#sock = socket.socket()
sock.bind((addr2, 3550))
n = int(input("How many people will be on the server: "))

sock.listen()
sockets = []
clients = []
for i in range(n):
    new = sock.accept()[0]
    sockets.append(new)
    print(i+1)
ste("Everyone Connected", sockets)
for soc in sockets:
    clients.append(Client(soc.recv(9000).decode(),soc))
ste("Everyone inputted their name", sockets)

for client in clients:
    threading.Thread(target=sendmsg,args=(client,clients)).start()