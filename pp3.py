
# Program 1: Create and Access List Elements

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Complete List:", fruits)
print("First Element:", fruits[0])
print("Last Element:", fruits[-1])


# Program 2: Traverse a List

numbers = [10, 20, 30, 40, 50]

print("Elements are:")
for item in numbers:
    print(item)


# Program 3: Update and Delete List Elements

students = ["Ram", "Shyam", "Rita", "Amit"]

print("Original List")
print(students)

students[1] = "Suresh"

print("After Update")
print(students)

del students[2]

print("After Delete")
print(students)


# Program 4: List Methods

numbers = [5, 2, 8, 1]

numbers.append(10)
numbers.insert(2, 100)
numbers.remove(8)
numbers.sort()

print(numbers)


# Program 5: List Operators

list1 = [1, 2, 3]
list2 = [4, 5]

print("Concatenation:", list1 + list2)
print("Repetition:", list1 * 3)
print(2 in list1)
print(10 in list1)


# Program 6: Create and Access Tuple

student = ("Rahul", 20, "Mumbai")

print(student)
print("Name:", student[0])
print("Age:", student[1])
print("City:", student[2])


# Program 7: Tuple Operators

t1 = (10, 20, 30)
t2 = (40, 50)

print("Concatenation:", t1 + t2)
print("Repetition:", t1 * 2)
print(20 in t1)
print(len(t1))


# Program 8: Traverse Tuple

colors = ("Red", "Green", "Blue")

for color in colors:
    print(color)


# Program 9: Dictionary Creation, Access and Update

student = {
    "Roll": 101,
    "Name": "Amit",
    "Marks": 88
}

print(student)
print(student["Name"])

student["Marks"] = 95

print(student)


# Program 10: Dictionary Methods

student = {
    "Roll": 101,
    "Name": "Amit",
    "Marks": 90
}

student["City"] = "Mumbai"

print(student)

del student["Roll"]

print(student)
print(student.keys())
print(student.values())
print(student.items())


# Program 11: Traverse Dictionary

student = {
    "Name": "Rahul",
    "Age": 20,
    "City": "Mumbai"
}

for key, value in student.items():
    print(key, "=", value)


# Program 12: Membership Operator

student = {
    "Name": "Rahul",
    "Age": 20
}

print("Name" in student)
print("Marks" in student)
