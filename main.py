import tkinter as tk
import random

def next_turn(row,column):
    global player

    if butttons[row][column]['text'] == '' and check_winner() is False:
        butttons[row][column]['text'] = player
        
        if check_winner() is False:
            player = players[1] if player==players[0] else players[0] 
            label.config(text=(player + '\'s turn')) 
        
        elif check_winner() is True:
            label.config(text=(player + ' wins'))
        else:
            label.config(text='Tie')

def check_winner():
    for row in range(3):
        if butttons[row][0]['text'] == butttons[row][1]['text'] == butttons[row][2]['text'] != '':
            for column in range(3):
                butttons[row][column].config(bg='green')
            return True
    
    for column in range(3):
        if butttons[0][column]['text'] == butttons[1][column]['text'] == butttons[2][column]['text'] != '':
            for row in range(3):
                butttons[row][column].config(bg='green')
            return True

    if butttons[0][0]['text'] == butttons[1][1]['text'] == butttons[2][2]['text'] !='':
        for i in range(3):
                butttons[i][i].config(bg='green')
        return True

    if butttons[0][2]['text'] == butttons[1][1]['text'] == butttons[2][0]['text'] != "":
        for i in range(3):
                butttons[i][2-i].config(bg='green')
        return True

    elif empty_spaces() is False:
        return 'Tie'
    
    return False

def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if butttons[row][column]['text'] != '':
                spaces -=1

    if spaces:
        return True

    return False

def new_game():
    for row in range(3):
        for column in range(3):
            butttons[row][column].config(text='',bg='#383838')

window = tk.Tk()
window.title('Tic Tac Toe')
players = ['X','O']
player = random.choice(players)
butttons = [[0,0,0],
            [0,0,0],
            [0,0,0]]

label = tk.Label(text=player + '\'s turn', font=('Arial',40))
label.pack(side = 'top')

reset_button = tk.Button(text='restart', font=('Arial',20), command = new_game)
reset_button.pack(side = 'top')

frame = tk.Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        butttons[row][column] = tk.Button(frame, text='',font=('Arial',20),width=5, height=2, command=lambda row=row, column=column : next_turn(row,column))
        butttons[row][column].grid(row=row, column=column)

window.mainloop()