#Program 6: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
numbers = []
for i in range(10):
    numbers.append(int(input(f"Enter number {i+1}: ")))

result = numbers[0]
for num in numbers[1:]:
    result -= num

print(result)