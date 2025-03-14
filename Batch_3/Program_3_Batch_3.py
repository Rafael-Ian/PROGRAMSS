#Program 3: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.
first_entries = set()

while True:
    number_input = input("Enter a number: ")

    if not number_input.replace('.', '', 1).replace('-', '', 1).isdigit():
        print("Wrong input. Exiting program")
        break

    if number_input in first_entries:
        print("Duplicate")
    else:
        print("Unique")
        first_entries.add(number_input)
        