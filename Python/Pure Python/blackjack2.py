import keyboard
from time import sleep
from os import system
from random import randint, choice

deck = [["Ace",11]]*4 + [["King", 10]]*4 + [["Queen", 10]]*4 + [["Jack", 10]]*4 + 4*list(zip(list("23456789") + [10],list(range(2,10))))
chance = dict(zip(range(12,22),(100,90,80,70,60,50,30,10,5,0)))
chance.update(zip(range(0,12),[100]*12))
chance.update(zip(range(22,50),[0]*38))

class Entity:
    def __init__(self):
        self.ace = 0
        self.score = 0 
        self.hand = []
        self.turn = True
    
    def draw(self):
        global deck
        card = choice(deck)
        self.hand.append(card)
        self.score += card[1]
        deck.remove(card)
        if card[0] == "Ace":
            self.ace += 1
        if self.score > 21 and self.ace > 0:
            self.ace -= 1
            self.score -= 10
        elif self.score > 21:
            self.turn = False

    def show(self):
        print("Computer :")
        print("Hand: \n  ", f"{self.hand[0][0]} and {len(self.hand) - 1} more cards..." ,"\n   Score: ?")
    def show2(self):
        print("Computer :")
        print("Hand: \n  ", [x[0] for x in self.hand] ,"\n   Score: ", int(self.score))
    

class Player(Entity):
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.bet = 0 #So that I can execute self.money += self.bet at the end on everyone no matter what
        Entity.__init__(self)

    def show(self):
        print(self.name, ":")
        print(f"Money: {self.money} | Bet: {self.bet}")
        print("Hand: \n  ", [x[0] for x in self.hand] ,"\n   Score: ", int(self.score) , "   |  Ace's: ", self.ace)
    def reset(self):
        self.__init__(self.name,self.money)

    
def resetDeck():
    global deck
    deck = [["Ace",11]]*4 + [["King", 10]]*4 + [["Queen", 10]]*4 + [["Jack", 10]]*4 + list(zip(list("123456789") + [10],list(range(2,10))))

def read(lines, person):
    for ind in lines:
        id = ind.split()
        if id[0] == person:
            return id[0],id[1]
    else:
        print(person, "not found in system!")
        return None


system('cls')
file = open('blackjack2.txt','r')
saved = file.readlines()
players = []

n = int(input('How many players will there be? (Up to 4): '))
for i in range(n):
    while True:
        if input('Player ' + str(i+1) + ", do you have a saved person? (y/n): ") == 'y':
            savedPerson = input("What is the saved name?: ")
            pers = read(saved, savedPerson)
            if pers != None:
                players.append(Player(pers[0],int(pers[1])))
                break
            else:
                continue
        else:
            name = input("What is your name?: ")
            players.append(Player(name,5000))
        break
while True:
    system('cls')


    print()
    for player in players:
        print(player.name + "'s", "money: ", player.money)

    for player in players:
        while True:
            player.bet = int(input(f"({player.name}) What is your bet?: "))
            if player.bet > player.money:
                print("You bet more than you have!")
                continue
            else:
                break

    system('cls')

    comp = Entity()
    comp.draw()
    comp.draw()
    print(f"Turns: (Computer: {comp.turn})", end = "")
    for player in players:
        print(f" ({player.name}: {player.turn}) ", end = "")
    print()
    comp.show()
    print("--------------------------\n--------------------------")
    for player in players:
        player.draw()
        player.draw()
        player.show()
        print("--------------------------")
    while True in [b.turn for b in players]:
        
        for player in players:
            if player.turn == True:
                if input(f"({player.name}) Hit? (y/n): ") == "y":
                    player.draw()
                else:
                    player.turn = False
        
        system('cls')
        if comp.turn:
            if randint(1,100) <= chance[comp.score]:
                comp.draw()
                
            else:
                comp.turn = False
        print(f"Turns: (Computer: {comp.turn})", end = "")
        for player in players:
            print(f" ({player.name}: {player.turn}) ", end = "")
        print()
        comp.show()
        print("--------------------------\n--------------------------")
        for player in players:
            player.show()
            print("--------------------------")
    else:
        system('cls')
        comp.show2()
        print("--------------------------\n--------------------------")
        for player in players:
            player.show()
            print("--------------------------")
    for player in players:
        print(f"{player.name}: ", end = "")
        if player.score > 21 and comp.score > 21 or player.score == comp.score:
            print("Tie! ", end = "")
        if (player.score > 21 and comp.score <= 21) or (comp.score <= 21  and player.score <= 21 and (player.score < comp.score)):
            print("You lose! ", end = "")
            player.money -= player.bet
        if (player.score <= 21 and comp.score > 21) or (comp.score <= 21 and player.score <= 21 and (player.score > comp.score)):
            print("You win! ", end = "")
            player.money += player.bet
        print(f"| Bet: {player.bet} | Current Money: {player.money}")
    print("Game over")
    again = input("Do you want to play again? (y/n): ")
    if again == "y":
        for player in players:
            player.reset()
        resetDeck()
        continue
    else:
        break
print("Saving...")
for pl in players:
    for i,line in enumerate(saved):
        id = line.split()
        if id[0] == pl.name:
            id[1] = str(pl.money)
            saved[i] = " ".join(id) + "\n"
            break
    else:
        saved.append(f"{pl.name} {pl.money}\n")
file = open("bj1players.txt","w")
for line in saved:
    file.write(line)
file.close()
print("Saved.")