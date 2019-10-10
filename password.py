#!/bin/python3
username = 'surender'
password = 'Password'

userinput = input("Please enter your username")
if userinput == username:
    a=input(" kindly provide Password?")
    if a == password:
        print("welcome to python world!")
    else:
        print ("That is worong password")
else:
        print ("This is wwrong username")
