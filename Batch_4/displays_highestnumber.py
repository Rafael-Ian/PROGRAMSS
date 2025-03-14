#Program 3: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number.
numbers = []

while True:
    try:
        numbers.append(float(input("Enter number: ")))
    except:
        break

print("Highest number: ", max(numbers) if numbers else "No valid numbers were entered.")