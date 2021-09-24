# Author: Sgt Tej Kumar Rai
# Date Created: 22/09/2021
# Date Last Modified: 24/09/2021
# Description: This source file contains all the labs from Chapter 3 of Pthon Essentils 1 module.
# # The topics covered within this chapter are Boolean Values, Conditional Execution, Loops, Lists and List Processing, Logical and Bitwise Operations

# 3.1.1.4 LAB: Questions and answers *********** (LAB  1) ***********
# Description: This LAB  uses a comparions operator to ouput False if n < 100 or True otherwise
n = int(input("Enter an integer:")) # Asks for an integer input
print(n >= 100) # Prints False if n < 100 or True otherwise
print() # Print a new line


# 3.1.1.10 LAB: Comparison operators and conditional execution *********** (LAB  2) ***********
# Description: This LAB  asks a user for the name of a houseplant and then generates output to the screen depending on the input.
plant_name = input("Enter the name of an indoor houseplant:")
if plant_name == "Spathiphyllum": print ("Yes - Spathiphyllum is the best plant ever!")
elif plant_name == "spathiphyllum": print ("No, I want a big Spathiphyllum!")
else: print("Spathiphyllum! Not [" + plant_name + "]!")
print() # Print a new line


# 3.1.1.11 LAB: Essentials of the if-else statement *********** (LAB  3) ***********
# Description: This LAB  calculates the Personal Income Tax (PIT) which had to be paid once a year by the inhabitant of a land of milk and honey
income = float(input("Enter the annual income: "))

if income <= 85_528: tax = (income * 0.18) - 556.02
else: tax = 14_839.02 + (income - 85_528) * 0.32

if tax < 0: tax = 0.0 # If the calculated tax is less tahn zero, it only means no tax at all

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
print() # Print a new line


# 3.1.1.12 LAB: Essentials of the if-elif-else statement *********** (LAB  4) ***********
# Description: This LAB  checks if the given year is a leap year or not
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

print("Test")

# 3.2.1.3 LAB: Essentials of the while loop *********** (LAB  5) ***********
# Description: This LAB  uses while loop to allow a user to guess the magician's secret number.
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


# 3.2.1.6 LAB: Essentials of the for loop *********** (LAB  6) ***********
# Description: This LAB  uses the for loop to print five outputs, with each iteration representing 1 second. Finally, it prints the final message.
import time # imports the time module

for count in range(1,6): # Assigns the control variable 'count' a number from 1 to 5 in turn
    print(count, "Mississippi") # Prints the loop iteration number and the word "Mississippi"
    time.sleep(1) # Use time.sleep() method to pause for 1 second

print("Ready or not, here I come!") # prints the final message.


# 3.2.1.9 LAB: The break statement - Stuck in a loop *********** (LAB  7) ***********
# Description: This LAB  uses while loop and break keyword to loop and continuously asks a user to enter a word unless the user neters "chupacabra".
correct_word = "chupacabra" # Word needed to exit the loop below.
user_word = "" # initialise user-word variable with an empty string

while True: # Loop indefinitely
    if correct_word == user_word: # If the word entered by the user matches the correct word break out of the loop
        break
    else:
        user_word = input("Enter a word:") # Asks the user to enter a word
print("You've successfully left the loop.") # prints this message when the user successfuly exits the loop


# 3.2.1.10 LAB: The continue statement - the Ugly Vowel Eater *********** (LAB  8) ***********
# Description: This LAB  uses for loop and continue keyword to remove vowel from the word enterd by a user.
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


# 3.2.1.11 LAB: The continue statement - the pretty Vowel Eater *********** (LAB  9) ***********
# Description: This LAB  improves the last LAB  by concatenating non-vowel letters into a long string during subsequent loop turns.
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


# 3.2.1.14 LAB: Essentials of the while loop *********** (LAB  10) ***********
# Description: This LAB  uses while loop to calculate the height of the pyramid that can be built using the given number of blocks 
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


# 3.2.1.15 LAB: Collatz's hypothesis *********** (LAB  11) ***********
# Description: This LAB  tests Collatz's hypothesis using the while loop.
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


# 3.4.1.6 LAB: The basics of lists *********** (LAB  12) ***********
# Description: This LAB  modifies the existing list using basic instructions related to a list.
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

number = int(input("Enter a number:")) # Prompt the user for an integer number

hat_list[2] = number # Replace the middle number of the list with the integer number entered by the user.
del hat_list[4] # Remove the last element from the list.

print(len(hat_list)) # Print the length of the existing list.
print(hat_list) # Print the existing list.

# 3.4.1.13 LAB: The basics of lists *********** (LAB  13) ***********
# Description: This LAB  creates and modifies a simple list and then modifies the list using methods such as append() and insert() and del instruction.
beatles = [] # Create an empty list named beatles.
print("Step 1:", beatles)

# Use the append() method to add the following members of the band to the list.
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

