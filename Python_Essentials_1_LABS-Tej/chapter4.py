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
