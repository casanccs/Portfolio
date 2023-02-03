import os
def c():
    os.system('cls')
c()
bp = ['♔','♕','♖','♗','♘','♙']
wp = ['♚','♛','♜','♝','♞','♟']
b = ' '
sp = ('a1','a2','a3','a4','a5','a6','a7','a8',
    'b1','b2','b3','b4','b5','b6','b7','b8',
    'c1','c2','c3','c4','c5','c6','c7','c8',
    'd1','d2','d3','d4','d5','d6','d7','d8',
    'e1','e2','e3','e4','e5','e6','e7','e8',
    'f1','f2','f3','f4','f5','f6','f7','d8',
    'g1','g2','g3','g4','g5','g6','g7','g8',
    'h1','h2','h3','h4','h5','h6','h7','h8')
s = {'a1' : wp[2], 'a2' : wp[5], 'a3' : b, 'a4' : b, 'a5' : b, 'a6' : b,
    'a7' : bp[5], 'a8' : bp[2],
    'b1' : wp[4], 'b2' : wp[5], 'b3' : b, 'b4' : b, 'b5' : b, 'b6' : b, 'b7' :
    bp[5], 'b8' : bp[4],
    'c1' : wp[3], 'c2' : wp[5], 'c3' : b, 'c4' : b, 'c5' : b, 'c6' : b, 'c7' :
    bp[5], 'c8' : bp[3],
    'd1' : wp[1], 'd2' : wp[5], 'd3' : b, 'd4' : b, 'd5' : b, 'd6' : b, 'd7' :
    bp[5], 'd8' : bp[0],
    'e1' : wp[0], 'e2' : wp[5], 'e3' : b, 'e4' : b, 'e5' : b, 'e6' : b, 'e7' :
    bp[5], 'e8' : bp[1],
    'f1' : wp[3], 'f2' : wp[5], 'f3' : b, 'f4' : b, 'f5' : b, 'f6' : b, 'f7' :
    bp[5], 'f8' : bp[3],
    'g1' : wp[4], 'g2' : wp[5], 'g3' : b, 'g4' : b, 'g5' : b, 'g6' : b, 'g7' :
    bp[5], 'g8' : bp[4],
    'h1' : wp[2], 'h2' : wp[5], 'h3' : b, 'h4' : b, 'h5' : b, 'h6' : b, 'h7' :
    bp[5], 'h8' : bp[2],}

board = f"""
8|{s['a8']} {s['b8']} {s['c8']} {s['d8']} {s['e8']} {s['f8']} {s['g8']}
{s['h8']}
7|{s['a7']} {s['b7']} {s['c7']} {s['d7']} {s['e7']} {s['f7']} {s['g7']}
{s['h7']}
6|{s['a6']} {s['b6']} {s['c6']} {s['d6']} {s['e6']} {s['f6']} {s['g6']}
{s['h6']}
5|{s['a5']} {s['b5']} {s['c5']} {s['d5']} {s['e5']} {s['f5']} {s['g5']}
{s['h5']}
4|{s['a4']} {s['b4']} {s['c4']} {s['d4']} {s['e4']} {s['f4']} {s['g4']}
{s['h4']}
3|{s['a3']} {s['b3']} {s['c3']} {s['d3']} {s['e3']} {s['f3']} {s['g3']}
{s['h3']}
2|{s['a2']} {s['b2']} {s['c2']} {s['d2']} {s['e2']} {s['f2']} {s['g2']}
{s['h2']}
1|{s['a1']} {s['b1']} {s['c1']} {s['d1']} {s['e1']} {s['f1']} {s['g1']}
{s['h1']}
a b c d e f g h
"""

def move():
    while True:
        what = input('enter position of piece: ')
        if s[what] == ' ':
            c()
            print(board)
            print()
            print("There is no peice there")
            continue
        where = input('enter the destination of peice: ')
        if s[where] != ' ':
            print(board)
            c()
            print()
            print("That space is occupied")
            continue
        s[where] = s[what]
        c()
        break

while True:

    board = f"""
    8|{s['a8']} {s['b8']} {s['c8']} {s['d8']} {s['e8']} {s['f8']} {s['g8']} {s['h8']}
    7|{s['a7']} {s['b7']} {s['c7']} {s['d7']} {s['e7']} {s['f7']} {s['g7']} {s['h7']}
    6|{s['a6']} {s['b6']} {s['c6']} {s['d6']} {s['e6']} {s['f6']} {s['g6']} {s['h6']}
    5|{s['a5']} {s['b5']} {s['c5']} {s['d5']} {s['e5']} {s['f5']} {s['g5']} {s['h5']}
    4|{s['a4']} {s['b4']} {s['c4']} {s['d4']} {s['e4']} {s['f4']} {s['g4']} {s['h4']}
    3|{s['a3']} {s['b3']} {s['c3']} {s['d3']} {s['e3']} {s['f3']} {s['g3']} {s['h3']}
    2|{s['a2']} {s['b2']} {s['c2']} {s['d2']} {s['e2']} {s['f2']} {s['g2']} {s['h2']}
    1|{s['a1']} {s['b1']} {s['c1']} {s['d1']} {s['e1']} {s['f1']} {s['g1']} {s['h1']}
      a b c d e f g h
    """
    print(board)
    move()