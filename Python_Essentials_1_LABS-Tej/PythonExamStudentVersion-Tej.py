##PLEASE FILL OUT THE BELOW DETAILS
##Student Name: Tej Kumar Rai
##Course Number: SIMR 20/001
##Student Number: 2*****52

##complete each task which is shown as a comment. 
#complete each task directly below the comment
#each task shows a task number, and number of marks awarded
#on each task requiring an output, ensure the task goes on a separate line (unless stated)
#and ensure that it states the task number prior to any output e.g. Task 11 
#upload your final file to your assigned folder share on class.net
# \\192.168.68.114\test-sub\regiNumber

#####################################################
#Section 1 25 Marks


#1) Create and Assign a type float variable called fltOne the value 10 (3)
fltOne = 10.
#2) Create and Assign a type float variable called fltTwo the value 20 (3)
fltTwo = 20.0
#3) Create and Assign a type float variable called fltThree with the product of fltTwo and fltOne(3)
fltThree = fltTwo * fltOne
#4) Create and assign a variable called stringOne with the value "The product of fltOne and fltTwo = "(3)
stringOne = "The product of fltOne and fltTwo = "

#5) On the console, output stringOne and fltThree (in that order) (3)
print("Task 5:", stringOne, fltThree)
#6) increment fltOne  (3)
fltOne += 1

#7)  prompt the user to provide an input to fltTwo with the message "Please provide another number for fltTwo". Ensure a float is given (4)
fltTwo = float(input("Task 7: Please provide another number for fltTwo"))

#8) on the console, output the product of fltOne and flotTwo with a suitable message (3) 
print("Task 8:", "The product of fltOne and fltTwo = ", fltOne * fltTwo)

#####################################################
#Section 2 35 Marks

#8) take the input from fltTwo and apply a decision based on the number inputted . 
#The decision should be based on if the user inputs a number below 100 
#the code should output "below 100" (5)
if fltTwo < 100: print("Task 8:", "below 100")

#9) take the difference between of fltOne and fltTwo (fltOne - fltTwo)
#Using if, else and elif, output the following: 
#If the product is below 0, output "below 0"
#if the product is 0 output "value is zero"
#if the product is above 0 output "above 0" (8)
if (fltOne - fltTwo) < 0: print("Task 9:", "below 0")
elif (fltOne - fltTwo) == 0: print("Task 9:", "value is zero")
else: print("Task 9:", "above 0")

#10) create a list called listOfInts (4)
listOfInts = []

#11 part a) create a for loop to iterate through the above list and populate the list with 
#{4,6,8,10,12,14,16,18,20,22}. Output the list to the console with a suitable message(7)
for i in range(10): listOfInts.append(4 + i * 2)
print("Task 11 part a:", listOfInts)

#11 part b) create a for loop to iterate through the above list and 
#multiply each value by three assigning the new value to the respective 
#index in the list. The list should now look like {12,18,24.....} (8)
for i in range(len(listOfInts)):
    listOfInts[i] *= 3
#11 part c )output listOfInts to the screen with a suitable message (3)
print("Task 11 par c:", listOfInts)

#####################################################
#Section 3 20 marks

#14) create a function which calculates a decrease of a given percentage (10 marks)
# the function should be called calcPerc
#the function should take a cost parameter and a percentage parameter
#it should return the cost less the percentage amount
#For example if the paramenters are cost = 100 and percentage = 50, it should return 50. 
#For another example, if the parameters are cost = 50 and percentage = 10, it should return 45.
#The percentage value should assume 10% if no value is given
#print a test to the screen with cost set as 50 and percentage set as 10
def calcPerc(cost, percentage = 10):
    return (cost - (cost * (percentage / 100)))
print("Task 14:", calcPerc(50))

#15) create a function called caseChanger which takes a string argument written all in lower case
#It will output all letters in lowercase except e which it will convert to capital E (10 marks)
#Perform a test print which using hello: caseChanger("hello") this should
#print hEllo to the console.
def caseChanger(user_word):
    formatted_word = ""
    for letter in user_word:
        if letter == "e": formatted_word += "E"
        else: formatted_word += letter
    return formatted_word

print("Task 15:", caseChanger("hello"))

##################################################### 
#Section 4 20 marks

#16)a) Create a list that represents a set of students. The list should contain the following
#students: Clark,Horan,Rai,White,Cooper,Jones,Cox,Smith (4 marks)
lstStudents = ['Clark', 'Horan', 'Rai', 'White', 'Cooper', 'Jones', 'Cox', 'Smith']

#b) use a method to order the students so that they are in alphabetical order (3 marks)
lstStudents.sort()

#17) create a tuple that represents exam marks with the following data. (4 marks)
#These are the respective exam marks for the alphabetically ordered student list
# 65,66,67,80,90,65,65,93
lstMarks = [65, 66, 67, 80, 90, 65, 65, 93]
tupStudentsMarks = ()
for i in range(len(lstStudents)):
    tupStudentsMarks += (lstStudents[i], lstMarks[i])


#18) Dictionary question (9 marks)
#create a dictionary 
#write code which adds both the student and a their corresponding mark. 
#do not perform this long hand (as in writing out the values above). Use data
#from the existing tuples above to create the dictionary
    dictStudentsMarks = {}
for i in range(0, len(tupStudentsMarks), 2):
    dictStudentsMarks[tupStudentsMarks[i]] = tupStudentsMarks[i + 1]
