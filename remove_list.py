
# letters=['a','b','a']
# letters.remove('a')
# print(letters)
# #letters.clear()# clear all list 

# # pop()
# #remove the specificy position , but if you  
# # dont speficied the position it's gonna remove the last item 

# removed=letters.pop()
# print(letters)
# print("The item removed: " , removed)



matrix=[
    ['a','b','c'], #Row 0
    ['d','e','f'],#Row 1
    ['g','h','i']#Row 2
] 
matrix[1].remove('e') 
print(matrix)
matrix[-1].pop(0)
print(matrix)
