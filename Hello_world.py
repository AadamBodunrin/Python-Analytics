#Using the max function, which is higher 5 or 23?
x = 5
y = 23
z = max(x,y)
print(z)

#Use the math function to find the square root of 74
#Option 1
import math
x = 74
y = math.sqrt(x)
print(y)


#Option 2
import math as m
x = 74
y = m.sqrt(x)
print(y)

#option 3
from math import sqrt
x = sqrt(74)
print(x)

#Use the easygui to print the message "To be or not to be" titled "What Hamlet elocuted"
#Option 1
import easygui
x = easygui.msgbox("To be or not to be", "What Hamlet elocuted")
print(x)

#Option 2
import easygui as e
e.msgbox("To be or not to be", "What Hamlet elocuted")

#Create a function that add 1 to any number you call
def spam(x):
	x += 1
	return x
print(spam(5))

#Create a function that print the integer value after dividing x by y
def bar(x,y):
	return int(x/y)
print(bar(8, 7))

def closure(a, b, funct):
	return funct(a, b)
print (closure(8, 9, min))

a_list = [1, ['a',['b','c']], 43, "Too many cooks spoil the broth"] #Create a list
print(len(a_list))#find out how many items are in the list
print(a_list[1][1][1])#To callout 'c' from a_list

