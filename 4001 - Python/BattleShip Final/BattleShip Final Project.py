#Kent Studer - 12544417, Information Technology 4001 Final Project FS 20'
#Battleship Game

#The objective of this program is to play the classic game of Battleship!
#The user will have 10 turns to successfully locate and find the computers
#battleship

from random import randint

#INPUT: Rows and Columns
#OUTPUT: 2D Board 
def createBoard(rows, columns):
    board = []
    for row in range(rows):
        row = []
        for col in range(columns):
            row.append(' ')
        board.append(row)
        
    return board

#INPUT: Board and Columns
#OUTPUT: A printed board with column and row labels
def printBoard(board, columns):
    CNames = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:columns]
    print('   | '+' | '.join(CNames)+ ' | ')
    for number, row in enumerate(board):
        print(number, ' | '+' | '.join(row)+' | ')

#INPUT: Board
#OUTPUT: A random row for the computer
def RandomRow(board):
    return randint(0, len(board)-1)

#INPUT: Board
#OUTPUT: A random column for the computer
def RandomCol(board):
    return randint(0, len(board[0])-1)

def main():

    play_game = True
    while(play_game):
        print("Welcome to BattleShip!")
        print("You will have 10 tries to sink the computers ship\nSo lets get firing!")

        Columns = 9
        Rows = 9
        Board = createBoard(Rows, Columns)
        printBoard(Board, Columns)

        ShipRow = RandomRow(Board)
        ShipCol = RandomCol(Board)

        print(ShipRow)
        print(ShipCol)

        for turn in range(10):
            print("Turn", turn + 1)
            while(True):
                try:
                    RowGuess = int(input("Guess Row: "))
                    if(RowGuess < 0):
                        print("Please input a valid row number")
                        continue
                except ValueError:
                    print("Please enter only a number")
                else:
                    break

            while(True):
                try:
                    ColGuess = int(input("Guess Col: "))
                    if(ColGuess < 0):
                        print("Please input a valid row number")
                        continue
                except ValueError:
                    print("Please enter only a number")
                else:
                    break

            if(RowGuess == ShipRow and ColGuess == ShipCol):
                print("You sank my battleship!")
                break
            else:
                if(RowGuess not in range(Rows) or ColGuess not in range(Columns)):
                    print("Your guess was out of the Game Board!")
                elif Board[RowGuess][ColGuess] == "X":
                    print("You already guessed that spot!")
                else:
                    print("You missed!")
                    Board[RowGuess][ColGuess] = "X"
                if turn == 10:
                    print("Game over")
                printBoard(Board, Columns)
        another = input("Would you like to play again? (y/n) ")
        if(another != 'y'):
            play_game = False
main()

        
