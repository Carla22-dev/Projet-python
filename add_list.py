
# add item in the list 

# append() - just throw in the end 


# letters=['a','b','c']
# letters.append('d')
# letters.insert(0,'x') # isert the 'x' on the first 
# print(letters)

matrix=[
    ['a','b','c'], #Row 0
    ['d','e','f'],#Row 1
    ['g','h','i']#Row 2
] 
# matrix.append(['x','y','z'])

# print(matrix)
# matrix.insert(0,['x','y','z'] )
# print('This is the matrix after the function insert:', matrix)


matrix[1].append('x')# row 1
print(matrix)
matrix[0].insert(0,'z') #row 0
print(matrix)