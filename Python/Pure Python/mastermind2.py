from random import choice
import keyboard
from os import system
from time import sleep

def cc():
    system('cls')


def pBoard(ans,bo, pe, t):
    print("   ┌" + "-"*34 + "┐")
    print(f"   |  {ans[0]}  {ans[1]}  {ans[2]}  {ans[3]}  ||  _  _  _  _  |")
    for i in range(len(bo)-1,-1,-1):
        print("   |" + "-"*34 + "|")
        if i == 9:
            s = " "
        else:
            s = "  "
        if i == t:
            c = "←"
        else:
            c = ""
        print(f"{i+1}{s}|  {bo[i][0]}  {bo[i][1]}  {bo[i][2]}  {bo[i][3]}  ||  {pe[i][0]}  {pe[i][1]}  {pe[i][2]}  {pe[i][3]}  |  {c}")
    print("   └" + "-"*34 + "┘")

def check(ans, guess):
    i = 0
    o = 0
    for j in range(4):
        if guess[j] in ans:
            if guess[j] == ans[j]:
                i += 1
            else:
                o += 1
    return ["●"]*i + ["○"]*o + [" "]*(4 - i - o)

def check2(ans,guess):
    #check for matching i's and memorize the spots
    #check for matching o's that have not been taken, and memorize the spots
    spots = []
    chosen = []
    i = 0
    o = 0
    #checking for number of i's
    for j in range(4):
        if guess[j] == ans[j]:
            i += 1
            spots.append(j)
            chosen.append(j)
    #now have CORRECT number of i's and the spots where the i's were at
    for j in range(4):
        for k in range(4):
            if guess[j] == ans[k] and (k not in spots) and (j not in chosen):
                o += 1
                spots.append(k)
                break
    return ["●"]*i + ["○"]*o + [" "]*(4 - i - o)

empty = "⚫"
choices = ["🔴", "🔵", "🟢", "🟡", "🟣", "⚪"]
right = "●"
wrong = "○"
arr = "↑"

board = [[empty for _ in range(4)] for _ in range(10)]
pegs = [[" " for _ in range(4)] for _ in range(10)]




cur = 0
Turn = 0
WON = False
lpress = False
rpress = False
spress = False
npress = [False for _ in range(6)]

while True:
    while True:
        cc()
        if input("1 player or 2 players? (Someone will make a code, another will guess) (type 1 or 2): ") == "2":
            print("Choices are: ")
            print(f"""1 -> {choices[0]} | 2 -> {choices[1]} | 3 -> {choices[2]} | 4 -> {choices[3]} | 5 -> {choices[4]} | 6 -> {choices[5]}""")
            print(f"Enter a single digit indicating the code. Ex: 1153 -> {choices[0]} {choices[0]} {choices[4]} {choices[2]}")
            code = input("Code: ")
            answer = [choices[int(code[0])-1],choices[int(code[1])-1],choices[int(code[2])-1],choices[int(code[3])-1]]
            if input(f"Your code is: {answer}, is this right? (type y or n): ") == "y":
                break
        else:
            answer = [choice(choices), choice(choices),choice(choices), choice(choices)]
            break

    if input(f'Choose the check rule:\n    (1) The pegs check independently regardless of what the other pegs are. Ex: \n    answer = {["🔴","🔴","🟢","🟢"]} guess = {["🔴","🔴","🔴","🔴"]} pegs = {["●","●","○","○"]}\n    (2) The pegs depend on the others. Ex:\n    answer = {["🔴","🔴","🟢","🟢"]} guess = {["🔴","🔴","🔴","🔴"]} pegs = {["●","●"," "," "]}\n(type 1 or 2) : ') == '1':
        checker = check
    else:
        checker = check2

    while Turn < 10 and not WON:
        cc()
        print("MASTERMIND")
        pBoard(["??","??","??","??"],board,pegs, Turn)
        print(" "*7 + " "*4*cur + arr)
        print("")
        print(f"""Rules:
        The arrow is where your current guess will be placed.
        You can move the arrow with the LEFT and RIGHT arrow keys on your keyboard.
        By pressing a number, the corresponding color will be selected for that guess.
        When you are done with the full guess, press SPACEBAR to see the results and move onto the next guess.
        {right} : Means that a color is in the right spot, but you don't know which color it is.
        {wrong} : Means a color is in the wrong spot, but you don't know which one.\n""")
        print(f"1 -> {choices[0]} | 2 -> {choices[1]} | 3 -> {choices[2]} | 4 -> {choices[3]} | 5 -> {choices[4]} | 6 -> {choices[5]}")

        num = False
        while True: #This loop will check when you press on a keyboard
            if keyboard.is_pressed("left arrow") and not lpress:
                cur -= 1
                if cur == -1:
                    cur = 3
                lpress = True
            elif not keyboard.is_pressed("left arrow") and lpress:
                lpress = False
                break
            if keyboard.is_pressed("right arrow") and not rpress:
                cur += 1
                if cur == 4:
                    cur = 0
                rpress = True
            elif not keyboard.is_pressed("right arrow") and rpress:
                rpress = False
                break

            if not keyboard.is_pressed("right arrow") and not keyboard.is_pressed("left arrow"): #Don't know why I need this
                for i in range(6):
                    if keyboard.is_pressed(str(i+1)) and not npress[i]:
                        board[Turn][cur] = choices[i]
                        cur += 1
                        if cur == 4:
                            cur = 3
                        npress[i] = True
                    elif not keyboard.is_pressed(str(i+1)) and npress[i]:
                        npress[i] = False
                        num = True
            if keyboard.is_pressed("space") and not spress:
                pegs[Turn] = checker(answer, board[Turn])
                if pegs[Turn] == ["●"]*4:
                    WON = True
                Turn += 1
                cur = 0
                spress = True
            if not keyboard.is_pressed("space") and spress:
                spress = False
                break
            sleep(0.05)
            if num:
                break

    cc()
    print("MASTERMIND")
    pBoard(answer,board,pegs, Turn)
    print()
    if WON:
        print("Congratulations! You cracked the code!\n\n")
    else:
        print("Sorry! You didn't guess the code :(\n\n")
    
    if input("Player again? (y/n) : ") == "y":
        continue
    else:
        break