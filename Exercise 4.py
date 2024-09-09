#initalize variables
principal = int(input("Enter the principal amount: "))
rate_of_interest = (int(input("Enter the interest rate (%): ")))/100
time_period = int(input("Enter the amount of months: "))

#calculate interest
interest_amount = principal*rate_of_interest*time_period

#print info
print(f"Starting at ${principal}, with a monthly interest rate of {rate_of_interest * 100}%, ${interest_amount} will accrue over a period of {time_period} months.\nThat all totals to ${principal + interest_amount}.")
