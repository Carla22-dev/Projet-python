
def encode(message, rails):
    
    matrix=[
        [] # o que quero fazer 
        for _ in range( rails) #para este numero de rails
    ]
    current_rail=0
    
    for cipher in message:
        matrix[current_rail].append(cipher)
        if current_rail== rails-1:
            direction=-1
        elif current_rail==0:
            direction=1
        current_rail+=direction
    matrix =''.join(''.join(row) for row in matrix)
    return matrix

print("The matrix is ", encode("WEAREDISCOVEREDFLEEATONCE", 3))