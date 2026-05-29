def binary_to_decimal(binary):
    decimal = 0
    for i, bit in enumerate(binary[::-1]):
        decimal += int(bit) * (2 ** i)
    return decimal

binary = input("Binary sonni kiriting: ")
print(binary_to_decimal(binary))
