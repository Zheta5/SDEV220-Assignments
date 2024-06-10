#File Name:M02_Lab.py
#Author: Carlos Guillen
#Date: 06/09/2024
#Purpose: Create a program that test students qualification for Deans list or Honor Roll

print("Welcome to the Dean's List and Honor Roll Qualification Program")

i =1 
while i < 5:
    Student_Firstname = input("Please enter your first name: ")

    Student_Lastname = input("Please enter your last name: ")
    if Student_Lastname == "ZZZ":
     exit()
    else: 
       print("Hello", Student_Firstname, Student_Lastname)
       GPA= float(input("Please enter your GPA: "))
    if GPA >= 3.5:
        print("Congratulations, you have been accepted to the Dean's List")
    elif GPA > 3.25 or GPA < 3.5:
        print("You have been accepted to the Honor Roll")
i+=1

               
