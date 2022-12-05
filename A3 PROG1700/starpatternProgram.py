"""
Program: Star Pattern Program
Author: Noah Taylor
Date: November 28th 2022
Filename: starpatternProgram.py
Purpose: Create patterns out of the * character
"""

def menu():
    print("[1] Square Pattern")
    print("[2] Triangle Pattern")


menu()
option = int(input("Which pattern would you like?: "))
    
    
    
while option != 0:
    if option == 1:
        num = int(input("Input a number between 1-10: "))
    print("Star Pattern Square") 
    for i in range(num):
        for i in range(num):
            print('*', end = '  ')
        print()
        
    else: option == 2
    rows = int(input("Enter number of rows: "))
    for i in range(rows, 0, -1):
        for j in range(0, i):
            print("* ", end=" ")
    print()
    
