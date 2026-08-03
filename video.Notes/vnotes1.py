age = 38
print(age)
print(type(age))

height = 5.8
print(height)
print(type(height))

name = "Hello"
print(name)
print(type(name))

age = 38

# Check if age is greater than 30
if age > 30:
    print(True)
else:
    print(False)


number = 5
message = "Hello " + str(number)
print(message)
print(type(message))


x = 10
y = 20

# Basic arithmetic operations
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(21 / 5)
print(21 // 5)
print(10 % 5)
print(10 ** 2)


text1 = "Name"
text2 = "name"

print(text1 == text2)


voter_age = 20

if voter_age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")


user_age = int(input("Enter your age: "))

# Classify the user's age group
if user_age < 13:
    print("You are a child.")
elif user_age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")


num = int(input("Enter a number: "))

# Check whether the number is positive and even/odd
if num > 0:
    print("Positive number")

    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Number is zero or negative")


year = int(input("Enter a year: "))

# Leap year condition
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It's a leap year")
else:
    print("Not a leap year")


first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
choice = input("Enter operator (+, -, *, /): ")

# Perform the selected operation
if choice == "+":
    print("Result =", first + second)
elif choice == "-":
    print("Result =", first - second)
elif choice == "*":
    print("Result =", first * second)
elif choice == "/":
    if second != 0:
        print("Result =", first / second)
    else:
        print("Division by zero is not allowed")
else:
    print("Invalid operator")
    
age = int(input("Enter your age: "))

# Ticket price based on age
if 0 < age <= 100:
    if age < 5:
        print("Free")
    elif age < 12:
        print("₹10")
    elif age < 18:
        student = input("Are you a student? (yes/no): ")

        if student.lower() == "yes":
            print("₹12")
        else:
            print("₹15")
    elif age < 60:
        print("₹50")
    else:
        print("₹10")
else:
    print("Invalid age")
