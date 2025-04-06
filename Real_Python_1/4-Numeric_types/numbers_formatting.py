#Number formatting usinf formateed string literal

'''adding a string to a number
    pricing, measurements, time, currency
'''

#format() function
length = format(2234E-6, ".6f")
print(f"{length}micron")

#f"" formatted string
def convert_to_usd(euro):
    usd = float(euro / 1.10)
    return f"${format(usd, ".2f")}"

print(convert_to_usd(5.25))

#f"" formatted string with args: decimal places
def convert_to_kg(grams):
    kg = float(grams / 1000)
    return f"{kg:.3f}kgs"

print(convert_to_kg(3335.67))

#f"" formatted string with args: thousand
def convert_to_metres(cm):
    metre = float(cm / 100)
    return f"{metre:,.2f} m"

print(convert_to_metres(122334.6))

#f"" formatted string with args: percentage
def convert_to_percentage(ratio):
    return f"{ratio:.2%}"

print(convert_to_percentage(0.546666))
