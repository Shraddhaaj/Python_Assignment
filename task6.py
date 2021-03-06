# -*- coding: utf-8 -*-
"""Task6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F2ai2CzT-4VJsv8B-XBl6kcx8wx_AZnX
"""

#1. Write a program in Python to find out the character in a string which is uppercase using list comprehension.
#ANS:

list1 = "Hello WorlD"

list2 = [char for char in list1 if char.isupper()]
print ("Uppercase letters:", list2)

#2. Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects. The dictionary should map the students with 
#their respective subjects.
#Let’s see how to do this using for loops and dictionary comprehension.
#HINT - Use Zip function also
#Sample input: students = ['Smit', 'Jaya', 'Rayyan'] subjects = ['CSE', 'Networking', 'Operating System']
#Expected output: {‘Smit’ : ’CSE’ , ’Jaya’ : ’Networking’ , ’Rayyan’ : ’Operating System’}

#ANS:

studentinput = ['Smit', 'Jaya', 'Rayyan']
subjectinput = ['CSE', 'Networking', 'Operating System']
print(dict(zip(studentinput,subjectinput)))

#3. Learn More about Yield, next and Generators.
#ANS:
#Yield: Yield is a function that can be used to return statement in a function and when function is called the execution starts with last yield statement.
#next: next() function  is used to fetch next item for the iterable.
#Generators: Python provides genrators to create your own iterator function.

#4. Write a program in Python using generators to reverse the string.
#Input String = “Consultadd Training”

def reverse_string(my_str):
    length = len(my_str)
    for i in range(1, length+1 ):
        yield my_str[-i]

reversed_string = ''.join(reverse_string("Consultadd Training"))
print ("Reversed string: ", reversed_string)

#5. Write an example on decorators.

#ANS:


def  addition(number):
  return number + 555

def addition_call(function):
  number_to_be_added = 2855
  return function(number_to_be_added)

addition_call(addition)