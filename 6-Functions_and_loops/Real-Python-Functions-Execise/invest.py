def invest(amount, rate, years):
    for year in range(1, years + 1):
        interest = float(amount) * float(rate)
        amount = float(amount) + interest
        print(f"year {year}: ${amount:.2F}")        

# print(invest(100, 0.05, 4))
# print(invest(120.5, 0.05, 4))

investments = {
    2200.55 : 3,
    3100    : 4,
    1500.90 : 9,
    4200    : 5
}

interest_rate = 0.05

def calculate_amount(amount, rate, year):
    rate = float(interest_rate)
    interest = float(amount) * rate * year
    total_amount = amount + interest
    compound_interest = total_amount - amount
    return f"Year {year}: initial investment is ${amount:,}, matures to ${total_amount:,.2F}, after {2025 + year}.\nCompound interest accrued: ${compound_interest:,.2F}"

for investment in investments:
    #Access key 'investment' float to get the value: investments[investment]
    print(calculate_amount(investment, interest_rate, investments[investment]))
    