# Program to find the factorial of a number
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial of", num, "is", fact)


# Program to find the grade of a student
marks = int(input("Enter marks (0-100): "))

if 75 <= marks <= 100:
    grade = "distinction"
elif marks >= 60:
    grade = "first class"
elif marks >= 50:
    grade = "second class"
elif marks >= 35:
    grade = "pass"
elif marks >= 0:
    grade = "fail"
else:
    grade = "invalid input"

print("Grade:", grade)


# Program to find the greatest among three numbers
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

largest = max(x, y, z)

print("Largest number is:", largest)
print("Average of the numbers is:", (x + y + z) / 3)


# Train ticket discount
employee = input("Are you a railway employee? (yes/no): ")

if employee.lower() == "yes":
    discount = 30
else:
    age = int(input("Enter your age: "))

    if age < 18:
        discount = 20
    elif age > 60:
        discount = 25
    else:
        discount = 5

print("Eligible discount:", str(discount) + "%")


# Prime number check
num = int(input("Enter a number: "))

prime = True

if num < 2:
    prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

if prime:
    print(num, "is a Prime Number")
else:
    print(num, "is Not a Prime Number")


# Fibonacci series
terms = int(input("How many terms? "))

a, b = 0, 1

for i in range(terms):
    print(a, end=" ")
    a, b = b, a + b

print()


# Simple Calculator
print("----- Simple Calculator -----")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice: "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result:", num1 + num2)
elif choice == 2:
    print("Result:", num1 - num2)
elif choice == 3:
    print("Result:", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Division by zero is not allowed")
else:
    print("Invalid choice")

# List Programs
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])
print(fruits[-1])

numbers = [1, 2, 3]

numbers.append(4)
numbers.insert(1, 1.5)
numbers += [5, 6]

print(numbers)

items = ["A", "B", "C", "D", "E"]

items.remove("B")
last = items.pop()
first = items.pop(0)

print(items)


marks = [45, 89, 12, 76, 23]

print(max(marks))
print(min(marks))
print(sum(marks))
print(len(marks))


letters = ["d", "a", "c", "b"]

sorted_letters = sorted(letters)
print(sorted_letters)
letters.reverse()
print(letters)


nums = [1, 2, 3, 4, 5, 6]

square_list = [i * i for i in nums if i % 2 == 0]

print(square_list)


colors = ["red", "blue", "red", "green"]


if "blue" in colors:
    print("Blue is present")

print(colors.count("red"))