appended_once = False # Boolean variable to check if the list has already been appended once.
for i in range(2): # Use for loop to iterate twice.   
    while True: # Infinite while loop
        band_member_name = input("Enter a band member name:") # Prompt user to input a band meember name.
        if band_member_name == "Stu Sutcliffe" or band_member_name == "Pete Best": # If the band member name inputted by 
                                                                                   # the user is either "Stu Sutcliffe" or "Pete Best" then execute the if block.
            if not appended_once: # Check if the append operation has been carried out once. If not excute the if block.
                beatles.append(band_member_name) # Append the band member name supplied by the user to the existing list.
                appended_once = True # Since the existing list has been appended once change appended_once variable to True.
                break # Break out of the while loop
            else: # If the append operation has been carried out once before, execute the else block.
                if beatles[3] != band_member_name: # If the band member name supplied by the user is the same as the one 
                                                   # appended last time ask the user to input the name again otherwise execute the if block below
                    beatles.append(band_member_name) # Append the band member name supplied by the user to the existing list.
                    break
print("Step 3:", beatles)

del beatles[3] # Use the del instruction to remove the fourth item from the existing list.
del beatles[3] # Use the del instruction to remove the fourth item from the existing list.
print("Step 4:", beatles)

beatles.insert(0, "Ringo Starr") # Use the insert method to add "Ringo Starr" to the beginning of the list.
print("Step 5:", beatles)

print("The Fab", len(beatles)) # Testing list legth

# 3.6.1.9 LAB: Operating with lists - basics *********** (LAB  14) ***********
# Description: This LAB  asks the user to input a list and generates another list with a unique element only.
user_input = input("To use the default list, please Enter; otherwise, please enter a list. (Example: 1,22,22,3):") # Prompt the user to input a list. If the user does not provide a list the default list will be used.
my_list = [] # Create an empty list to store a list
if len(user_input) == 0: # Check if the user has provided a list or not.
    my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9] # Default list to use if the user does not provide a list.
else:
    temp_list = [] # Create an empty list to store a temporary list.
    temp = "" # Initialise the temp variable to an empty sting.
    for character in user_input: # Loop through each character in user_input in turn.
        if character != ",": temp += character # Concatinate character iteratively until ',' character is encountered.
        else: # When ',' character is encountered append everything stored in temp variable to the temp_list.
            temp_list.append(temp) 
            temp = ""
        if len(temp) > 0: temp_list.append(temp) # Once the for loop is completed if there are any data in the temp variable append the data to the temp_list.
    my_list = temp_list[:] # Copy temp_list to my_list

duplicate_item_present = True # Boolean variable to test if duplicate item is present.

while duplicate_item_present: # While loop iterates infinitely until the condition is False.
    for i in range(len(my_list)):
        if i > 0: # if i > 0 copy all the items of my_list before after the my_list[i].
            temp_list = my_list[:i] + my_list[i + 1:]
        else: # Else copy all the items of my_list after the my_list[i].
            temp_list = my_list[i + 1:]
        if my_list[i] in temp_list: # if my_list[i] item is present in the temp_list created above delete my_list[i] and break the for loop
            del my_list[i]
            break
        else: # Else check if i is equal to the length of my_list. If they are equal, it means that no duplicate item is present so the duplicate_item_present variable can now be set to False.
            if i == len(my_list) - 1:
                duplicate_item_present = False
print("The list with unique elements only:")
print(my_list)

# AdditionalListLAB: Tic-Tac-Toe Game *********** (LAB  15) ***********
# Description: Given below is the code for a Tic-Tac-Toe game.
loop_infinitely = keep_playing_game = True # Initialise all the boolean variables to True.
board = [["-" for row in range(3)] for column in range(3)] # Create a 3x3 two-dimensional list for the tic-tac-toe game.
while loop_infinitely: # While loop_infinitely is True, loop infinitely.
    no_row_entry = no_column_entry = no_sign_entry = True # When the while loop starts, initialise all the boolean variables to True.
    print("\nCurrent Board:")
    for i in range(3): print(board[i]) # Print rows on the terminal using the board list iteratively.
    if keep_playing_game: # The if-block gets executed when the keep_playing_game variable is True.
        while no_row_entry: # While no_row_entry is True, loop infinitely.
            try: user_row_entry = int(input("Enter row number[1-3]:")) # Ask the user to input row number between 1 and 3. Catch non-integer entry.         
            except: continue # If a non-integer entry is detected, ask the user to enter the row number again.
            if user_row_entry <= 3 and user_row_entry >= 1: no_row_entry = False  # Check if the row number entered by the user is between 1 and 3. If not, ask the user to enter again.
        while no_column_entry: # While no_column_entry is True, loop infinitely.
            try: user_column_entry = int(input("Enter column number[1-3]:")) # Ask the user to input column number between 1 and 3. Catch non-integer entry.
            except: continue # If a non-integer entry is detected, ask the user to enter the column number again.
            if user_column_entry <= 3 and user_column_entry >= 1: no_column_entry = False  # Check if the column number entered by the user is between 1 and 3. If not, ask the user to enter again.
        while no_sign_entry: # While no_sign_entry is True, loop infinitely.
            user_sign = input("Enter 'o' or 'x' ('q' to quit):" ) # Ask the user to select between signs 'o' and 'x'. Also, accept instruction 'q' for quit.
            if user_sign == 'o' or user_sign == 'x': no_sign_entry = False # no_sign_entry becomes False once the user selects a sign.
            if user_sign == 'q': keep_playing_game = no_sign_entry = loop_infinitely = False # no_sign_entry and loop_infinitely becomes False if the user inputs 'q'
    if board[user_row_entry - 1][user_column_entry - 1] != 'o' and 'x': board[user_row_entry - 1][user_column_entry - 1] = user_sign # In the user-specified row and column, assign the sign specified by the user if no previous sign entry is detected.
