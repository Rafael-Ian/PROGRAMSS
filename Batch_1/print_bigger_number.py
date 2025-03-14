#Program 1: Create a program that ask user to input 2 numbers. Print the bigger number.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print("The bigger number is: ", num1)
elif num1 < num2:
    print("The bigger number is: ", num2)
else:
    print("The numbers are equal.")
