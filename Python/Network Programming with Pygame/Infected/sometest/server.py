import socket
from player import *
import threading
import pickle

def player_thread(player):
    thread = threading.Thread(target = update_player, args = (player,))
    thread.run()

def update_player(player, players):
    while True:
        player = pickle.loads(player.sock.recv(9000)) #new player object (gets "rewritten")
        for player2 in players:
            if player2 != player:
                player2.sock.send(pickle.dumps(player))





addr = socket.gethostbyname(socket.gethostname())
print(addr)
sock = socket.socket()
sock.bind((addr, 3550))
sock.listen()

n = int(input("How many players: "))

players = []
id = 0

for i in range(n):
    new = sock.accept()[0]
    color = new.recv(100).decode()
    player = Player(color, new, id)
    players.append(player)
    player.sock.send(pickle.dumps(player)) #sending the player
    id += 1
    
for player in players:
    player.sock.send("Done".encode())

#At this point, all player classes have been created (So they need to wait before)

for player in players:
    player_thread(player)