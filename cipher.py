
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

#print("The matrix is ", encode("WEAREDISCOVEREDFLEEATONCE", 3))


def decode(encoded_message, rails):
    direction =1
    directzero=0
    direction1=0
    direction2=0
    current_rail=0
    position=0
    quantities=[]
    rails_list=[]
    matrix=[
        []  for _ in range (rails)]
    result=[]
    for i, cipher in enumerate((encoded_message)):
        result.append(current_rail)
        #matrix[current_rail].append(cipher)
        if current_rail== rails-1:
            direction=-1
        elif current_rail==0:
            direction=1
        current_rail+=direction
    for i in range(rails):
        quant=result.count(i)
        quantities.append(quant)

    for quant in quantities:
        rails_list.append([])
    for i in range(rails):
        quant = quantities[i]

        rail = list(encoded_message[position:position + quant])

        rails_list[i] = rail

        position += quant

    decoded_message = []

    rail_positions = [0] * rails

    for current_rail in result:
        decoded_message.append(
            rails_list[current_rail][rail_positions[current_rail]]
        )

        rail_positions[current_rail] += 1

    return ''.join(decoded_message)



print(decode("TEITELHDVLSNHDTISEIIEA", 3))