#Program 7: Create a program that ask user to input 10 numbers. Print how many are even numbers.
count_even = 0
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        count_even += 1

print(f"Number of even numbers: {count_even}")
