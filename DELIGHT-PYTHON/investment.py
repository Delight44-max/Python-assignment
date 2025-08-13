principal = 1000
rate = 0.07


print("Year\tAmount on Deposit")


for year in range(1, 31):
    amount = principal * (1 + rate) ** year
    print(f"{year}\t{amount:.2f}")