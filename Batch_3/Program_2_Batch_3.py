#Program 2: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
seen = set()#Stores numbers that are encountered
result = []

for i in range(10):
    num = input("Enter number: ")
    if num not in seen:
        result.append(num)
        seen.add(num)

print("Filtered numbers: ", result)