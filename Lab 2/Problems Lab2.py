## Problem 1: Course Marks

marks = [75, 82, 68, 91, 45]

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)
passed = sum(1 for mark in marks if mark >= 50)

print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Passed Courses:", passed)



## Problem 2: Weekend Temperatures

temperatures = (28, 30, 27, 31, 29, 32)

for i, temperature in enumerate(temperatures):
    if i < 3:
        day = "Saturday"
    else:
        day = "Sunday"

    print(day, "Temperature:", temperature)

print("Highest Temperature:", max(temperatures))
print("Lowest Temperature:", min(temperatures))



## Problem 3: Word Analyzer

text = input("Enter a word or short sentence: ")

vowels = 0
spaces = 0

for character in text:
    if character.lower() in "aeiou":
        vowels += 1

    if character == " ":
        spaces += 1

print("Number of Characters:", len(text))
print("Number of Vowels:", vowels)
print("Number of Spaces:", spaces)



## Problem 4: Grade Calculator

def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    return grade


marks = [85, 78, 90, 72, 80]

average = sum(marks) / len(marks)
grade = calculate_grade(marks)

print("Marks:", marks)
print("Average:", average)
print("Grade:", grade)



## Problem 5: Shopping Cart Processor

products = [
    {"name": "Laptop", "price": 60000, "quantity": 1},
    {"name": "Mouse", "price": 650, "quantity": 2},
    {"name": "Keyboard", "price": 1200, "quantity": 1},
    {"name": "USB Drive", "price": 850, "quantity": 2}
]


def apply_discount(total):
    if total >= 2000:
        return total * 0.90
    return total


total = 0

for product in products:
    line_total = product["price"] * product["quantity"]
    total += line_total
    print(product["name"], "Total:", line_total)

discounted_total = apply_discount(total)

print("Original Total:", total)

if total >= 2000:
    print("Discount:", total * 0.10)
else:
    print("Discount:", 0)

print("Final Total:", discounted_total)



## Problem 6: Countdown

number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Please enter a non-negative integer.")
else:
    while number >= 0:
        print(number)
        number -= 1



## Problem 7: Student Record Analyzer

students = [
    {"name": "Rahim", "department": "CSE", "marks": 85, "attendance": 92},
    {"name": "Karim", "department": "CSE", "marks": 48, "attendance": 76},
    {"name": "Sara", "department": "DS", "marks": 91, "attendance": 95},
    {"name": "Nadia", "department": "DS", "marks": 67, "attendance": 84},
    {"name": "Hasan", "department": "CSE", "marks": 73, "attendance": 78}
]

total_marks = 0
passed_students = 0
highest_student = students[0]

for student in students:
    print("Name:", student["name"], "| Marks:", student["marks"])

    total_marks += student["marks"]

    if student["marks"] >= 50:
        passed_students += 1

    if student["marks"] > highest_student["marks"]:
        highest_student = student

average = total_marks / len(students)

print("Passed Students:", passed_students)
print("Class Average:", average)
print("Highest Scorer:", highest_student["name"])
print("Highest Mark:", highest_student["marks"])



## Problem 8: Product Inventory Summary

products = [
    {"name": "Notebook", "price": 120, "quantity": 3},
    {"name": "Pen", "price": 20, "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse", "price": 650, "quantity": 1}
]

total_inventory_value = 0
highest_product = None
highest_line_total = 0

for product in products:
    line_total = product["price"] * product["quantity"]
    total_inventory_value += line_total

    print("Product:", product["name"])
    print("Price:", product["price"])
    print("Quantity:", product["quantity"])
    print("Line Total:", line_total)
    print()

    if line_total > highest_line_total:
        highest_line_total = line_total
        highest_product = product["name"]

print("Total Inventory Value:", total_inventory_value)
print("Product with Highest Line Total:", highest_product)
print("Highest Line Total:", highest_line_total)