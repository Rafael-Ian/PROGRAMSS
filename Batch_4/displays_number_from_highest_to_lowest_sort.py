#Program 4: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function
numbers = []

while True:
    try:
        numbers.append(float(input("Enter number: ")))
    except:
        break
#Displays numbers in descending order
print("Numbers sorted from highest to lowest: ", sorted(numbers, reverse=True) if numbers else "No numbers were entered.")
