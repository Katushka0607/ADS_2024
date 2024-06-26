"""
Write a program which asks for two integer numbers.
The program should then print out whichever is greater.
If the numbers are equal, the program should print a different message.
Examples:
    Please type in the first number: >> 5
    Please type in another number: >> 3
    The greater number was: 5

    Please type in the first number: >> 5
    Please type in another number: >> 8
    The greater number was: 8

    Please type in the first number: >> 5
    Please type in another number: >> 5
    The numbers are equal!

"""
# Write your solution here

# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
#
# if number1 > number2:
#    print("The greater number is: " + str(number1))
# elif number1 < number2:
#    print("The greater number is: " + str(number2))
# else:
#    print("The numbers are equal.")

"""
Python comparison operators can also be used on strings. 
String a is smaller than string b if it comes alphabetically before b. Notice however that the comparison is only reliable if
- the characters compared are of the same case, i.e. both UPPERCASE or both lowercase
- only the standard English alphabet of a to z, or A to Z, is used.

Write a program which asks the user for two words. The program should then print out whichever of the two comes alphabetically last.

You can assume all words will be typed in lowercase entirely.

Examples:
Please type in the 1st word: >> car
Please type in the 2nd word: >> scooter
scooter comes alphabetically last.

Please type in the 1st word: >> zorro
Please type in the 2nd word: >> batman
zorro comes alphabetically last.

Please type in the 1st word: >> python
Please type in the 2nd word: >> python
You gave the same word twice.

"""
# Write your solution here

# word1 = input("Please use only lower case letters.\nType in the 1st word: ")
# word2 = input("Type in the 2nd word: ")
# if word1 > word2:
#    print(word1 + " comes alphabetically last.")
# elif word1 < word2:
#    print(word2 + " comes alphabetically last.")
# else:
#    print("You entered the same word twice.")

"""
Write a program which asks for the user's name. 
If the name is Huey, Dewey or Louie, the program should recognise the user as one of Donald Duck's nephews.
In a similar fashion, if the name is Morty or Ferdie, the program should recognise the user as one of Mickey Mouse's nephews.

Examples:
    Please type in your name: >> Morty
    I think you might be one of Mickey Mouse's nephews.
    
    Please type in your name: >> Huey
    I think you might be one of Donald Duck's nephews.
    
    Please type in your name: >> Ken
    You're not a nephew of any character I know of.
"""
# Write your solution here

# name = input("Please type in your name: ")
# if name == "Huey" or name == "Dewey" or name == "Louie":
#    print("I think you might be one of Donald Duck's nephews.")
# if name == "Morty" or name == "Ferdie":
#   print("I think you might be one of Mickey Mouse's nephews.")
# else:
#    print("You're not a nephew of any character I know of.")

"""
FizzBuzz
Write a program which asks the user for an integer number. 
If the number is divisible by three, the program should print out Fizz. 
If the number is divisible by five, the program should print out Buzz. 
If the number is divisible by both three and five, the program should print out FizzBuzz.

Examples:
    Number: >> 9
    Fizz
    
    Number: >> 7
    
    Number: >> 20
    Buzz
    
    Number: >> 45
    FizzBuzz
"""
# Write your solution here

# number = int(input("Please enter a whole number: "))
# if number % 3 == 0 and number % 5 == 0:
#    print("FizzBuzz")
# elif number % 5 == 0:
#    print("Buzz")
# elif number % 3 == 0:
#    print("Fizz")
# else:
#    print("The number is neither divisible by 3 nor by 5.")

"""
LeapYear
Generally, any year that is divisible by four is a leap year. 
However, if the year is additionally divisible by 100, it is a leap year only if it also divisible by 400.

Write a program which asks the user for a year, and then prints out whether that year is a leap year or not.

Examples:
    Please type in a year: >> 2011
    That year is not a leap year.
    
    Please type in a year: >> 2020
    That year is a leap year.
    
    Please type in a year: >> 1800
    That year is not a leap year.
"""
# Write your solution here

year = int(input("Please enter a year: "))
if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("That year is a leap year.")
elif year % 4 == 0 and year % 100 == 0:
    print("That year is NOT a leap year.")
elif year % 4 == 0:
    print("That year is a leap year.")
else:
    print("That year is NOT a leap year.")
