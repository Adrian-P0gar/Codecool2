import os
import random
import pyfiglet
import sys

credits = ["Alexandru Oriean", "Adi Pogar"]
board = [[3 * j + i + 1 for i in range(3)]
         for j in range(3)]  # create the empty board
char = "="


def banner(char):
    text = pyfiglet.figlet_format("Tic-Tac-Toe")
    print(char * 50, char * 50, sep='\n')
    print(text)


def winCond(board):
    return (board[0][0] == board[0][1] == board[0][2]) or (board[1][0] == board[1][1] == board[1][2]) or (board[2][0] == board[2][1] == board[2][2]) or (board[0][0] == board[1][0] == board[2][0]) or (board[0][1] == board[1][1] == board[2][1]) or (board[0][2] == board[1][2] == board[2][2]) or (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0])


def displayBoard(board):
    os.system('clear')
    for row in range(3):
        print('+–––––––' * 3, '+', sep='')
        print('|       ' * 3, '|', sep='')
        for col in range(3):
            print('|   ' + '{}'.format(board[row][col]) + '   ', end='')
        print('|')
        print('|       ' * 3, '|', sep='')
    print('+–––––––' * 3, '+', sep='')


def menu():
    # menu
    banner(char)
    print(' Credits: {0}, {1} '.format(
        credits[0], credits[1]).upper().center(50, '='))
    print('=' * 50)
    print('Press 1 for Singleplayer'.center(50, ' '))
    print('Press 2 for Multiplayer'.center(50, ' '))
    print('Press 0 to Exit'.center(50, ' '))
    playMode = input('Your option: ')

    while playMode not in ["1", '2', '0']:
        playMode = input('Please enter a valid option (0, 1 or 2): ')

    if playMode == '1' or playMode == '0':
        sys.exit()
    if playMode == '2':
        displayBoard(board)


def x_move():
    global i, d
    x = input('x Choose your position: ')

    try:
        position = int(x)
        if board[int((position-1) / 3)][int(position % 3 - 1)] == position:
            board[int((position - 1) / 3)][int(position % 3 - 1)] = 'X'
            i = 1
            d += 1
            displayBoard(board)
    except (ValueError, IndexError):
        print("")


def zero_move():
    global i, d
    O = input('0 Choose your position: ')
    try:
        position = int(O)
        if board[int((position-1) / 3)][int((position-1) % 3)] == position:
            board[int((position-1) / 3)][int((position-1) % 3)] = '0'
            i = 0
            d += 1
            displayBoard(board)
    except (ValueError, IndexError):
        print("")


def main():
    global i, d
    i = 0
    d = 0
    banner(char)
    winCond(board)
    displayBoard(board)
    menu()
    while d < 9:
        if x_move() == 1:
            menu()
            zero_move()
        if winCond(board) is True:
            print("x")
            break
        if d == 9:
            print("It't a tie")
            break
        if zero_move() == 0:
            x_move()
        if winCond(board) is True:
            print("0")
            break


main()
