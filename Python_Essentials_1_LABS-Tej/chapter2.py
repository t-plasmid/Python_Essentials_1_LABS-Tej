# Author: Sgt Tej Kumar Rai
# Date Modified: 22/09/2021
# Description: This source file contains all the labs from Chapter 2 of Pthon Essentils 1 module.

# ******************************************************************* Start: Chapter 2 ******************************************************************* #
# The topics covered within this chapter are data types, variables, basic input-output operations and basic operators.

# 2.1.1.6 LAB: The print() function *********** (Snippet 1) ***********
# Start: This snippet invokes the print function using quotes and parenthesis
print("Hello, Python!") # Uses double quotes
print("Tej") # Prints my name
print('Tej') # Uses single quotes
print() # Print a new line

# 2.1.1.18 LAB: The print() function *********** (Snippet 2) ***********
# Start:  This snippet uses keyword arguments sep and end of the print function
print("Programming","Essentials","in", sep="***", end="...") # Keyword arguments sep and end are used to generated the expected output
print("Python") 
print() # Print a new line
# End

# 2.1.1.19 LAB: Formatting the output *********** (Snippet 3) ***********
# Start: The snippet formats the character output
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
print() # Print a new line
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****") # \n sequence is used to reduce the number of print() function invoations to one. 
print() # Print a new line
# Makes the arrow twice as large while keeping the proportions.
# Also the arrow is duplicated and placed side by side.  
print("        *        " * 2)
print("       * *       " * 2)
print("      *   *      " * 2)
print("     *     *     " * 2)
print("    *       *    " * 2)
print("   *         *   " * 2)
print("  *           *  " * 2)
print(" *             * " * 2)
print("*****       *****" * 2)
print("    *       *    " * 2)
print("    *       *    " * 2)
print("    *       *    " * 2)
print("    *       *    " * 2)
print('    *       *    ' * 2) # Here quotes has been replaced with apostrophes to test its effect.
print("    *********    " * 2)
print() # Print a new line
# End

# 2.2.1.11 LAB: Python literals - strings *********** (Snippet 4) ***********
# Start: This snippet make use of one-line print function to output three lines of outputs.
print('"I\'m\n""learning""\n"""Python"""') # One-line print() function which outputs three lines of expected output.
print() # Print a new line
# End

# 2.4.1.7 LAB: Variables *********** (Snippet 5) ***********
# Start: This snippet makes use of variables to calculate the total number of apples.
john = 3 # John had three apples
mary = 5 # Mary had five apples
adam = 6 # Adam had six apples
print(john, mary, adam, sep=",") # It prints the number of apples each of them had on one line separated by a comma.
total_apples = john + mary + adam # It calculates the total apple each of them had.
print("Total number of apples:", total_apples) # Finally, it prints the total number of apples.
print() # Print a new line
# End

# 2.4.1.9 LAB: Variables: a simple converter *********** (Snippet 6) ***********
# Start: This snippet converts miles to kilometer and vice-versa.
kilometers = 12.25
miles = 7.38

miles_to_kilometers = 1.61 * miles # Converts miles to kilometer. Note: 1 miles = 1.61 kilometers
kilometers_to_miles = kilometers / 1.61 # Converts kilometers to miles. Note: 1 kilometers = 1 / 1.61 miles

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
print() # Print a new line
# End

# 2.4.1.10 LAB: Operators and expressions *********** (Snippet 7) ***********
# Start: This snippet evaluates the expression and ouput the result to the terminal.
x =  -1 # Sample inputs are 0, 1 or -1
x = float(x)
y = (3 * x ** 3) - (2 * x ** 2) + (3 * x) - 1 # Here y = 3x^3 - 2x^2 + 3x - 1
print("y =", y) # Expected outputs are -1.0, 3.0 and -9.0 respectively
print() # Print a new line
# End

#2.5.1.2 LAB: Comments *********** (Snippet 8) ***********
# Start: This snippet computes the number of seconds in a given number of hours
hours = 2 # Number of hours
seconds = 3600 # Number of seconds in 1 hour

print("Hours: ", hours) # Prints the number of hours
print("Seconds in Hours: ", hours * seconds) # Prints the number of seconds in a given number of hours
print("Goodbye") # Prints Goodbye
print() # Print a new line
# End

# 2.6.1.9 LAB: Simple input and output *********** (Snippet 9) ***********
# Start: This snippet evalueates the results of four basic arithmetic operations
a = float(input("Enter the first value:")) # input a float value for variable a here
b = float(input("Enter the second value:")) # input a float value for variable b here

print(str(a + b)) # output the result of addition here
print(str(a - b)) # output the result of subtraction here
print(str(a * b)) # output the result of multiplication here
print(str(a / b)) # output the result of division here
print("\nThat's all, folks!")
print() # Print a new line
# End

# 2.6.1.10 LAB: Operators and expressions *********** (Snippet 10) ***********
# Start: This snippet evaluates the expression below.
x = float(input("Enter value for x: ")) # Input a float value for variable a
y = 1 / (x + 1 / (x + 1 / (x + 1 / x))) # Evaluates the expression on the right and stores the value on y
print("y =", y) # Prints the evaluated value
print() # Print a new line
# End

# 2.6.1.11 LAB: Operators and expressions *********** (Snippet 11) ***********
# Start: This snippet evaluates the end time from the given time and duration
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

end_hour = (hour + (mins + dura) // 60) % 24 # It's a 24 hour clock and 60 mins = 1 hour
end_mins = (mins + dura) % 60 # Returns remainder which is always less than 60 mins

print(end_hour, end_mins, sep=":") # Prints output in the format hh:mm
print() # Print a new line
# End

# ******************************************************************* End: Chapter 2 ******************************************************************* #