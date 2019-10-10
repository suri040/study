#!/bin/python3
mydict ={'surender': [1234,'surender.kumar',5000] , 'rakesh': [4321,'rakesh.kumar',5000]}
search_username = input("Enter your username: ")
if search_username in mydict:
    a= int(input("Kindly provide your password : "))
    if a in mydict:
         print([(a, mydict[a] for a in mydict])
    else:
        print ("Password is not correct")
else:
    print ("Username is nor correct")
