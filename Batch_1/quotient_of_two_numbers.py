#Program 5: Create a program that ask user to input two numbers. Print the quotient of the two number with the decimal point.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num2 != 0:
    quotient = num1 / num2
    print("Quotient: ", quotient)
else:
    print("Can't be divided by zero.")