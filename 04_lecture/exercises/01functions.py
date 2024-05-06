"""
Exercises "Functions"
"""
from typing import Callable

"""
### Function Definition / Execution ###

Define a function called "bark()". When executed, "Woof" should get printed to the console.
Execute the function after its definition and run the program!
"""


# Write your solution here
# def bark():
#    print("Woof")


# bark()

"""
### Function with 1 Argument, additional logic ###

Write a program that asks the user to enter an animal. The program should respond with the corresponding animal sound.
Define a function called "makeSound(animal)". The function should use the given input to print the correct animal sound.
Add functionality for at least 3 animals and print the right sounds.
If the animal doesn't exists in the program, print "???".
Use a loop to repeatedly ask the user to enter another animal.
Make sure that upper- and lowercase letters both work when entering an animal.

Examples:
    Please enter an animal: >> dog
    Woof
    Please enter an animal: >> Cat
    Meow
    ...
"""

# Write your solution here
"""
def make_sound(animal):
    animal = animal.lower()
    if animal == "dog":
        print("woof")
    elif animal == "cat":
        print("meow")
    elif animal == "cow":
        print("moo")
    else:
        print("???")


i = 0
for i in range(0,3):
    animal_input = input("enter an animal: ")
    make_sound(animal_input)
    i += 1
"""

"""
def make_sound(animal: str) -> str:
    animal = animal.lower()
    sound = "???"
    if animal == "dog":
        sound = "woof"
    elif animal == "cat":
        sound = "meow"
    elif animal == "cow":
        sound = "moo"
    return sound


print("Hi! To exit, enter an ""x"" instead of an animal.")

while True:
    animal_input = input("enter an animal: ")
    if animal_input == "x":
        print("Bye!")
        break
    else:
        result = make_sound(animal_input)
        print(result)
        continue
"""

"""
### Function with 2 Arguments ###

Write a function named print_many_times(text, times), which takes a string and an integer as arguments. 
The integer argument specifies how many times the string argument should be printed out.

Example:
    print_many_times("Gimme Five!", 5)
    Gimme Five!
    Gimme Five!
    Gimme Five!
    Gimme Five!
    Gimme Five!

Additional Task:
Instead of "hard coding", let the user enter the text and the number of times to print it!
Ask the user repeatedly using a loop.
"""

# Write your solution here

"""
def print_many_times(text: str, times: int):
    for i in range(times):
        print(text)


i = 1
while i <= 3:
    times_input = int(input("How many times should the text be printed? --> "))
    print_many_times("Gimme Five!", times_input)
    i += 1
"""

"""
### Return Values ###

Define a function named greatest_number, which takes three arguments. The function returns the greatest in value of the 
three. Use the already defined function "print_greatest" and pass the return value of your function to it!

Example:
    return_value = greatest_number(3, 4, 1)
    print_greatest(return_value)
    The greatest number is 4!
    
Additional Task:
Add a type hint to the return value of the function!
"""

# Write your solution here
"""
def greatest_number(a: int, b: int, c: int) -> int:
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c


nr1 = int(input("Enter number 1: << "))
nr2 = int(input("Enter number 2: << "))
nr3 = int(input("Enter number 3: << "))
return_value = greatest_number(nr1, nr2, nr3)


# print(type(return_value))

def print_greatest(number: int) -> int:
    print(f'The greatest number is {number}.')


print_greatest(return_value)
"""

"""
### Type Hints ###

Refactor your programs from above and add type hints to all function arguments and return values (if available)!
"""

# No code here, refactor the programs above!

"""
### Named arguments ###

Define a function named super_print which takes two arguments, a string and a boolean value.
If the boolean value is false, print the text as it was. If its True, print it in all upper case.
Use named arguments to use a different order of the arguments. First, use the string as first argument. For the second
call, use the boolean value as the first argument. Also, make use of type hints for the function arguments.

Example Outputs:
    HELLO WORLD
    hello world
"""

# Write your solution here
"""
def super_print(a: str, b: bool):
    if b == True:
        print(a.upper())
    else:
        print(a)


super_print("text1 should be printed in lower case", False)
super_print(b=True, a="text2 should be printed in upper case")
"""

"""
def super_print(a: str, b: bool):
    if b == "False":
        print(a)
    elif b == "True":
        print(a.upper())
    else:
        print("???")


a_text = input("Please enter a short text to be printed: ")
b_choice = input("Should the text be printed in upper case? (True/False) ")

super_print(a_text, b_choice)
"""

"""
### Default Values ###

Define a simple function greet() that takes one argument "name". The function should print a greeting for the entered 
name. Ask the user for his/her name and execute the greet function, passing the name as an argument.
If nothing was entered, use a default value for the name to greet "Unknown".

Hint: An empty string is still a value you can pass, be careful :-)

Example:
    Please enter your name: >> René
    Hello René!
    Please enter your name: >> 
    Hello Unknown!
"""


# Write your solution here
def greet(name):
    print("Hello " + name + "!")


user_name = input("Please enter your name: >> ")
if user_name == "":
    user_name = "Unknown"

greet(user_name)
