#Program 2: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.
numbers = []

while True:
    try:
        numbers.append(float(input("Enter number: ")))
    except:
        break
#Proceeds if at least one valid number was entered
if numbers:
    unique_numbers = set(numbers)
    most_common = max(unique_numbers, key=numbers.count) #Finds the number with highest count
    print("Number with the most duplicates: ", most_common)
else:
    print("No valid numbers were entered.")