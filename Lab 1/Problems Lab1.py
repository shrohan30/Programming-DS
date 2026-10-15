## Problem 1: Basic Arithmetic

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

if b != 0:
    print("Quotient:", a / b)
else:
    print("Quotient: Undefined (division by zero)")


## Problem 2: Student Profile

name = input("Enter student name: ")
student_id = input("Enter student ID: ")
age = int(input("Enter age: "))
department = input("Enter department: ")
cgpa = float(input("Enter CGPA: "))

print("\n----- Student Profile -----")
print("Name:", name)
print("Student ID:", student_id)
print("Age:", age)
print("Department:", department)
print("CGPA:", f"{cgpa:.2f}")


## Problem 3: Temperature Conversion

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print("Fahrenheit:", fahrenheit)
print("Kelvin:", kelvin)


## Problem 4: Student Marks Analysis

name = input("Enter student name: ")
marks = []

for i in range(5):
    mark = float(input(f"Enter mark for course {i + 1}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)
passed = sum(1 for mark in marks if mark >= 50)

print("\n----- Marks Report -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Passed Courses:", passed)