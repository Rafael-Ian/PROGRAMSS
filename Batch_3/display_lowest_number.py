#Program 4: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number
numbers = []

while True:
    try:
        numbers.append(float(input("Enter number")))
    except:
        break

print("Lowest number: ", min(numbers) if numbers else "No numbers entered")