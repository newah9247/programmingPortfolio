"""
Program: Pennies for Pay 
Author: Noah Taylor
Date: November 28th 2022
Filename: penniesForPay.py
Purpose: Find how many pennies you get for the days you have worked
"""


#Asks the user to input the number of days that they have worked
days = int(input("Enter the number of days you have worked: "))
#Defines amounts for counter, penny and total
counter = 1
penny = 0.01
total = 0.01

#Makes a "table" by printing Day and Pay and formatting using spaces
print ("Days     Pay")
print(format(counter), "     ", penny)

#While loop causes additions to each defined function to increase amount of pennies for days worked
while counter < days:
    counter = counter + 1
    penny = penny * 2 
    total = total + penny
    
#Prints final dollar amount for how many days you have worked 
    print(format(counter), "     ", penny)
print ("Total  ", "$"(total))
