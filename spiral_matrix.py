
size=5
top=0
bottom=size-1
right=size-1
left=0
number_of_spiral=1

matrix=[
    [0]*size # o que quero fazer 
    for _ in range( size) #para este numero de size
]

while top<=bottom and left<=right:
    
    # left ---> right
    for col in range(left,right+1):
        matrix[top][col]=number_of_spiral
        number_of_spiral+=1
    top+=1

    # up---> down
    
    for row in range(top,right+1):
        matrix[row][right]=number_of_spiral
        number_of_spiral+=1

    right-=1

    # right------> left
    for col in range(right,left-1,-1):
        # print(f"col{col} ")
        # print(number_of_spiral)
        matrix[bottom][col]=number_of_spiral
        number_of_spiral+=1

    bottom-=1
    
    # down ----> up
    for row in range (bottom,top-1,-1):
        matrix[row][left]=number_of_spiral
        number_of_spiral+=1
    left+=1

    
print(f"top {top}, bottom {bottom} , right {right}, left {left}")
print(matrix)