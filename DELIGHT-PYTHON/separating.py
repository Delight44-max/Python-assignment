number = int(input("Enter a five-digit integer: "))


divisors = [10000, 1000, 100, 10, 1]

for d in divisors:
    digit = number // d
    print(digit, end=' ')
    number %= d  