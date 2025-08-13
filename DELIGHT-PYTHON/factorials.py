Userinput = int(input("Enter a nonnegative integer: "))

if Userinput < 0:
    print("Sorry, factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, Userinput + 1):
        factorial *= i
    print(f"{Userinput}! = {factorial}")