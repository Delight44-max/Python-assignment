price = float(input("Enter the purchase price (up to $1): "))

if 0 <= price <= 1:
    change = int(round((1 - price) * 100))  # convert change to cents

    print("Your change is:")

    # Calculate the number of coins
    quarters = change // 25
    change %= 25

    dimes = change // 10
    change %= 10

    nickels = change // 5
    change %= 5

    pennies = change

    if quarters > 0:
        print(f"{quarters} quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} penn{'ies' if pennies > 1 else 'y'}")
else:
    print("Please enter a valid price between $0.00 and $1.00.")