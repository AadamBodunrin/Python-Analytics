x = 5
y = 23
z = max(x,y)
print(z)

import math
x = 74
y = math.sqrt(x)
print(y)


import math as m
x = 100
y = m.sqrt(x)
print(y)

from math import sqrt
x = sqrt(6)
print(x)

import easygui
x = easygui.msgbox("To be or not to be", "What Hamlet elocuted")
print(x)

import easygui as e
e.msgbox('What are you doing for my retirement?', 'Mama said:')

def spam(x):
	x += 1
	return x
print(spam(5))

def bar(x,y):
	return int(x/y)
print(bar(8, 7))

def closure(a, b, funct):
	return funct(a, b)
print (closure(8, 9, min))

listy = [1, ['a',['b','c']], 43, "Too many cooks spoil the broth"] 
print(len(listy))

