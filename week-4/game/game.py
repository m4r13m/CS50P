from random import randint
import sys

def main():

    level = get_level()
    x = randint(1, level)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                continue
            elif guess < x:
                print("Too small!")
            elif guess > x:
                print("Too large!")
            else:
                sys.exit("Just right!")
        except ValueError:
            pass

def get_level():
    while True:
        try:
            l = int(input("Level: "))
            if l <= 0:
                continue
            return l
        except ValueError:
            pass

main()
