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

a_list = [1, ["a",["b","c"]], 43, "Too many cooks spoil the broth"] #Create a list
print(len(a_list))#find out how many items are in the list

print(a_list[1][1][1])#To callout "c" from a_list

a_list.append("Foul play") #add string "foul play" to the end of a_list
print(a_list)

a_list.insert(1, "Child's Play" ) #Insert "Child's Play at position 1 of a_list
print(a_list)

a_list.extend([1,2,3]) #unpack the list and add it to the end of a_list
print(a_list)

a_list.pop() #Removes the last item in the list. That would be three in this case
print(a_list)

a_list.pop(3) #Remove the item in position 3 1.e 43
print(a_list)

print(a_list[3]) #Print the third item in the list

print(a_list[2:5]) #Print from the second item to the fifth item i.e. elements in position 2, 3 and 4

print(a_list[:4]) #Print from the beginning item to the fourth item i.e. elements in position 0,1,2,3

print(a_list[1:]) #Print from the first item to the end of the list

print(a_list[-1]) #Print the last item in the list

print(a_list[::-1])  #Print the list backwards, starting from the last item to the first i.e. reverse the list

a_list.remove(2) #Remove the first '2' in the list

a_list[1] = "Sycamore roots" #Change the item in position 1 to "Sycamore roots"
print(a_list) 


x = [1,4,5,68,9,45,23,67,33,34]
for items in range(len(x)):
	print(items, x[items])

y = list(range(len(x)))
print(y)

"""Write a function search_list that searches a 
list of tuples pair and return the value 
associated with the first element of 
the pair"""

list_of_tuples = [("AAPL", 96.43), ("IONS", 38), ("GS", 158)]

def search_list(list_of_tuples, value):
	for element in list_of_tuples:
		if element[0] == value.upper():
			return element[1]
	else:
			return("The value you selected is not available")

print(search_list(list_of_tuples, "GS"))

inventory = [("widgets", 100), ("spam", 30), ("eggs", 200)]
def search_list(inventory, value):
	for elements in inventory:
		if elements[0] == value:
			return elements[1]
	else:
		return None
y =search_list(inventory, value = "spam")
print(y)
z= search_list(inventory, value = "hay")
print(z)

dictname = {"AAPL":96.43 , "IONS":38, "GS": 158, "widgets": 100, "spam": 30, "eggs": 200} #Create a dictionary
print(dictname.keys()) #print the keys of the dictionary
print(dictname.values()) #print the values of the dictionary
print(sorted(dictname.keys())) #print the keys in ascending order
print(sorted(dictname.keys(), reverse = True)) #print the keys in descending order
print(sorted(dictname.values())) #print the value in ascendinf order
print(dictname["AAPL"]) #print the vale of AAPL
print(dictname.get("IONS")) #print the value of IONS
dictname["Awarri"] = 89 #Add a new key:value pair to the dictionary
del(dictname["Awarri"]) #delete the key:value pair of Awarri
print(dictname)

import datetime as d 
z= d.date(2016, 12, 24)
y = d.date(2019, 11, 21)
print(max(z,y)) 
print(y - z) #To check the difference between the two days
print((y-z).days) #To print the just the number of days
print(d.date.today()) #To print today's date
print(d.datetime.today()) #To print today's date and time

#To add days, minutes and seconds using the datetime library
zz = (d.datetime.today())
tt = zz+d.timedelta(days= 5)
print(zz, tt)
ww = tt +d.timedelta(minutes = 5, seconds = 10)
print(tt, ww)

#To convert  Date in string to normal date 
finale = "01-Apr-03"
finale_obj = d.datetime.strptime(finale, '%d-%b-%y')
print(finale_obj)

#To convert a time string to time
ending = "2:18:24"
Hours, Minutes, Seconds = ending.split(":")
x = d.timedelta(hours = int(Hours), minutes = int(Minutes), seconds = int(Seconds))
print(x)

#To convert a date to string
today = d.datetime.today()
today_now = d.datetime.strftime(today, "%m-%d-%y %H:%M:%S")
print(today, today_now)

# To open a csv file and view its content
data_tuples = list()
with open("sample_data.csv", 'r') as sample_data:
	for line in sample_data:
		data_tuples.append(line.strip().split(" , "))
print(data_tuples[0:10])




