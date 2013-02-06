#!/usr/bin/python -tt

import sys
import os

# Main
def main():
    
    print "What would you like to do? \n"

    print "1: Multiplication"
    print "2: Division"
    print "3: Addition"
    print "4: Subtraction"
    print "5: Exit"
    
    choice = raw_input()
    
    if choice == "1":
        a = input("Please enter first number:")
        b = input("Please enter second number:")
        print "The answer is:"
        print multi(a, b)
    elif choice == "2":
        a = input("Please enter first number:")
        b = input("Please enter second number:")
        print "The answer is:"
        print divid(a, b)
    elif choice == "3":
        a = input("Please enter first number:")
        b = input("Please enter second number:")
        print "The answer is:"
        print addit(a, b)
    elif choice == "4":
        a = input("Please enter first number:")
        b = input("Please enter second number:")
        print "The answer is:"
        print subtr(a, b)
    elif choice == "5":
        exit()
    else:
        print "Please enter a number between 1-5"
        main()

def convertString(string):
    try:
        returnValue = int(string)
    except ValueError:
        returnValue = float(string)
    return returnValue

def cls():
    os.system(['clear','cls'][os.name == 'nt'])
    
def multi(a, b):  
    return convertString(a) * convertString(b)

def divid(a, b):
    return convertString(a) / convertString(b)

   
def addit(a, b):
    return convertString(a) + convertString(b)

def subtr(a, b):
    return convertString(a) - convertString(b)

# Boilerplate

if __name__ == '__main__':
    main()
