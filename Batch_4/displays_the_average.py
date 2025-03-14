#Program 5: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.
numbers = []

while True:
    try:
        numbers.append(float(input("Enter number: ")))
    except:
        break
#Calculates and displays the average
print("Average: ", sum(numbers) / len(numbers) if numbers else "No numbers were entered.")