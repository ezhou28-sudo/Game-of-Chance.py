"""This Python program is a fun, interactive game of chance that challenges the player to 
test their luck in three different mini-games: 
1.Dice Roll : The computer randomly rolls a six-sided die. The player guesses a number 
between 1 and 6.
2.Coin Flip : The program simulates flipping a coin. The player guesses whether it
 will land on Heads (H) or Tails (T).
3.Color Spinner : The computer spins a four-color spinner (red, green, blue, or yellow).
 The player guesses which color it will land on.
 
 After all three guesses, the program reveals the actual results of each game and tells 
 the player how many they guessed correctly, from “all right” to “all wrong.”
 
 This project uses Pythons random module to generate random outcomes, conditional 
 statements (if, elif, else) to compare guesses, and simple input/output functions to 
 interact with the player.
"""
#Starting with Welcomes and introduce my game/program to users.
print("*****WELCOME*****")
print("This is our game of chance. ")
print("Let's see if you won...")
#The fisrt part of the game. Dice Roll. Set up the random number values and ask user to give an input.
import random 
dice_roll= random.randint(1,6)
user_dice=int(input("What is your guess on the dice roll?(1-6)"))
#The second part of the game. Coin flip. Set up the random number values and ask user to pick side. 
#Set up number values for user's guess on heads and tails
coin_flip= random.randint(1,2)
user_coin=input("What is your guess on the coin flip, Heads (H) or Tails (T)?")
if user_coin==str("H"):
    coin_value=1
if user_coin==str("T"):
    coin_value=2
#else:
   #print("Please enter H or T for coin flip game")
   #coin_value=print(str(input("What is your guess on the coin flip, Heads (H) or Tails (T)?")))
#The third part of the game. Spinner. Set up the random number values and ask user for input
#Set up a number value for user's guess on each color
spin_spinner= random.randint(1,4)

user_spin=input("What is your guess on the spinner, red (r), green (g), blue (b), or yellow (y)?")
if user_spin==str("r"):
    spin_color=1
if user_spin==str("g"):
    spin_color=2
if user_spin==str("b"):
    spin_color=3
if user_spin==str("y"):
    spin_color=4
#else:
    #print("Please enter the color that is exist in the options,red (r), green (g), blue (b), or yellow (y)")
    #4user_spin=print(str(input("What is your guess on the spinner, red (r), green (g), blue (b), or yellow (y)?")))

print("You rolled a "+ str(dice_roll))
#Transfer number values to texts
if coin_flip==1:
    coin_flip=str("Heads")
else :
    coin_flip=str("Tails")
if spin_spinner==1:
    spin_spinner=str("red")
if spin_spinner==2:
    spin_spinner=str("green")
if spin_spinner==3:
    spin_spinner=str("blue")
if spin_spinner==4:
    spin_spinner=str("yellow")

print("You flipped "+ str(coin_flip))
print("You spun "+str(spin_spinner))
#Transfer the texts back to number values
if coin_flip==str("Heads"):
    coin_flip=1
if coin_flip==str("Tails"):
    coin_flip=2
if spin_spinner==str("red"):
    spin_spinner=1
if spin_spinner==str("green"):
    spin_spinner=2
if spin_spinner==str("blue"):
    spin_spinner=3
if spin_spinner==str("yellow"):
    spin_spinner=4
#Printoff user's score
if dice_roll==user_dice and coin_flip==coin_value and spin_spinner==spin_color:
    print("You've got the all right!!!")
elif dice_roll!=user_dice and coin_flip!=coin_value and spin_spinner!=spin_color:
    print("You've  got them all wrong!!!")
elif dice_roll==user_dice and coin_flip==coin_value and spin_spinner!=spin_color:
    print("That was close, you only got the spinner wrong")
elif dice_roll!=user_dice and coin_flip==coin_value and spin_spinner==spin_color:
    print("That was close, you only got the dice roll wrong")
elif dice_roll==user_dice and coin_flip!=coin_value and spin_spinner==spin_color:
    print("That was close, you only got the coin flip wrong")
elif dice_roll==user_dice:
    print("You only got the dice roll right")
elif coin_flip==coin_value:
    print("You only got the coin flip right")
elif spin_spinner==spin_color:
    print("You only got the spinner right")