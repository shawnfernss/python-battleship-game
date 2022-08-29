from msvcrt import getch
from random import randint
import os
import time


# Board for holding ship locations
HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
# Board for displaying hits and misses
GUESS_BOARD = [[" "] * 8 for i in range(8)]


def print_board(board):
    print(" A B C D E F G H")
    print(" +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

# computer create 5 ships


def create_ships(board):
    for ship in range(12):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = "X"

# get locations from user for ships


def get_ship_location():
    row = input("Enter the row of the ship: ").upper()
    while row == "":
        print('!!! Not an appropriate choice, please select a valid row !!!')
        row = input("Enter the row of the ship: ").upper()
    while row not in "12345678":
        print('!!! Not an appropriate choice, please select a valid row !!!')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column == "":
        print('!!! Not an appropriate choice, please select a valid column !!!')
        column = input("Enter the column of the ship: ").upper()

    while column not in "ABCDEFGH":
        print('!!! Not an appropriate choice, please select a valid column !!!')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]

# check if all ships are hit


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

# clear the hidden and guess board


def clear_board(board):
    board.clear()


if __name__ == "__main__":
    answer = 'y'
    while answer == 'y' or answer == 'Y':
        create_ships(HIDDEN_BOARD)
        turns = 20
        while turns > 0:
            print('Guess a battleship location')
            print()
            print_board(GUESS_BOARD)
            row, column = get_ship_location()
            if GUESS_BOARD[row][column] == "-":
                print("You guessed that one already.")

            elif HIDDEN_BOARD[row][column] == "X":
                print("Hit")
                time.sleep(1)
                os.system("cls")
                GUESS_BOARD[row][column] = "X"
                turns -= 1

            else:
                print("MISS!")
                time.sleep(1)
                os.system("cls")
                GUESS_BOARD[row][column] = "-"
                turns -= 1

            if count_hit_ships(GUESS_BOARD) == 5:
                print("You win!")
                break
            print("You have " + str(turns) + " turns left")
            if turns == 0:
                print("You ran out of turns")
                print("Hit enter to see the location of battleships")
                getch()
                os.system("cls")
                print(
                    '------------ Here is the true location of Battleships-------------')
                print_board(HIDDEN_BOARD)

        answer = input("Do you want to Play Again? Yes(y) or No(n)? : ")
        if answer == 'y' or answer == 'Y':
            HIDDEN_BOARD.clear()
            GUESS_BOARD.clear()
            HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
            GUESS_BOARD = [[" "] * 8 for i in range(8)]
        else:
            exit()
