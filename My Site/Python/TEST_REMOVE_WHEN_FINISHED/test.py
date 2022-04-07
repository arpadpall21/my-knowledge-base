myInt = 256
myInt2 = -255

print(
    # myInt.to_bytes(1, byteorder='big', signed=False)        # OverflowError 
)

print(
    myInt.to_bytes(2, byteorder='big', signed=False)   
)

print(
    myInt2.to_bytes(1, byteorder='big', signed=True)   
)

