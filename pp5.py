
# Part A: File Handling

# Q1. Write a Python program to create a text file and write data into it.

file = open("student.txt", "w")
file.write("Name: Rahul\n")
file.write("Course: B.Sc. CA\n")
file.write("City: Mumbai\n")
file.close()

print("Data written successfully.")


# Q2. Write a Python program to read and display the contents of a text file.

file = open("student.txt", "r")
data = file.read()

print("File Contents:")
print(data)

file.close()


# Q3. Write a Python program to append new data to an existing text file.

file = open("student.txt", "a")
file.write("Marks: 85\n")
file.close()

print("Data appended successfully.")


# Q4. Write a Python program to read a text file line by line.

file = open("student.txt", "r")

for line in file:
    print(line, end="")

file.close()


# Q5. Write a Python program to demonstrate read(), readline(), and readlines() methods.

file = open("student.txt", "r")

print("Using read():")
print(file.read())

file.close()

file = open("student.txt", "r")

print("\nUsing readline():")
print(file.readline())

file.close()

file = open("student.txt", "r")

print("\nUsing readlines():")
print(file.readlines())

file.close()


# Q6. Write a Python program to copy the contents of one text file into another text file.

source = open("student.txt", "r")
destination = open("copy.txt", "w")

data = source.read()
destination.write(data)

source.close()
destination.close()

print("File copied successfully.")


# Q7. Write a Python program to count the number of lines, words, and characters in a text file.

file = open("student.txt", "r")
data = file.read()

lines = data.splitlines()
words = data.split()
characters = len(data)

print("Number of Lines:", len(lines))
print("Number of Words:", len(words))
print("Number of Characters:", characters)

file.close()


# Q8. Write a Python program to explore various attributes of a file object.

file = open("student.txt", "r")

print("File Name:", file.name)
print("File Mode:", file.mode)
print("Is File Closed?", file.closed)

file.close()

print("Is File Closed?", file.closed)


# Q9. Write a Python program to demonstrate the use of tell() and seek() methods.

file = open("student.txt", "r")

print("Initial Position:", file.tell())

data = file.read(5)

print("Data Read:", data)
print("Current Position:", file.tell())

file.seek(0)

print("Position after seek:", file.tell())

file.close()


# Part B: Directory Operations

# Q10. Write a Python program to display the current working directory.

import os

current_directory = os.getcwd()

print("Current Working Directory:")
print(current_directory)


# Q11. Write a Python program to create a new directory.

import os

if not os.path.exists("MyFolder"):
    os.mkdir("MyFolder")
    print("Directory created successfully.")
else:
    print("Directory already exists.")


# Q12. Write a Python program to display all files and folders present in the current directory.

import os

items = os.listdir()

print("Files and Directories:")

for item in items:
    print(item)


# Q13. Write a Python program to check whether a specified file exists.

import os

filename = input("Enter File Name: ")

if os.path.isfile(filename):
    print("File exists.")
else:
    print("File does not exist.")


# Part C: Built-in Exception Handling

# Q14. Handle division by zero.

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")


# Q15. Handle invalid input using ValueError.

try:
    age = int(input("Enter Age: "))
    print("Age:", age)
except ValueError:
    print("Invalid input")


# Q16. Handle multiple built-in exceptions.

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")


# Q17. Demonstrate try, except, else and finally.

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    result = a / b
except (ZeroDivisionError, ValueError):
    print("Error occurred")
else:
    print("Result:", result)
finally:
    print("Program completed")


# Part D: File Handling with Exceptions

# Q18. Handle FileNotFoundError.

try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")


# Q19. Safely read a text file using exception handling.

try:
    with open(input("Enter File Name: "), "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
finally:
    print("File operation completed")


# Part E: User-Defined Exceptions

# Q20. Create a user-defined exception for validating age.

class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter Age: "))
    if age < 18:
        raise InvalidAgeError
    print("Eligible")
except InvalidAgeError:
    print("Age must be 18 or above")


# Q21. Demonstrate user-defined exception with arguments.

class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age

try:
    age = int(input("Enter Age: "))
    if age < 18:
        raise InvalidAgeError(age)
    print("Valid Age:", age)
except InvalidAgeError as e:
    print("Invalid Age:", e.age)


# Q22. Create a user-defined exception for insufficient bank balance.

class InsufficientBalanceError(Exception):
    pass

try:
    balance = 5000
    amount = int(input("Enter Amount: "))
    if amount > balance:
        raise InsufficientBalanceError
    print("Remaining Balance:", balance - amount)
except InsufficientBalanceError:
    print("Insufficient Balance")
