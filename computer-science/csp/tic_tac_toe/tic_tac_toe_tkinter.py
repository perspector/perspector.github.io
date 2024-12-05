from tkinter import *
from tkinter import ttk
from colorama import Fore
import time

root = Tk()
root.title("Tic Tac Toe")
root.geometry('400x400')
frm = ttk.Frame(root, padding=10)
frm.grid()


currentPlayer = 'X'
global currentColor
currentColor = 'red'


xWon = False
oWon = False
#currentPlayer = "X"

board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
#boardText = "|   |   |   |\n+---+---+---+\n|   |   |   |\n+---+---+---+\n|   |   |   |"
boardText = "Current Player: X"
#scoreboard = Label(frm, text=boardText, font="monospace").grid(column=1, row=4)
#global scoreboard
scoreboard = Label(frm, text=boardText, font="monospace", )
scoreboard.grid(columnspan=2, row=4)

def btnClick(button):
    global currentPlayer
    #if currentPlayer == "O":
    #    currentPlayer = "X"
    #elif currentPlayer == "X":
    #    currentPlayer = "O"
    #print(currentPlayer)
    print("hi")
    correspondingPos = [
        (2, 0), (2, 1), (2, 2),
        (1, 0), (1, 1), (1, 2),
        (0, 0), (0, 1), (0, 2)
    ]
    pos = correspondingPos[button - 1]
    if board[pos[0]][pos[1]] == "X" or board[pos[0]][pos[1]] == "O":
        boardText = "Sorry, that space is taken. Choose again."
    else:
        board[pos[0]][pos[1]] = currentPlayer
        #print(board)
        if currentPlayer == "O":
            currentPlayer = "X"
            print("NOW X")
        elif currentPlayer == "X":
            currentPlayer = "O"
            print("NOW O")
        displayBoard()
#mode = "Classic"
#def modeSwitch():
#    if mode == "Classic":
#    btnMode.config(text=mode)
#    root.update_idletasks()
#btnMode = ttk.Button(frm, text='Mode: Classic', command=lambda: modeSwitch()).grid(column=1, row=1)

btn1 = ttk.Button(frm, text='1', command=lambda: btnClick(1)).grid(column=0, row=2)
btn2 = ttk.Button(frm, text='2', command=lambda: btnClick(2)).grid(column=1, row=2)
btn3 = ttk.Button(frm, text='3', command=lambda: btnClick(3)).grid(column=2, row=2)
btn4 = ttk.Button(frm, text='4', command=lambda: btnClick(4)).grid(column=0, row=1)
btn5 = ttk.Button(frm, text='5', command=lambda: btnClick(5)).grid(column=1, row=1)
btn6 = ttk.Button(frm, text='6', command=lambda: btnClick(6)).grid(column=2, row=1)
btn7 = ttk.Button(frm, text='7', command=lambda: btnClick(7)).grid(column=0, row=0)
btn8 = ttk.Button(frm, text='8', command=lambda: btnClick(8)).grid(column=1, row=0)
btn9 = ttk.Button(frm, text='9', command=lambda: btnClick(9)).grid(column=2, row=0)

