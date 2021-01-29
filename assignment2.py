"""
Created on 01/07/21

Program to Assignment #2

@author: Michelle Medina
"""
# List Variables 
tuition1 = 0
tuition2 = 0
tuition3 = 0
tuition4 = 0

increase = 0
totalTuition=0.0

# The user will enter their starting tuition for year one
tuition1 = int(input("Enter year 1 tuition price: "))
# The user also enters the annual increase of the tuition in a fraction format For example, 0.05 (for 5% increase)
increase = float(input("Enter annual increase %: "))

# This increase is applied for years 2, 3 and 4.
tuition2 = (tuition1 * increase) + tuition1
tuition3 = (tuition2 * increase) + tuition2
tuition4 = (tuition3 * increase) + tuition3

totalTuition = tuition1 + tuition2 + tuition3 + tuition4

# The program then outputs the tuition for each year, and the total tuition for all four years.
print("Tuition year 1 is", tuition1)
print("Tuition year 2 is", tuition2)
print("Tuition year 3 is", tuition3)
print("Tuition year 4 is", tuition4)
print("Your total tuition is ", totalTuition)
