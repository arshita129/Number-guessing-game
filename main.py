import random
import sys


def clue1(num):
    l = []
    for i in range(2, num):
        if num % i == 0:
            l.append(i)
    for i in l:
        print("The number is a multiple of: ", i, ",", end=" ")


def clue2(num):
    a = random.randint(2, 5)
    print("The number lies between ", a + num, " and ", num-a)


def clue3(num):
    if num % 2 == 0:
        print("The number is an even number")
    else:
        print("The number is an odd number")


print("Hello! Welcome to the Number Guessing Game")
print("*" * 50)
print("Rules:")
print("* You will enter the upper bound")
print("* You will be given three clues and u have to guess the number according to them!!!")
print("* If u guess the number within three chanced then u win otherwise u loose")
print("Lets Start! All the Best!")
print()
n = int(input("Enter the upper bound"))
number = random.randint(0, n)
print()
print("Your first clue is: ")
clue1(number)
print()
guess = int(input("Your guess? "))
if guess == number:
    print()
    print("You guessed the number in first attempt!")
    print("*" * 50)
    print("YOU WON!")
    print("*" * 50)
    print("See you next time")
    print("Bye!")
    sys.exit(0)
if abs(number - guess) < 5:
    print()
    print("You are close!!")
    print()
print("Try Again!")
print()
print("Your second clue is: ")
clue2(number)
print()
guess = int(input("Your guess? "))
if guess == number:
    print()
    print("You guessed the number in second attempt!")
    print("*" * 50)
    print("YOU WON!")
    print("*" * 50)
    print("See you next time")
    print("Bye!")
    sys.exit(0)
if abs(number - guess) < 5:
    print()
    print("You are close!!")
print()
print("Try Again!")
print("This is your last chance!")
print()
print("Your last clue is: ")
clue3(number)
print()
guess = int(input("Your guess? "))
if guess == number:
    print()
    print("You guessed the number in last attempt!")
    print("*" * 50)
    print("YOU WON!")
    print("*" * 50)
    print("See you next time")
    print("Bye!")
    sys.exit(0)
print()
print("Sorry you lost the game")
print("the number was ", number)
print("Better luck next time")
print("Bye!")
