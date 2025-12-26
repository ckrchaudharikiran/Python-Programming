decimal = int(input("Enter the number: "))

binary = bin(decimal)[2:]      # remove "0b"
octal = oct(decimal)[2:]       # remove "0o"
hexadecimal = hex(decimal)[2:].upper()  # remove "0x" and make uppercase

print(f"Binary for {decimal} is {binary}")
print(f"Octal for {decimal} is {octal}")
print(f"Hexadecimal for {decimal} is {hexadecimal}")

