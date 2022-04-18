with open('test.txt') as textFile:
    print( textFile.readlines(7) )

with open('google.png', 'br') as binFile:
    print( binFile.readlines(21) )
