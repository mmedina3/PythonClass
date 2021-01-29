"""
Created on 01/17/21

Program to Assignment #4

@author: Michelle Medina
"""

#1. Write the definition of a function that take one number, that represents a temperature in Fahrenheit and prints the equivalent temperature in degrees Celsius.

def convert_f():
    f = int(input("What is the weather in fahrenheit today?: "))
    #formula: (32°F − 32) × 5/9 = 0°C
    celsius= (f - 32) * 5/9

    print("The conversion to celsius is: ", float(celsius))

#2.Write the definition of another function that takes one number, that represents speed in miles/hour and prints the equivalent speed in meters/second.

def convert_MPH():
    mph = int(input("What is your speed in MPH? "))
    #formula: divide the speed value by 2.237
    speed = mph/2.237

    print("The MPH speed converted to meters/second is: ", float(speed))


#3 Write the definition of a function named main. It takes no input, hence empty parenthesis, and does the following:
def main():
    main_input = 0
# # - prints Enter 1 to convert Fahrenheit temperature to Celsius
    main_input = int(input(" Enter 1 to convert Fahrenheit temperature to Celsius \n OR \n Enter 2 to convert speed from miles per hour to meters per second \n"))

# -take the input, lets call this main input, and if it is 1, get one input then call the function of step 1 and pass it the input.
    if main_input == 1:
         convert_f()

# - if main input is 2, get one more input and call the function of step 2.
    elif main_input == 2:
         convert_MPH()

# - if main input is neither 1 or 2, print an error message.
    else:
         print("Sorry, please insert a valid number!")

#4 After you complete the definition of the function main, write a statement to call main.
main()