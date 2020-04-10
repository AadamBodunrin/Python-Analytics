# Strings

# 'Single quoted string'
# "Double quoted string"
# '''This is a triple quoted string'''

print("Pass" + "word")
print("Single" + " quotes")
print("Ha" * 4)

# Find is used to see if an item is in a string. -1 means false here, while the position of the item is returned if found.
print("double".find("s")) 
print("double".find("u"))
print("double".find("bl"))

#Lower, upper, title are used to change a string to suit the method called
print("TestInG".lower())
print("another".upper())
print("PassWORD123".lower())
print("the animal farm by george orwell".title())

print("Tab\tDelimited")
print("\nNew\nLine")
print("Slash\\Character")
print("'Single' in Double")
print('"Double" in single')
print("\"Double\" in Double")

## Numbers (Integers and Floats) e.g. 2 is an integer, 2.0 is a float
print(2+2)  # Will return 4 (an integer)
print(2.0 + 2) # will return a 4.0(a float)

print(10 - 4) # Subtraction
print(3 * 9)# Multiplication
print(5 / 3) # Division
print(5 // 3) # Floor division, always returns a number without a remainder

print(8 % 3) # Modulo division, returns the remainder

print(2.0 ** 3) # Exponent
print(pow(3, 3))

## Converting string and numbers
print(str(1.1)) # Convert the float 1.1 to string
print(int("10")) # Convert a string to an intger
print(float("5.6")) #Convert the string to a float
print(float(5))
print(float(("5,45.67").replace(",", ""))) # Use replace to remove the comma and then convert to a float

## Booleans and None
print(None, True, False) 
print(bool(1), bool(0)) # 1 will return True, 0 returns False

## Working with Varibles

my_name = "Aadam" # Saving a string as a variable
print(my_name)  
my_name += " Bodunrin" # Adding another string to an already named variable
print(my_name)

## Lists

my_lists = [1,2,3,4,5] # A list
print(my_lists)
my_list = ["Scare", "Wild", "Animals"]
print(my_list[0]) #print only the item indexed at zero
print(my_list[-1]) #print the last item in the list
print(len(my_lists)) #Print the length of the string

print(my_lists[0:2]) #Slicing a list. 0:2 returns items indexed at 0 and 1
print(my_lists[:4]) # Return all the items indexed at 0,1,2,3
print(my_lists[2:]) # return all the items indexed from 2 to the end of the list
print(my_lists[::2]) #Return every other item in the list
print(my_lists[::-1]) #Reverse the whole list

my_lists[0] = "Wild" #Change the value of the item indexed at zero
print(my_lists)
my_lists.append(6) #Append is used to add an element to the end of a list
my_lists.append(7)
print(my_lists)
my_lists += [8, 9, 10, 11]

my_lists.remove(8) #Removes 8 in the list
my_lists.pop() #Pop removes the last item in a list
my_lists.pop(4) #This removes the item indexed at 4
print(my_lists)
my_lists.insert(2, 42) #Insert is used to add an item to a particular position in a list. The position comes first
print(my_lists)

#Tuples and Range
points = (2.0, 4.0) #Create a tuple
print(points[0], points[1]) #Access the item in  tuple

Point_3D = points + (3.5,) #Add a new item to a tuple. The comma is a must for a tuple.
print(Point_3D)
x,y,z = Point_3D #Assign the three items in the tuple to x,y,z respectively. i.e. Unpacking
print(y) #This returns the second item in the tuple

# Another example of Unpacking
print("My name is %s %s" % ("Keith", "Thompson")) 
print("My name is {} {}.".format("Aadam", "Olajide"))

print(range(10))
print(list(range(10)))
print(list(range(1, 40, 2)))


# Dictionaries
ages = {'Kevin': 29, 'Alex': 29, 'Bob': 40} #Create a dictionary
print(ages)
print(ages["Kevin"])
ages["Nick"] = 47
print(ages)
del ages["Alex"]
print(ages)
print(ages.pop("Nick"))
print(ages)
print(ages.get("Kevin"))
print(ages.keys())
print(ages.values())
print(list(ages.keys()))

weights = dict(kevin = 40, Jared = 43)
print(weights)

colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla', 'red')])
print(colors)


