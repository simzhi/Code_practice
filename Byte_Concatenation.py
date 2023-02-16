# Byte Concatenation:
# Write a Python function that takes two byte arrays 
# and concatenates them into a single byte array.

# Function to concatenate byte arrays
def concat_bytes(b1, b2):
    return b1 + b2

print(concat_bytes([1,2,3,4],[5,8,9]))

# Bit-wise operations:
# Write a Python function that takes two integers and performs a bitwise OR operation on them.

def bitwiseOR(x, y):
    return x | y
print(bitwiseOR(4, 5))

def bitwiseAND(x, y):
    return x & y
print(bitwiseAND(4, 5))

def bitwiseXOR(x, y):
    return x ^ y
print(bitwiseXOR(156, 52))

def bitwiseNOT(x):
    return ~x & 255
print(bitwiseNOT(156))
print(bitwiseNOT(8))

print((8).bit_length())
print((555).bit_count())
