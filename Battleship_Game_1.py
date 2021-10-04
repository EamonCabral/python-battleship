# Author: EamonCabral
# This code runs a simple/goofy game of battleship.
# There is a hidden passcode you can use when you are asked for your name
# Using 'Speedup' instead of your name will skip the rules and run the code faster

import sys,time,random

typing_speed = 0.9#wpm

def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*1/typing_speed)
    print('')

from random import randint

print("\nWelcome to Eamon's Battleship game!\n")
print("First off, I'd like to introduce myself.\n")
print("My name is: ")

slow_type(".")
slow_type(".")
slow_type(".")
slow_type(".")

print("\nEamon\n")

slow_type("..")

print("\nOf course\n")

slow_type("...\n")

name = input("What is your name? ")

if name.lower() == "speedup":
    print("Alright Eamon, let's speed this game up!!!")
    name = "Captain SNOT!"
    input("From now on, your name is Captain SNOT!, and we will skip the rules! - Press [Enter/Return]")
    typing_speed = 1000
else:
    typing_speed = 0.9  # wpm

if name.lower() != 'captain snot!':
    print("\nHi " + str(name) + ", let's begin playing Battleship!");
    slow_type("...\n")
    print("\nFirst off, " + str(name)+", let's see what our board looks like, shall we?");

if name.lower() == 'captain snot!':
    yesorno = 'y'
else:
    yesorno = input("\nType in YES to continue, NO if you're already bored: ")

if yesorno.lower() == 'y' or yesorno.lower() == 'yes' or yesorno.lower() == '':
    print("\nAlright, check it out!\n")

elif yesorno.lower() == 'n' or yesorno.lower() == 'no':
    slow_type("\n...\n")
    print("\nAlright, come back later... \n")
    exit()

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

if name.lower() != 'captain snot!':
    print(input("\nPretty cool, eh? "))

print("\nCool, so here are the rules:\n")

print("\n\nEamon will randomly select a ship location based on two coordinates (Row and Column)")

slow_type(".")
slow_type(".")
slow_type(".")
slow_type(".\n")

print("He will, of course, not tell you where his ship is hidden... because he has no idea where the ship is")

slow_type(".")
slow_type(".")
slow_type(".")
slow_type(".\n")

print("The range of values you will use for your Rows and Columns should be from {1} to {5}")

slow_type(".")
slow_type(".")
slow_type(".")
slow_type(".\n")

print("You get four {4} guesses, if you find it in one of those four guesses, you win!")

slow_type(".")
slow_type(".")
slow_type(".\n")
slow_type("If not:\n")

print("U SUCK!")

slow_type(".")
slow_type(".")
slow_type(".")
slow_type(".")
slow_type(".\n")

print("LAUGHING!!")
slow_type(".")
slow_type(".")
slow_type(".\n")

print("\n\n\nAlright, are you ready!? ")
print("(Feel free to scroll up and revise the rules...)\n\n\n")

if name.lower() != 'captain snot!':
    print(input("Type in: 'I like boogers!' when you're ready: "))
    print("\nYou didn't actually have to type in 'I like boogers!' That's just for fun, LOL")
    slow_type('.....')
    print('\nAlright, seriously')
    slow_type('...')

print("\n\nReady!?\n")
print("Press [Enter/Return] to play, type in 'boogers!' to quit :)\n")

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

condition = input('')

while condition.lower() != 'boogers!' and condition.lower() != 'q' and condition.lower() != 'boogers':

    for turn in range(4):

        print("\n\nTurn",turn+1)

        guess_row = input("Guess Row: ")
        guess_col = input("Guess Col: ")
        accepted_inputs = str(list(range(100001)))

        if guess_row.lower() == "abort game" or guess_col.lower() == "abort game":
            typing_speed = 0.9
            print("\nPasscode accepted, aborting code in:\n")
            slow_type("\n5\n4\n3\n2\n1...")
            print("\nCode finalized")
            exit()

        while guess_row == '' or guess_col == '':
            if guess_row.lower() == "abort game" or guess_col.lower() == "abort game":
                typing_speed = 0.9
                print("\nPasscode accepted, aborting code in:\n")
                slow_type("\n5\n4\n3\n2\n1...")
                print("\nCode finalized")
                exit()
            else:
                print("\nOops, one of your inputs was empty, could you please try again?\n" + \
                      "\nBe sure not to use any letters!\n")
                guess_row = input("Guess Row: ")
                guess_col = input("Guess Col: ")

        while guess_col not in accepted_inputs or guess_row not in accepted_inputs:
            if guess_row.lower() == "abort game" or guess_col.lower() == "abort game":
                typing_speed = 0.9
                print("\nPasscode accepted, aborting code in:\n")
                slow_type("\n5\n4\n3\n2\n1...")
                print("\nCode finalized")
                exit()
            else:
                print("\nWOW! You typed in a letter... you almost broke down my game!\n" + \
                      "\nTry that again, but now with numbers from 1 to 5\n")
                guess_row = input("Guess Row: ")
                guess_col = input("Guess Col: ")

        guess_row = int(guess_row) - 1
        guess_col = int(guess_col) - 1

        if guess_row == ship_row and guess_col == ship_col:
            board[ship_row][ship_col] = "X"
            print("\n\nCONGRATULATIONS!!!! You sank my battleship!\n")
            print_board(board)
            print("\nPlay again? Press [Enter/Return] to play, Type 'boogers!' or 'q' to quit ")
            ship_row = random_row(board)
            ship_col = random_col(board)
            board = []
            for x in range(0, 5):
                board.append(["O"] * 5)
            condition = input('')
            turn = 1
            if condition.lower() == 'boogers!' and condition.lower() == 'q':
                print('\n\nOkay, go!\n')
            else:
                break
        else:
            if guess_row not in range(5) or guess_col not in range(5):
             print("\nOops, that's not even in the ocean.")

            elif (board[guess_row][guess_col] == '*'):
                print("You guessed that one already.\n")
                print_board(board)

            else:
             print("You missed my battleship!\n")
             board[guess_row][guess_col] = "*"

             print_board(board)

            if turn == 3:
                print("\n\nBoo hoo... you lost :-( !")
                print("Press Enter/Return if you want to play again, type in boogers! if you would like to quit")
                condition = input('')
else:
    print('\n\n\nOkay, see you later!\n\n')




