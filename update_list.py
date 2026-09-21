
#update the values 

letters=['a','b','c']

letters[0]='x'

matrix=[
    ['a','b','c'], #Row 0
    ['d','e','f'],#Row 1
    ['g','h','i']#Row 2
]

matrix[-1]=['x','y','z']
matrix[0][0]='-'
matrix[1][1]='-'
matrix[-1][-1]='-'
print(matrix)