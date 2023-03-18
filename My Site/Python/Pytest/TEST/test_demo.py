some_word = 'test'
# test := 'x'         # // -! not allowed

if (word_len := len(some_word)) > 1:
    print( f'word has {word_len} characters')   # // -> 'word has 4 characters

def generate_numbers():
    for i in range(1, 51):
        yield i

if (num := next((n for n in generate_numbers() if n % 2 == 0 and n % 3 == 0), None)):
    print(num)
