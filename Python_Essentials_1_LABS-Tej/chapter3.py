# Author: Sgt Tej Kumar Rai
# Date Modified: 22/09/2021
# Description: This source file contains all the labs from Chapter 3 of Pthon Essentils 1 module.

# ******************************************************************* Start: Chapter 3 ******************************************************************* #
# The topics covered within this chapter are Boolean Values, Conditional Execution, Loops, Lists and List Processing, Logical and Bitwise Operations

# 3.1.1.4 LAB: Questions and answers *********** (Snippet 1) ***********
# Start: This snippet uses a comparions operator to ouput False if n < 100 or True otherwise
n = int(input("Enter an integer:")) # Asks for an integer input
print(n >= 100) # Prints False if n < 100 or True otherwise
print() # Print a new line
# End

# 3.1.1.10 LAB: Comparison operators and conditional execution *********** (Snippet 2) ***********
# Start: This snippet asks a user for the name of a houseplant and then generates output to the screen depending on the input.
plant_name = input("Enter the name of an indoor houseplant:")
if plant_name == "Spathiphyllum": print ("Yes - Spathiphyllum is the best plant ever!")
elif plant_name == "spathiphyllum": print ("No, I want a big Spathiphyllum!")
else: print("Spathiphyllum! Not [" + plant_name + "]!")
print() # Print a new line
# End

# 3.1.1.11 LAB: Essentials of the if-else statement *********** (Snippet 3) ***********
# Start: This snippet calculates the Personal Income Tax (PIT) which had to be paid once a year by the inhabitant of a land of milk and honey
income = float(input("Enter the annual income: "))

if income <= 85_528: tax = (income * 0.18) - 556.02
else: tax = 14_839.02 + (income - 85_528) * 0.32

if tax < 0: tax = 0.0 # If the calculated tax is less tahn zero, it only means no tax at all

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
print() # Print a new line
# End

# 3.1.1.12 LAB: Essentials of the if-elif-else statement *********** (Snippet 4) ***********
# Start: This snippet checks if the given year is a leap year or not
year = int(input("Enter a year: "))

# Checks if the entered year falls into the Gregorian era
if year < 1582: print ("Not within the Gregorian calendar period.") # The Gregorian calendar started from 1582
else: 
    # Checks if the entered year is a leap year or not
    if year % 4 != 0: print ("Common year")
    elif year % 100 != 0: print ("Leap year")
    elif year % 400 != 0: print ("Common year")
    else: print ("Leap year")
print() # Print a new line
# End
print("Test")

# 3.2.1.3 LAB: Essentials of the while loop *********** (Snippet 5) ***********
# Start: This snippet uses while loop to allow a user to guess the magician's secret number.
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int(input("Enter a number:")) # Asks the user to enter an integer number

while number != secret_number: # Check whether the number entered by the user is the same as the number pioked by the magicial.
    print("Ha ha! You're stuck in my loop!") # If the number choosedn by the user is different than the magaician's secret number, the user sees this message.
    number = int(input("Enter a number:")) # Also the user will be promted to enter a number again.

print("Well done, mubble! You are free now.") # If the number entered by the user matches the number picked by the magician, the user sees this message.
print() # Print a new line
# End:

# 3.2.1.6 LAB: Essentials of the for loop *********** (Snippet 6) ***********
# Start: This snippet uses the for loop to print five outputs, with each iteration representing 1 second. Finally, it prints the final message.
import time # imports the time module

for count in range(1,6): # Assigns the control variable 'count' a number from 1 to 5 in turn
    print(count, "Mississippi") # Prints the loop iteration number and the word "Mississippi"
    time.sleep(1) # Use time.sleep() method to pause for 1 second

print("Ready or not, here I come!") # prints the final message.
# End

# 3.2.1.9 LAB: The break statement - Stuck in a loop *********** (Snippet 7) ***********
# Start: This snippet uses while loop and break keyword to loop and continuously asks a user to enter a word unless the user neters "chupacabra".
correct_word = "chupacabra" # Word needed to exit the loop below.
user_word = "" # initialise user-word variable with an empty string

while True: # Loop indefinitely
    if correct_word == user_word: # If the word entered by the user matches the correct word break out of the loop
        break
    else:
        user_word = input("Enter a word:") # Asks the user to enter a word
print("You've successfully left the loop.") # prints this message when the user successfuly exits the loop
# End

# 3.2.1.10 LAB: The continue statement - the Ugly Vowel Eater *********** (Snippet 8) ***********
# Start: This snippet uses for loop and continue keyword to remove vowel from the word enterd by a user.
user_word = input("Enter a word:") # Prompt the user to enter a word and assigns it to the user_word variable.
user_word = user_word.upper() # Use the string method upper() to convert the word entered by the user to upper case.
for letter in user_word:
    # if the letter is "A", "E", "I", "O" or "U" skip the loop else print the letter to the terminal
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)
# End

# 3.2.1.11 LAB: The continue statement - the pretty Vowel Eater *********** (Snippet 9) ***********
# Start: This snippet improves the last snippet by concatenating non-vowel letters into a long string during subsequent loop turns.
word_without_vowels = "" # Initialise the word_without_vowels variable with an empty string.

user_word = input("Enter a word:") # Prompt the user to enter a word and assigns it to the user_word variable.
user_word = user_word.upper() # Use the string method upper() to convert the word entered by the user to upper case.
for letter in user_word:
    # if the letter is "A", "E", "I", "O" or "U" skip the loop else print the letter to the terminal.
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter # Use concatenation operation to combine selected letters into a long string during subsequent loop turns.

print(word_without_vowels) # Print the word assigned to word_without_vowels.
# End

# 3.2.1.14 LAB: Essentials of the while loop *********** (Snippet 10) ***********
# Start: This snippet uses while loop to calculate the height of the pyramid that can be built using the given number of blocks 
# using one principle: each lower layer contains one block more than the layer above.
blocks = int(input("Enter the number of blocks: ")) # Ask for the number of blocks the builders have
height = 0 # Initialise height variable to 0

while blocks > 0: # Loop until blocks = 0
    # Execute the if block iteratively if the condition is met otherwise break out of the loop.
    if blocks >= (height + 1):
        blocks = blocks - (height + 1)
        height += 1
    else:
        break
print("The height of the pyramid:", height) # Print the height of the pyramid that can be built using the given number of blocks.
# End

# 3.2.1.15 LAB: Collatz's hypothesis *********** (Snippet 11) ***********
# Start: This snippet tests Collatz's hypothesis using the while loop.
number = int(input("Enter a non-negative and non-zero integer number:")) # Ask for a natural number
steps = 0 # Initialise steps variable to 0.
if number > 0: 
    c0 = number # Take any non-negative and non-zero integer number and name it c0.
    while c0 != 1: # Loop until c0 is not equal to 1
        if c0 % 2 == 0: # If it's even evaluate a new c0 as the following.
            c0 /= 2
        else: # Otherwise, if it's odd, evaluate a new c0 as the following.
            c0 = 3 * c0 + 1
        
        steps += 1 # Increment steps variable by 1 evertime the loop is completed successfully.
        print(int(c0)) # Print all the intermediate values of c0
    print("steps =", steps) # Print the steps needed to reach the initial value of c0 to 1 using the algorithm.
# End
# ******************************************************************* End: Chapter 3 ******************************************************************* #