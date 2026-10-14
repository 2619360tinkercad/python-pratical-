
# Q1. Write a Python program to display "Hello World".

print("Hello World")


# Q2. Write a Python program to display your Name, Roll Number, and Class.

print("Name: Rahul Sharma")
print("Roll No: 25")
print("Class: FYBSc DS")


# Q3. Write a Python program to create variables of different data types and display their values and types.

name = "Rahul"
age = 18
percentage = 85.5
status = True

print(name, type(name))
print(age, type(age))
print(percentage, type(percentage))
print(status, type(status))


# Q4. Write a Python program to accept two numbers from the user and perform arithmetic operations.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)

if b != 0:
    print("Division =", a / b)
else:
    print("Division by zero is not allowed")


# Q5. Write a Python program to calculate the area of a rectangle.

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth
print("Area =", area)


# Q6. Write a Python program to calculate the area and circumference of a circle.

radius = float(input("Enter radius: "))

area = 3.14 * radius * radius
circumference = 2 * 3.14 * radius

print("Area =", area)
print("Circumference =", circumference)


# Q7. Write a Python program to convert temperature from Celsius to Fahrenheit.

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Fahrenheit =", fahrenheit)


# Q8. Write a Python program to swap two variables.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before Swap:", a, b)

a, b = b, a

print("After Swap:", a, b)


# Q9. Write a Python program to demonstrate type conversion.

num = "100"

print(type(num))

num = int(num)

print(type(num))
print(num + 50)


# Q10. Write a Python program to evaluate arithmetic expressions.

a = 10
b = 5

print(a + b)
print(a * b)
print(a / b)
print(a ** b)


# Q11. Write a Python program to demonstrate relational operators.

a = 10
b = 20

print(a > b)
print(a < b)
print(a == b)
print(a != b)


# Q12. Write a Python program to demonstrate logical operators.

a = 10

print(a > 5 and a < 20)
print(a > 20 or a < 20)
print(not(a > 5))


# Q13. Write a Python program to calculate simple interest.

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

si = (p * r * t) / 100

print("Simple Interest =", si)


# Q14. Write a Python program to calculate the average of three numbers.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

avg = (a + b + c) / 3

print("Average =", avg)


# Q15. Write a Python program to accept a student's name and marks in three subjects and calculate total and percentage.

name = input("Enter student name: ")

m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))

total = m1 + m2 + m3
percentage = (total / 300) * 100

print("Student Name =", name)
print("Total Marks =", total)
print("Percentage =", percentage)
