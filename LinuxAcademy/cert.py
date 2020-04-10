def fib(n):
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
        yield a
fib_gen = fib(4)
print(fib_gen)


num = 10
if num > 20 or num >= 10:
    print("First")
elif num <= 10:
    print("Second")
else:
    print("Third")

ages = {'Keith': 30, 'Levi': 25, 'John': 20}
age = ages.get('Kevin')
print(age)

val = 1 or '2'
val *= 3
print(val)

num = input("Enter a float value: ")
new_num = float(num) // 100 * 1.0
print(new_num)

def add_five(num1, num2=5):
    return num1 + 5
print(add_five(1, 2))

num = 9
if num < 10:
    print("Less than 10")
if num > 10:
    print("Greater than 10")
else:
    print("Less than 10")

values = ['Kevin Bacon', 60, '555-555-5555', False]
val = not values[1]
print(val)

num = 15.1
num2 = num / 4
num2 //= 2
num2 + 1
print(num2)

def fizz(num):
    if num % 3 == 0 and num % 5 == 0:
      return 'FizzBuzz'
    elif num % 3 == 0:
      return 'Fizz'
    elif num % 5 == 0:
      return 'Buzz'
    else:
      return num

print(fizz(14))

num = 12
if num <= 15:
    print("Less than 15")
elif num >= 15:
    print("Greater than 15")
else:
    print("Less than 15")

letter = 'a'
if letter < 'b':
    print("First")
if letter == 'b' or letter > 'c':
    print("Second")
elif letter <= 'a':
    print("Third")
else:
    print("Fourth")
    
for num in range(1, 10, 2):
	if num % 3:
		print(num)
		
num = 5
message = 'Hello'
print(message, num)


def hello(name, salutation):
    print(salutation, name, sep=", ")

hello("William", salutation="Howdy")

ages = {'Keith': 30, 'Levi': 25, 'John': 20}
output = ages.keys()
print(output)

pair1 = ('a', 'b', 'c')
pair2 = ('d', 'e', 'f')
index = 0

while index < len(pair1):
    for item in pair2:
        print(pair1[index], item)
    index += 1

num = 12
num2 = num
num = num + 1
num2 = num2 / 2
print(num2)

num1 = 15
num2 = num1
num1 *= 2
print(num2)
