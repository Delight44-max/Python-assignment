Userinput = int(input("Enter a nonnegative integer: "))


factorial = 1


for i in range(1, Userinput + 1):
    factorial *= i

print(f"{Userinput}! = {factorial}")