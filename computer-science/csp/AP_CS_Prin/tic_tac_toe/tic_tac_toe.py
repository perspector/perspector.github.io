from colorama import Fore

xWon = False
oWon = False
currentPlayer = "X"

board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]


def displayBoard():
    for row in board:
        print("| ", end="")
        for column in row:
            if column == 0:
                print(" ", end="")
            elif column == "X":
                print(Fore.RED + "X" + Fore.RESET, end="")
            elif column == "O":
                print(Fore.BLUE + "O" + Fore.RESET, end="")
            print(" | ", end="")
        print("\n+---+---+---+")


def askPos(player):
    print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n===| Player {player}: |===")
    print("===| Current Board: |===")
    displayBoard()
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
    board[pos[0]][pos[1]] = player

def whoWon(player):
    if player == "X":
        xWon = True
        print(Fore.GREEN + "\n\nCongratulations! X Won!!!" + Fore.RESET)
        exit()
    else:
        oWon = True
        print(Fore.GREEN + "\n\nCongratulations! O Won!!!" + Fore.RESET)
        exit()

while xWon != True and oWon != True:
    #xMove = int(input("What space would you like?"))
    askPos(currentPlayer)
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
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
