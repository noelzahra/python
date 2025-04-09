# Function to check contact number len
# press return twice to complete and exit function after return

def call_number(input_number) -> int:
    ''' A function to check mobile contact number len is 8 digits.'''
    contact_str = str(input_number)
    if len(contact_str) == 8:
        print(f"{input_number} is correct format")
        return (input_number)
    else:
        print(f"{input_number} is wrong format. Please check number again")

help(call_number)

call_number(79798002)

new_contact = call_number(99667788)
wrong_format_contact = call_number(9922883377)
