
# Q1. Write a Python program to demonstrate that Lists are mutable by updating an existing element.

colors = ["Red", "Green", "Blue"]

print("Original List:", colors)

colors[1] = "Yellow"

print("Modified List:", colors)


# Q2. Write a Python program to demonstrate that Tuples are immutable.

student = ("Rahul", 20, "Mumbai")

print("Original Tuple:", student)

try:
    student[1] = 25
except TypeError as e:
    print("TypeError:", e)


# Q3. Write a Python program to swap two numbers using Tuple Assignment.

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("Before Swapping")
print("a =", a)
print("b =", b)

a, b = b, a

print("After Swapping")
print("a =", a)
print("b =", b)


# Q4. Write a Python program to unpack a Tuple into individual variables.

student = ("Amit", 21, "Mumbai")

name, age, city = student

print("Name :", name)
print("Age :", age)
print("City :", city)


# Q5. Write a Python program to calculate the sum of any number of values using Variable-Length Arguments (*args).

def addition(*numbers):
    total = 0

    for i in numbers:
        total += i

    print("Sum =", total)

addition(10, 20)
addition(10, 20, 30)
addition(10, 20, 30, 40)


# Q6. Write a Python program to create a Dictionary containing student information and display all key-value pairs.

student = {
    "Roll": 101,
    "Name": "Rahul",
    "Course": "B.Sc.IT",
    "Marks": 88
}

for key, value in student.items():
    print(key, ":", value)


# Q7. Write a Python program to update and delete elements from a Dictionary.

employee = {
    "ID": 101,
    "Name": "Amit",
    "Salary": 35000
}

print("Original Dictionary")
print(employee)

employee["Salary"] = 45000
employee["Department"] = "IT"

del employee["ID"]

print("\nUpdated Dictionary")
print(employee)


# Q8. Write a Python program to count the frequency of each character in a given string using a Dictionary.

text = input("Enter a String: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print(frequency)


# Q9. Write a Python program to merge two Dictionaries.

student1 = {
    "Name": "Rahul",
    "Age": 20
}

student2 = {
    "City": "Mumbai",
    "Marks": 90
}

student1.update(student2)

print(student1)


# Q10. Write a Python program to store the marks of five students in a Dictionary and display the topper.

marks = {
    "Rahul": 80,
    "Amit": 92,
    "Riya": 87,
    "Neha": 95,
    "Soham": 78
}

topper = max(marks, key=marks.get)

print("Topper :", topper)
print("Marks :", marks[topper])


# Q11. Write a Python program to find the maximum and minimum elements in a List.

numbers = [25, 10, 80, 45, 67]

print("Maximum =", max(numbers))
print("Minimum =", min(numbers))


# Q12. Write a Python program to remove duplicate elements from a List.

numbers = [10, 20, 30, 10, 20, 40, 50]

unique = []

for item in numbers:
    if item not in unique:
        unique.append(item)

print(unique)


# Q13. Write a Python program to reverse a Tuple.

t = (10, 20, 30, 40, 50)

print(tuple(reversed(t)))


# Q14. Write a Python program to sort a Dictionary by its keys.

student = {
    "B": 85,
    "A": 90,
    "D": 70,
    "C": 80
}

for key in sorted(student):
    print(key, ":", student[key])


# Q15. Write a Python program to find whether a given key exists in a Dictionary.

student = {
    "Name": "Rahul",
    "Age": 20,
    "City": "Mumbai"
}

key = input("Enter Key: ")

if key in student:
    print("Key Found")
else:
    print("Key Not Found")
