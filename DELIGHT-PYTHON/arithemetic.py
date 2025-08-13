numbers = []


for i in range(4):
    num = int(input(f"Enter integer {i + 1}: "))
    numbers.append(num)


total = sum(numbers)
average = total / len(numbers)
product = 1
for num in numbers:
    product *= num

smallest = min(numbers)
largest = max(numbers)


print(f"Sum: {total}")
print(f"Average: {average}")
print(f"Product: {product}")
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")