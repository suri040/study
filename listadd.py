#!/bin/python3
course=['linux','python','devops','core']
n = input("Please enter your course : ")
print(n)
if n in course:
        print( "n is matched")
else:
        course.append(n)
        print(course)
