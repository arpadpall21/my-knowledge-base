with open('test2.txt', 'w') as f:
    f.write('Test')
    f.write('Test')
    f.write('Test')
    f.write('Test')
    
    f.seek(4)
    f.write('----')
