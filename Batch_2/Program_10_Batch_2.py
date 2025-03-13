#Program 10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start + 1, end):
    print(num)