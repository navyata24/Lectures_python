# 1.
n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    numbers.append(value)

print("List of elements:", numbers)
print("Greatest number:", max(numbers))
print("Smallest number:", min(numbers))

numbers.sort()
print("Minimum and Maximum are:", numbers[0], "and", numbers[-1])


# 2.
my_list = [1, 2, 3]

first = my_list[0]
my_list[0] = my_list[-1]
my_list[-1] = first

print("List after swapping first and last elements:", my_list)


# 3.
subjects = ("math", "java", "python", "physics", "chemistry")

for subject in subjects:
    print(subject)
