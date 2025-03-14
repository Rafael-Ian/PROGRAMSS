#Program 5: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function
numbers = []

while True:
    try:
        numbers.append(float(input("Enter number: ")))
    except:
        break

print("Sorted numbers: ", sorted(numbers) if numbers else "No numbers are entered.")
