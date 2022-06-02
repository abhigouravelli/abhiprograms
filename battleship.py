from random import randint

size = 5
turns = 10
board = []

for row in range(size):
    board.append(["0"] * size)

def print_board(board):
    for row in board:
        print(" ".join(row))

ship_row = randint(0, len(board) - 1)
ship_col = randint(0, len(board[0]) - 1)

for turn in range(turns):
    print("Turn", turn + 1)
    print_board(board)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))
    if guess_row == ship_row and guess_col == ship_col:
        print("Congrtulations! You sank my battleship! ")
        break
    elif guess_row < 0 or guess_row > size - 1 or guess_col < 0 or guess_col > size - 1:
        print("That is not even in the ocean")
    elif board[guess_row][guess_col] == "X":
        print("You already guessed that one")
    else:
        print("You missed my battleship")
        board[guess_row][guess_col] == "X"
else:
    print("Sorry -- You lose...")
    board[ship_row][ship_col] = "S"
    print_board(board)
     