def displayBoard():
    global currentPlayer
    print(currentPlayer)
    #try:
    #    if currentPlayer == "O":
    #        currentPlayer = "X"
    #    elif currentPlayer == "X":
    #        currentPlayer = "O"
    #except Exception as e:
    #    print(e)
    #    currentPlayer = "O"
    
    #if currentPlayer == "O":
    #    currentPlayer = "X"
    #    print("NOW X")
    #elif currentPlayer == "X":
    #    currentPlayer = "O"
    #    print("NOW O")
    boardText = "Current Player: "
    if currentPlayer == "X":
        boardText += "X\n"
    elif currentPlayer == "O":
        boardText += "O\n"
    for row in board:
        #print("| ", end="")
        boardText += "| "
        for column in row:
            if column == 0:
                #print(" ", end="")
                boardText += "  "
            elif column == "X":
                #print(Fore.RED + "X" + Fore.RESET, end="")
                boardText += "X"
            elif column == "O":
                #print(Fore.BLUE + "O" + Fore.RESET, end="")
                boardText += "O"
            #print(" | ", end="")
            boardText += " | "
        #print("\n+---+---+---+")
        boardText += "\n+---+---+---+\n"
    scoreboard.config(text=boardText)
    root.update_idletasks()
    #boardText = StringVar(value=boardText)
    print(boardText)
    #if currentPlayer == "O":
    #    currentPlayer = "X"
    #else:
    #    currentPlayer = "O"
    print("CURRENTPLAYER = ", currentPlayer)
    storedPlayer = currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    elif currentPlayer == "O":
        currentPlayer = "X"
    
    if board[0][0] == currentPlayer and board[0][1] == currentPlayer and board[0][2] == currentPlayer:
        whoWon(currentPlayer)
    elif board[1][0] == currentPlayer and board[1][1] == currentPlayer and board[1][2] == currentPlayer:
        whoWon(currentPlayer)
    elif board[2][0] == currentPlayer and board[2][1] == currentPlayer and board[2][2] == currentPlayer:
        whoWon(currentPlayer)
    elif board[0][0] == currentPlayer and board[1][0] == currentPlayer and board[2][0] == currentPlayer:
        whoWon(currentPlayer)
    elif board[0][1] == currentPlayer and board[1][1] == currentPlayer and board[2][1] == currentPlayer:
        whoWon(currentPlayer)
    elif board[0][2] == currentPlayer and board[1][2] == currentPlayer and board[2][2] == currentPlayer:
        whoWon(currentPlayer)
    elif board[0][0] == currentPlayer and board[1][1] == currentPlayer and board[2][2] == currentPlayer:
        whoWon(currentPlayer)
    elif board[0][2] == currentPlayer and board[1][1] == currentPlayer and board[2][0] == currentPlayer:
        whoWon(currentPlayer)
    #if currentPlayer == "X":
    #    currentPlayer = "O"
    #else:
    #    currentPlayer = "X"
    currentPlayer = storedPlayer


def askPos(player):
    pass
    #print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n===| Player {player}: |===")
    #print("===| Current Board: |===")
    #displayBoard()
    #pos = input('What is your move? (type "help" to show position guide) ')
    #if pos == "help":
    #    print("""---| Position Guide: |---
    #| 7 | 8 | 9 |
    #| 4 | 5 | 6 |
    #| 1 | 2 | 3 |""")
    #    pos = input('What is your move? ')
    #pos = int(pos) - 1

    #correspondingPos = [
    #    (2, 0), (2, 1), (2, 2),
    #    (1, 0), (1, 1), (1, 2),
    #    (0, 0), (0, 1), (0, 2)
    #]
    #pos = correspondingPos[pos]
    '''
    while board[pos[0]][pos[1]] == "X" or board[pos[0]][pos[1]] == "O":
        print(Fore.RED + "Sorry, that place not available." + Fore.RESET)
        pos = input('What is your move? (type "help" to show position guide) ')
        if pos == "help":
            print("""---| Position Guide: |---
    | 7 | 8 | 9 |
    | 4 | 5 | 6 |
    | 1 | 2 | 3 |""")
            pos = input('What is your move? ')
        pos = int(pos) - 1

        correspondingPos = [
            (2, 0), (2, 1), (2, 2),
            (1, 0), (1, 1), (1, 2),
            (0, 0), (0, 1), (0, 2)
        ]
        pos = correspondingPos[pos]
    board[pos[0]][pos[1]] = player'''

def whoWon(player):
    global boardText
    if player == "X":
        xWon = True
        print(Fore.GREEN + "\n\nCongratulations! X Won!!!" + Fore.RESET)
        boardText = "X Won!!!"
    else:
        oWon = True
        print(Fore.GREEN + "\n\nCongratulations! O Won!!!" + Fore.RESET)
        boardText = "O Won!!!"
    scoreboard.config(text=boardText)
    root.update_idletasks()
    time.sleep(10)
    exit()

while xWon != True and oWon != True:
    root.mainloop()



#root.mainloop()



#btn0 = ttk.Button(frm, text='', color='white', command=)
#btn1 = Button(frm, text=' ', bg='white').grid(column=0, row=0)
#btn1['command'] = lambda: btn1.config(bg='green')
#btn1['command'] = btn1['bg'] = 'green'

