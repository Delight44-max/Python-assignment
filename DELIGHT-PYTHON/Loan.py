principal = int(input("Enter the ammount you want to borrow"))
annual_interest = float(input("Enter interest rate"))
duration = float(input("Enter duration"))
MONTH_IN_YEARS = 12
NUMBER_OF_YEARS = duration * MONTH_IN_YEARS
PERCENTAGE = 100
rate = annual_interest / (PERCENTAGE * MONTH_IN_YEARS)
monthly_Payment = principal * (rate * ( 1 + rate )) ** NUMBER_OF_YEARS / ( 1 + rate ) ** NUMBER_OF_YEARS - 1
print("Monthly payment is", monthly_Payment)

