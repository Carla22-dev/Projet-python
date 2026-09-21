

import copy


# matrix=[['a','b'],#Row 0
#         ['c','d']
# ] #Row 1

# matrix_copy=copy.deepcopy(matrix)
# matrix.pop()

# matrix_copy[0].append('z')

# print('Original: ', matrix)
# print('Copy: ', matrix_copy)

original=[['a','b'],#Row 0
          ['c','d']] #Row 1


#ASSIGMENT

copy1=original
print("Same object ?", original is copy1, "\n")

#Shadow Copy 

copy2=original.copy()
print(copy2)
print("Same Object?", original is copy2)
print("Shared Lists ?", original[0] is copy2[0], "\n")

#Deep  Copy 
copy3=copy.deepcopy(original)
print("Same Object?: ",original is copy3)
print("Shared Lists?: ",original[0] is copy3[0], "\n")
