# Creating a Die roller
# https://www.reddit.com/r/dailyprogrammer/comments/8s0cy1/20180618_challenge_364_easy_create_a_dice_roller/


import random
import sys
import re



def main():

# Input of die 
# Format is e.g. 3d5, meaning 3 dies of 5 sides are rolles
# The number of dice to roll can be an integer between 1-100, inclusive
# The number of sides can be from 2-100 inclusive

    regex = r"\b([1-9]|[1-9][0-9]|100)[d]([2-9]|[1-9][0-9]|100)\b"
    
    
    while True:
        print("Input new roll")
        try:
            # Match input string to regex
            match = re.search(regex, input("")).string
        except AttributeError:
            print("Not correct formatting like (2d50)")
            continue
    
        # Split matched string to get number of dices and sides input
        dices, sides = match.split("d")
        
        # Change type to int
        dices = int(dices)
        sides = int(sides)

        # Keep track of sum of dice rolls
        sum = 0

        # Roll number of dices
        for i in range(dices):
            roll = roll_dice(sides)
            sum += roll
            print(roll, end="... ")
        
        # Print final sum
        print(f"Sum:", sum)
        print()

def roll_dice(sides):
    # return random int based on the number of sides of dice
    roll = random.randint(2, sides)

    return roll


if __name__ == "__main__":
    main()