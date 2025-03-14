#Program 1: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
numbers = [float(input(f"Enter number {i+1}: ")) for i in range(10)]

duplicates = {num for num in numbers if numbers.count(num) > 1}
#Displays duplicate numbers
print("Numbers with duplicate: ", list(duplicates) if duplicates else "No duplicate numbers found.")