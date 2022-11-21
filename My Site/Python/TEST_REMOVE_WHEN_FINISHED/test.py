import re

def readMatrix(grid):
    collect = ''
    for rowIdx in range(len(grid[0])):
        for colIdx in range(len(grid)):
            collect += str(grid[colIdx][rowIdx])

    words = re.sub('[^A-Za-z]', ' ', collect)
    print( words )
    words = re.sub('\s+', ' ', words)

    print( words )

matrixGrid = [[ 7,  ' ',  3],
              ['T', 's', 'i'],
              ['h', '%', 'x'],
              ['i','  ', '#'],
              ['s', 'M', ' '],
              ['$', 'a', ' '],
              ['#', 't', '%'],
              ['i', 'r', '!']]


print( readMatrix(matrixGrid))     # -> 'cde'
