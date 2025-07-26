number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

# Calculate sum
sum = number1 + number2 + number3
print("Sum:", sum)

# Calculate product
product = number1 * number2 * number3
print("Product:", product)

# Calculate average
average = sum / 3
print("Average:", average)

# Find largest and smallest
largest = number1
smallest = number1

if number2 >= largest:
    largest = number2
if number2 < smallest:
    smallest = number2

if number3 > largest:
    largest = number3
if number3 < smallest:
    smallest = number3

print("The largest is", largest)
print("The smallest is", smallest)