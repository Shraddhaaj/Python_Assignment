# -*- coding: utf-8 -*-
"""Task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E8v0Jcn4ClYGbvR_24nuUaSA2MtCScSv
"""

#1. Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “Consultadd” as a string

operation_input= int(input("Enter a number:"))
if (operation_input%3==0):
  print("Consultadd")
# If a number is divisible by 5 it should print “Python Training” as a string
if (operation_input%5==0):
   print("Python Training")

# If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string.

if ((operation_input%3==0) & (operation_input%5==0)):
 print ("Consultadd Python Training")

#2.Write a program in Python to perform the following operator based task:
#Ask user to choose the following option first:
#If User Enter 1 - Addition
#If User Enter 2 - Subtraction
#If User Enter 3 - Division
#If User Enter 4 - Multiplication
#If User Enter 5 - Average
#Ask user to enter two numbers and keep those numbers in variables num1 and num2 respectively for the first 4 options mentioned above.
#Ask the user to enter two more numbers as first and second for calculating the average as soon as the user chooses an option 5.
#At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
#NOTE: At a time a user can only perform one action.



option= int(input("Enter the option:  "))

if (option>=1 and option<=5):
  print("Enter two numbers:" )
  num1= int(input("Enter number 1:" ))
  num2= int(input("Enter number 2:" ))

if (option==1):
  Result= num1 + num2
  print("Result =",Result)

elif (option==2):
  Result = num1 - num2
  print("Result=",Result)


elif (option==3):
  Result = num1 / num2
  print("Result=", Result)


elif (option==4):
  Result = num1 * num2
  print("Result=", Result)

elif (option==5):
  num3= int(input("Enter a new value:" ))
  num4= int(input("Enter a new Value:" ))
  Result = (num1 + num2 + num3 +num4) / 4
  print("Result=", Result) 



if (Result<=0):
  print("NEGATIVE:")

#3. Write a program in Python to implement the given flowchart

a=10
b= 20
c= 30

avg = (a+b+c)/3
print("avg =", avg)

if avg > a and avg > b and avg > c:
    print("%d is higher than %d, %d, %d" %(avg, a, b, c))
elif avg > a and avg > b:
    print("%d is higher than %d, %d" %(avg, a, b))
elif avg > a and avg > c:
    print("%d is higher than %d, %d" %(avg, a, c))
elif avg > b and avg > c:
    print("%d is higher than %d, %d" %(avg, b, c))
elif avg > a:
    print("%d is just higher than %d" %(avg, a))
elif avg > b:
    print("%d is just higher than %d" %(avg, b))
elif avg > c:
    print("%d is just higher than %d" %(avg, c))

#4. Write a program in Python to break and continue if the following cases occurs:
#If user enters a negative number just break the loop and print “It’s Over”
#If user enters a positive number just continue in the loop and print “Good Going".
#Doubt(about output)
for i in [ 5, -25 ,30, 80, 58, 95, 70, -80, 79, 88 ]:
  if (i > 0):
    print("Good Going")
    continue
  print("It's Over")
  if (i < 0):
    break

#5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.

for i in range (2000,3201):
  if (i%7==0 and i%5!= 0):
    print(i)

#6. 6. What is the output of the following code examples?


#1.ANS: After running this code I got an error of 'int' object is not iterable.
#2. ANS: 0
#        error
#        1
#        error
#        2
# 
#3.ANS: 0
#     1
#     2
#     3
#     4

#7.Write a program that prints all the numbers from 0 to 6 except 3 and 6.
#Expected output: 0 1 2 4 5
#Note: Use ‘continue’ statement

for i in range (7):
  if i==3 or i==6:
    continue
  print(i)

#8. Write a program that accepts a string as an input from the user and calculate the number of digits and letters.
#Sample input: consul72
#Expected output: Letters 6 Digits 2
 
j = input("String Input: " )
digit=letter=0 
for i in j:
  if i.isdigit():
    digit= digit+1
  elif i.isalpha():
    letter = letter +1
  else:
    pass

print("Letters:",  letter)
print("Digits:",  digit)

#9.Read the two parts of the question below:
#Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever.
#Modify the program so that it asks users whether they want to guess again each time. Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question whether 
#they want to continue guessing. The program stops if the user guesses the correct number or answers “no”.(The program continues as long as a user has not answered “no” and has 
#not guessed the correct number).


Lucky_number = 8
number = int(input("Guess the lucky number "))
while True:
  if number == Lucky_number:
   print("This is a right number")
   break
  else:
    print("This is not the right number")
    break

# 10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as
#While counter <= 5:
#print(“Type in the”, counter, “number”
#counter=counter+1
#The program asks for five guesses (no matter whether the correct number was guessed or not). If the correct number is guessed, the program outputs “Good guess!”, otherwise it 
#outputs “Try again!”.After the fifth guess it stops and prints “Game over!”.

#ANS:
Correct_Number = 7
counter = 1
while counter <= 5:
   number = int(input("Guess the " + "str(counter)" + " number "))
   if number != Correct_Number:
       print ("Try again.")
   else:
       print ("Good guess!")
   counter = counter +1
else:
   print ("Game over")

# 11. In the previous question, insert break after the “Good guess!” print statement. break will terminate the while loop so that users do not have to continue guessing after
#they found the number. If the user does not guess the number at all, print “Sorry but that was not very successful”.

Correct_Number = 20
counter = 1
while counter <= 5:
   number = input("Guess the " + str(counter) + ". number ")
   if number != Correct_Number :
     print ("Try Again")
   elif number == Correct_Number:
       print ("Good Guess!")
       break
   counter = counter +1
else:
   print ("Sorry but that was not very successful")