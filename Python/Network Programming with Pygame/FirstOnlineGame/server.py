import socket
import threading

clientCount = 1

class Client:
    
    def __init__(self,name,color,socket):
        self.name = name
        self.socket = socket
        self.color = color
        self.id = clientCount

#addr = socket.getaddrinfo("172.25.75.225", 3950)[0] #Port can be any number above the "special" ones, the address is the address that will be the server
print(socket.gethostbyname(socket.gethostname()))
addr = socket.getaddrinfo(socket.gethostbyname(socket.gethostname()), 3950)[0] 
sock = socket.socket(addr[0], addr[1], addr[2])
sock.bind(addr[-1])
sock.listen()

n = int(input("How many people will be in the lobby? (Type a positive integer.) "))
clients = [] #clients list holds all sockets for each client

for i in range(n):
    print(f"Waiting for client #{i+1}")
    new = sock.accept()
    name = new[0].recv(9000).decode()
    new[0].send("hi".encode())
    color = new[0].recv(9000).decode()
    new[0].send('Connected!'.encode())
    client = Client(name, color, new[0])
    clientCount += 1
    clients.append(client) #clients will hold all of the sockets for each individual client

for client in clients:
    client.socket.recv(9000)

for i in range(n):
    print(f"Hello, {clients[i].name}!")

for client in clients: #This part sends the message to the clients saying they are ready to start sending and recieving
    client.socket.send("All players have joined!".encode())
    print(client.socket.recv(9000).decode())
#After all clients put in their information, each one would send the color they want to be. We need to send all info
for client in clients:
    #message will be in the form: "color id"
    client.socket.send(f"{client.color} {client.id}".encode())
    print(client.socket.recv(9000).decode())
    client.socket.send(str(n).encode()) #each client needs to know how many players there are in the match
    print(client.socket.recv(9000).decode())
#NOTE: Here we are sending each client, the information that THEY are

print("Sent all players their information!")
for client in clients:
    client.socket.send("Sent all players their information!".encode())
    client.socket.recv(9000)
#Once we hit this point, each client has created their respective player, now we need each of them to create instances of the others
for client1 in clients:
    for client2 in clients:
        if client2.id != client1.id:
            client1.socket.send(f"{client2.color} {client2.id}".encode())
            print(client1.socket.recv(9000).decode())
print("Sent all players others' information! ")



def receive(r,w):
    while True:
        clients[r].socket.send(clients[w].socket.recv(9000))

for i in range(n):
    for j in range(n):
        if i != j:
            threading.Thread(target = receive, args = (i,j)).start()

