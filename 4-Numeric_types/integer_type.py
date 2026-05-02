#Integer types
''' Integer literals
    Decimal: 42
    Binary: 0b101010, 
    Hexadecimal: 0x2a, 
    Octal: 0o52
'''
list = [55, 2, 1.618, 0.003, -42, '42', 0b101010, 0x2a, 0o52]

for num in list:
    print(f"{num}, is a {type(num)}")


#Integer built-in function int()
print(int())
string = '42'
print(int(string))
float = 3.99
print(int(float))