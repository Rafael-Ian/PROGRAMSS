#Program 7: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
sum = 0

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    sum += num

print("Sum of all the numbers: ", sum)