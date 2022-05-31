myint = 255
mybites = b'lskdjf'
mybites2 = b'\xff\x00'
mybites3 = bytes('ááááééóöüúő', 'utf-8', 'ERROR')

mybites4 = bytes.fromhex('00 fa c8 55 11   ')

# print( mybites2 )
# print( mybites2[1] )
# print( mybites.hex('-', 2) )


mybitesX = bytes(mybites2)

print( mybitesX )
print( mybites2 )

del mybites2
print( mybitesX )