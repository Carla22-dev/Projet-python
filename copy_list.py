
letters=['a','b','c']

letters_copy_shadow=letters.copy()# shadow copy 
letters_copy=letters
letters.pop()
print('Oringinal:', letters)
print('Copy: ', letters_copy)
print('Copy with shadow: ', letters_copy_shadow)



matrix=[['d','e','f'],
        ['a','z','i'],
        ['a','a','c']
]

matrix_copy=matrix.copy()
matrix.pop()

print("Original: ", matrix)
print('Copy:    ', matrix_copy)



