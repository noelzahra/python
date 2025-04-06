#Exponent function

prompt_base = input("Enter a base: ")
prompt_exponent = input("Enter an exponent: ")

def find_exponent(prompt_base, prompt_exponent):
    base = float(prompt_base)
    exponent = float(prompt_exponent)
    return base ** exponent

print(find_exponent(prompt_base, prompt_exponent))