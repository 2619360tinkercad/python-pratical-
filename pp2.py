
# A) if, if-else, if-elif-else

# Program 1: Check Whether Number is Positive

num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")


# Program 2: Check Even or Odd (if-else)

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# Program 3: Find Greatest of Three Numbers (if-elif-else)

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a >= b and a >= c:
    print("A is Greatest")
elif b >= a and b >= c:
    print("B is Greatest")
else:
    print("C is Greatest")


# B) for and while Loop

# Program 4: Print Numbers from 1 to 10 using for Loop

for i in range(1, 11):
    print(i)


# Program 5: Display Multiplication Table using for Loop

num = int(input("Enter a Number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# Program 6: Print Numbers from 1 to 10 using while Loop

i = 1

while i <= 10:
    print(i)
    i += 1


# Program 7: Sum of First N Natural Numbers

n = int(input("Enter Value of N: "))

i = 1
total = 0

while i <= n:
    total += i
    i += 1

print("Sum =", total)


# C) break, continue, pass

# Program 8: Demonstration of break

for i in range(1, 11):
    if i == 6:
        break
    print(i)


# Program 9: Demonstration of continue

for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# Program 10: Demonstration of pass

for i in range(1, 6):
    if i == 3:
        pass
    print(i)
