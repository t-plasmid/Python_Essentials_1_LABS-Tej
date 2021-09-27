# Author: Sgt Tej Kumar Rai
# Date Created: 27/09/2021
# Date Last Modified: 27/09/2021
# Description: This source file contains all the labs from Chapter 4 of Pthon Essentils 1 module.
# # The topics covered within this chapter are Functions, Tuples, Dictionaries and Data Processing.

# 4.3.1.6 LAB: A leap year: writing your own functions *********** (LAB 1) ***********
# Description: This LAB passes each test year in the test_data list to the function as an argument, which then determines whether or not the year is a leap year.
# If the year is a leap year, the function returns True; otherwise, it returns False.
# Finally, the function return is compared to the expected return for the corresponding years from the test_results list.
# If they match, the terminal displays 'OK,' otherwise 'Failed.' 

def is_year_leap(year): # Create a one-parameter function
    if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)) : return True # Return True if the year passed as the function's argument is a leap year.
    else: return False # Otherwise, return False.

test_data = [1900, 2000, 2016, 1987] # List of years to test.
test_results = [False, True, True, False] # List of expected returns for the corresponding years in the preceding list. 
for i in range(len(test_data)): # Iterate through each element of the list containing years to test.
	yr = test_data[i] # Use the variable 'yr' to store a year element from the list.
	print(yr,"->",end="") # Print the output to the terminal.
	if is_year_leap(yr) == test_results[i]: print("OK") # Invoke is_year_leap(year) function to check if the year passed to the function is a leap year or not. If the year is a leap year, print 'OK' to the terminal.
	else: print("Failed") # Otherwise, print 'Failed' to the terminal.

# 4.3.1.7 LAB: How many days: writing and using your won functions *********** (LAB 2) ***********
# Description: This LAB further develops on the preceding LAB to generate the number of days in a given month and year and then compares them with the expected return value from a list.
def is_year_leap(year): # Create a one-parameter function.
    if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)) : return True # Return True if the year passed as the function's argument is a leap year.
    else: return False # Otherwise, return False.
    
def days_in_month(year, month): #Create a two-parameter function.  
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # Create a list containing the number of days in each month of a common year.
    if is_year_leap(year): days_in_months[1] = 29 # Replace the second element of the days_in_months list if the given year is a leap year.
    return days_in_months[month - 1] # Return the number of days for the given month.

test_years = [1900, 2000, 2016, 1987] # List of years to test.
test_months = [2, 2, 1, 11] # List of months to test.
test_results = [28, 29, 31, 30] # List of expected returns for the corresponding months and years in the preceding lists.
for i in range(len(test_years)): # Iterate through each element of the test_years list containing years to test.
	yr = test_years[i] # Use the variable 'yr' to store a year element from the list.
	mo = test_months[i] # Use the variable 'mo' to store a month element from the list.
	print(yr, mo, "->", end="") # Print the output to the terminal.
	if days_in_month(yr, mo) == test_results[i]: print("OK") # # Invoke days_in_month(year, month) function to retrive the number of days in the given month and year. If return value matches with the corresponding value from the test_results lists, print 'OK' to the terminal.
	else: print("Failed") # Otherwise, print 'Failed' to the terminal.

# 4.3.1.9 LAB: Prime numbers - how to find them *********** (LAB 3) ***********
# Description: This LAB determines whether or not the supplied integer is a prime number.
# The number is displayed to the terminal if it is a prime number.
def is_prime(num): # Create a one-parameter function.
    if num == 2: return True # Return True is the argument passed to the function is 2.
    elif num > 2: # If the argument passed to the function is greater than true execute the elif block.
        for i in range(2, num): # Iterate from 2 to (num - 1) inclusive.
            if num % i == 0: return False # If num is divisible by i return False. In otherwords, the argument passed to the function is not a prime number.
            else: return True # Otherwise, it's a prime number.

for i in range(1, 20): # Iterate from 1 to 19 inclusive.
	if is_prime(i + 1): print(i + 1, end=" ") # Print all the prime numbers
print() # Print an empty line.

# 4.3.1.10 LAB: Converting fuel consumption *********** (LAB 4) ***********
# Description: This lab converts European fuel consumption to USA fuel consumption and vice versa.
def litres_100km_to_miles_gallon(litres): # Create a one-parameter function.
    # Europe: Fuel consumption = the amount of fuel consumed / 100km
    # USA: Fuel consumption = the number of miles / gallon of fuel
    # A mile = 1609.344 meters
    # A gallon = 3.785411784 litres 
    km_per_litre = 100 / litres # In Europe, fuel consumption equal to the amount of fuel consumed in litres per 100km.
                                # So distance(km) per litre is equal to 100 per fuel consumption in Europe.
    miles_per_litre = km_per_litre / 1.609344 # A mile = 1609.344 meters (or 1.609344 kilometers).
    miles_per_gallon = miles_per_litre * 3.785411784 # A gallon = 3.785411784 litres .
    return miles_per_gallon # Return the miles / gallon value.

def miles_gallon_to_litres_100km(miles): # Create another one-argument function.
    miles_per_litre = miles / 3.785411784 # In the USA, fuel consumption equal to the number of miles per gallon of fuel. Since, a gallon is 3.785411784 litres, miles per litre is equal to fuel consumption in the USA per 3.785411784.
    km_per_litre = miles_per_litre * 1.609344 # A mile = 1609.344 meters (or 1.609344 kilometers).
    litres_per_100km = (1 / km_per_litre) * 100 # km_per_litre km needs 1 litre. So 1 km needs 1/km_per_litre litre. Finally, 100km needs (1/km_per_litre) * 100 litres.
                                                # Note: In Europe, fuel consumption = the amount of fuel consumed / 100km.
    return litres_per_100km # Return the litres / 100km value.

# Print relevant outputs to the terminal.
print(litres_100km_to_miles_gallon(3.9))
print(litres_100km_to_miles_gallon(7.5))
print(litres_100km_to_miles_gallon(10.))
print(miles_gallon_to_litres_100km(60.3))
print(miles_gallon_to_litres_100km(31.4))
print(miles_gallon_to_litres_100km(23.5))
