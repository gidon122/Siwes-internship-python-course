# PIZZA DELIVERY APP

# print("Welcome to our Pizza Delivery App")
# size = input("What size do you want? (S, M, or L): ").upper()
# pepperoni = input("Do you want Pepperoni? Y or N: ").upper()
# extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
# if size == "S":
#     bill = 10
# elif size == "M":
#     bill = 15
# elif size == "L":
#     bill = 20
# else:

#     print("Invalid size entered!")
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     elif size == "M" or size == "L":
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your total bill is ${bill}")






# # # TEASURE ISLAND GAME

# print("Welcome to Treasure Island.")
# print("Your mission is to find the Treasure.\n")
# direction = input("You are at the crossroad, where do you want to go? Type 'left' or 'right': ").lower()
# if direction == "left":
#     lake = input("You got to a lake. Type 'wait' for a boat or 'swim' to cross: ").lower()
#     if lake == "wait":
#         door = input("There is a house with three doors. One red, one yellow, one black. Which do you choose?: ").lower()
#         if door == "red":
#             print("It's a room full of fire. Game Over.")
#         elif door == "yellow":
#             print("You Win! You found the treasure!")
#         elif door == "black":
#             print("It's a room full of snow, you'll freeze. Game Over.")
#         else:
#             print("Invalid door choice. Game Over.")
#     elif lake == "swim":
#         print("You got attacked by an angry trout. Game Over.")
#     else:
#         print("Invalid choice. Game Over.")

# elif direction == "right":
#     print("You fell into a hole. Game Over.")
# else:
#     print("Invalid direction. Game Over.")








# import random

# secret_number = random.randint(0, 9)
# attempts = 0
# max_attempts = 3

# print("Welcome to the Guessing Game!")
# print("I have a secret number between 0 and 9.")
# print(f"You have {max_attempts} attempts to guess it.")

# while attempts < max_attempts:
#     guess = int(input(f"Guess {attempts + 1}/{max_attempts} - Enter your guess: "))

#     if guess == secret_number:
#         print(f" Correct! The secret number was {secret_number}. You Win!")
#         break
#     else:
#         attempts += 1
#         if attempts < max_attempts:
#             print(f" Wrong! You have {max_attempts - attempts} attempt(s) left.")
#         else:
#             print(f" Game Over! The secret number was {secret_number}.")




print ("WELCOME TO THE TREASURE ISLAND ")
print ("YOUR MISSION IS TO FIND THE TREASURE")

direction = input("YOU ARE AT A CROSSROAD, WHERE DO YOU WANT TO GO? L OR R")

if direction == "left":
    lake = input("You are at the middle of a lake type wait to wait for a boat type swim to swim across")
    if lake == "wait":
        island = input("You've arrived at the island unharmed. There is a housee with three doors. red, yellow and black: choose one?")
        if island == "red":
            print ("it is a room full of fire. Game over")
        elif island == "yellow":
            print ("it is a room full of snow, you will freeze. Game over")
        elif island == "black":
            print ("it is a room filled with treasures. You win. Game over")
        else:
            print ("invalid input game over")
    elif lake == "swim":
        print ("Shack don catch you")
    else:
        print ("invalid input game over")

elif direction == "right":
    print ("Game over")

else:
    print ("invalid input game over")