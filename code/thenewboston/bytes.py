from struct import *

# stores as bytes data

packed_data = pack('iif', 6, 19, 4.73)
print(packed_data)

print(calcsize('i'))
print(calcsize('i'))
print(calcsize('iif'))

# To Get back bytes data back into the normal
original_data = unpack('iif', packed_data)
print(original_data)
