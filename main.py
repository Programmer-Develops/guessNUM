import random

print("Number Guessing Game")
print("Guess Number Between 1 and 9 :-")

chances = int(input("Enter your guess ="))
number = 5

if chances == number :
    print("Correct")
else:
    print("wrong")