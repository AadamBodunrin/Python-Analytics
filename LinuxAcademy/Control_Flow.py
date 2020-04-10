# Comparisons
print(238 > 253)
print(63 < 63)
print(24*2 == 48)
print(4 <= 4)
print(96 >= 100)
print(0.1+0.1+0.1 != 0.3)


print(2 in [1,2,3])
print(4.0 in (3.4, 4.5, "Square", 4.00))

x = (3.4, 4.5, "Square", 4.0)
print(type(x))
print(4.0 in x)

print("Square" not in x)

# Conditionals

# Single if statement
if True:
    print("Was true")

#If and else statement
if 1 > 2:
    print("1 is greater than 2")
else:
    print("No, 2 is greater than 1.")

name = "Harts"
if len(name) > 6:
    print("Name is long")
elif len(name) == 5:
    print("The name has exactly five characters")
elif len(name) >= 4:
    print("The name has at least four characters")
else:
    print("The name is short")

# While loop

count  = 0
while count < 10:
    if count % 2 == 0:
        count += 1
        continue
    print(f"We are counting odd number: {count}")
    count += 1


count1 = 1
while count1 < 10:
    if count1 % 2 == 0:
        break
    print(f"We are counting odd numbers {count1}")
    count1 += 1

# For loop
colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    print(color)

for color in colors:
    if color == "blue":
        continue
    elif color == "red":
        break
    else:
        print(color)

point = (2.0, 3.0, 7)
for i in point:
    print(i ** i)

list_of_points = [(1, 2), (2, 3), (3, 4)]
for x,y in list_of_points:
    print("x is {}, y is {}".format(x, y))

ages = {'kevin': 59, 'bob': 40, 'kayla': 21}
for key in ages:
    print(key + " is {} years old.".format(ages[key]))

for key,value in ages.items():
    print("Person named: {}".format(key))
    print("Age is: {}".format(value))

for key, value in ages.items():
    print(value)