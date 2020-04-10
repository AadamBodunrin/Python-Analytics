#The following will create a txt file
with open('xmen.txt', 'w+') as my_file:
    my_file.write('Beast\n')
    my_file.write('Phoenix\n')
    my_file.writelines([
        'Cyclops\n',
        'Bishop\n',
        'Nightcrawler\n',
    ])



#This chunck will open the file and read its contents
my_file = open('xmen.txt', 'r')
with my_file:
    print(my_file.read())

import os

stage = os.getenv("STAGE", "dev").upper()

output = ("We are running in {}".format(stage))

if stage.startswith("PROD"):
    output = "DANGER!!! - " + output

print(output)

#Error Handing
import sys

file_name = 'recipes.txt'

try:
    my_file = open(file_name, 'x+')
    my_file.write('Meatballs\n')
    my_file.close()
except FileExistsError as err:
    print(f"The {file_name} file already exists")
except:
    print(f"Unable to write to the {file_name} file")
else:
    print(f"Wrote to {file_name}")
finally:
    print("Execution complete")

#Higher order function
"""def inspect(func, *args):
    print(f"Running {func.__name__}")
    val = func(*args)
    print(val)
    return val

def combine(a, b):
    return a + b 

print(inspect(combine, 1, 3)) """

#using decorators
def inspect(func):
    def wrapped_func(*args, **kwargs):
        print(f"Running {func.__name__}")
        val = func(*args, **kwargs)
        print(f"Result: {val}")
        return val

    return wrapped_func

@inspect
def combine(a, b):
    return a + b

print(combine(a = 1, b = 12))

class User:
    base_url = 'https://example.com/api'

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def query(cls, query_string):
        return cls.base_url + '?' + query_string

    @staticmethod
    def name():
        return "Kevin Bacon"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

print(User.name)
print(User.name())
print(User.query('name=test'))
print(User.base_url)
user = User('Keith', 'Thompson')
print(user.full_name)
print(user.name())


# Breakpoint Debugging with PDB

