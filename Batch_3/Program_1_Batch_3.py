#Program 1: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
numbers = [] #stores inputs

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

#Finds non-duplicates
non_duplicates = [value for value in numbers if numbers.count(value) == 1]
print(non_duplicates)