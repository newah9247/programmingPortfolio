"""
Program: Modular Grading Average Program
Author: Noah Taylor
Date: November 28th 2022
Filename: modularGradingAverageProgram.py
Purpose: Grading Purposes
"""
#Select class you want to get grades for
def getGrades(grade):
    grade = int(input("Please input your grade: "))
    if grade >= 90:
        print("A")
    elif grade >=80:
        print("B")
    elif grade >=70:
        print("C")
    elif grade >=60:
        print("D")
    else:
        print("Fail")
    menu()
    
#Validates Grades
def validateGrade(grades):
    if grades > 100 or grades < 0:
        print("one or more of the grades you entered is wrong please try again")
        getGrades()
        menu()
        
#Displays grades
def displayResults():
    getGrades()
    validateGrade()
    menu()

#Calculates your average grades   
def calculateAvg ():
    #first number
    num1 = float(input("Please input your first number: "))
    #second number
    num2 = float(input("Please input your second number: "))

    # calculate average of those numbers
    avg = (num1 + num2) / 2

    # print average value
    print('The average of numbers = %0.2f' %avg)
    


#Startup menu, select an option
def menu():
    print("[1] Display Instructions")
    print("[2] Get Grades")
    print("[3] Validate Grades")
    print("[4] Display Results")
    print("[5] Calculate Average")
    
menu()
option = int(input("Enter what you would like to do, if you would like to terminate the program please input 6!: "))

#Option Selector
while option != 0:
    if option == 1:
        print("The Instructions for this assignment are to create a modular grading program.")
        break
        menu()
    
    elif option == 2:
        getGrades()
        break
        menu()
    
    elif option == 3:
        validateGrade()
        break
        menu()
    
    elif option == 4:
        displayResults()
        break
        menu()
    
    elif option == 5:
        calculateAvg()
        break
        menu()
        
    elif option == 6:
        print("Thank you for using this program, Goodbye.")
    
    else:
        print("Invalid Option")
        break
        
#Loop, enter option afterwards
print()
menu()
option = int(input("Enter your option: "))