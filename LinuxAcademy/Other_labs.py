# Indexing and Slicing Python Strings

message = input("Enter a message: ")
print("First character:" + message[0])
print("Last charcater:" + message[-1])
print("Middle character:", message[int(len(message) / 2)])
print("Even index characters:", message[0::2])
print("Odd index characters:", message[1::2])
print("Reversed message:", message[::-1])

#Using Python String Methods
print("Lowercase: " + message.lower())
print("Uppercase: " + message.upper())
print("Capitalized: " + message.capitalize())
print("Titled: " + message.title())
words = message.split()
print("Words: " , words)

sorted_words = sorted(words)

print("Alphabetic First Word:", sorted_words[0])
print("Alphabetic Last Word:", sorted_words[-1])


#Using Python Dictionaries
emails = {}

emails['ashley'] = 'ashley@example.com'
emails['craig'] = 'craig@example.com'
emails['elizabeth'] = 'elizabeth@example.com'

assert emails == {
    'ashley': 'ashley@example.com',
    'craig': 'craig@example.com',
    'elizabeth': 'elizabeth@example.com'
}, f"Expected `emails` to be {{'ashley': 'ashley@example.com', 'craig': 'craig@example.com', 'elizabeth': 'elizabeth@example.com'}} but got: {repr(emails)}"


del emails["craig"]

emails["dalton"] = "dalton@example.com"

print(list(emails.keys()))
print(list(emails.values()))

pairs = list(emails.items())
print(pairs)

for key,values in emails.items():
	print(key, values)

users = []

assert users == [], f"Expected `users` to be [] but got: {repr(users)}"

users.append('kevin')
users.append('bob')
users.append('alice')

del users[1]

rev_users = list(reversed(users))

users.insert(1, 'melody')

users += ['andy', 'wanda', 'jim']

center_users = users[2:4]

#Utilizing Python Loops
upper_number = int(input("How many values should we process: "))

for i in range(1, upper_number + 1):
    print(i)

for i in range(1, upper_number + 1):
    if i % 3 == 0 and i % 5 == 0:
        print ("Fizzbuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#Defining and Using Python Functions
def split_name(name):
    names = name.split()
    first_name = names[0]
    last_name = names[-1]

    return {"First_name" : first_name,
        "last_name" : last_name,
        }

print(split_name("Wild Drinkwater"))

def is_palindrome(item):
    item = str(item)
    return item == item[::-1]

def build_list(item, count = 1):
    items = []
    for _ in range(count):
        items.append(item)
    return items

print(build_list("Lake", 1))



pick_a_num = int(input("Kindly pick a number: "))

if pick_a_num % 3 == 0 and pick_a_num % 5 == 0:
    print("FizzBuzz")
elif pick_a_num % 3 == 0:
    print("Fizz")
elif pick_a_num % 5 == 0:
    print("Buzz")
else:
    print("This is the number you picked:" , pick_a_num)

