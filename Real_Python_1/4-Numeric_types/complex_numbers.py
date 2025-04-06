#Complex numbers

#using complex function
imaginary_num = complex(3, 2)
print(f"{imaginary_num} is a {type(imaginary_num)}") #j in output is the imaginary unit

#using complex number literal j to the imaginary part
z = 5 + 2j
print(z.real)
print(z.imag)
print(z.conjugate())

x = 7j - 3
print(x.conjugate())

z1 = 3 + 2j
z2 = 2 + 3j
mass = z1 + z2
mass_of_z = z1 * z2
net_mass = z1 / z2

print(mass)
print(mass_of_z)
print(net_mass)