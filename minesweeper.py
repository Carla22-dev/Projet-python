
def annotate(garden):
    garden = [list(row) for row in garden]
    if not garden:
        return []
    width = len(garden[0])
    for row in garden:
        if len(row) != width :
            raise ValueError("The board is invalid with current input.")
    for row in garden:
        for cell in row:
            if cell not in (" ", "*"):
                raise ValueError("The board is invalid with current input.")
    for row in range(len(garden)):
        for col in range(len(garden[row])): 
            if garden[row][col]==" ":   
                count_flower=0   
                for drow in [-1,0,1]:# descobrir todas as posiçoes 
                    
                    for dcol in [-1,0,1]:
                        
                            neighbor_row=row+drow
                            neighbor_col=col+dcol
                            if 0<= neighbor_row < len(garden) and (0<= neighbor_col<len(garden[row])):
                                if garden[neighbor_row][neighbor_col]=="*":
                                    count_flower+=1
                if count_flower==0:
                    continue
                garden[row][col]=(str(count_flower))
            if garden[row][col]=="*":
                continue
    garden = ["".join(row) for row in garden]
    return garden

garden=["   ", " * ", "   "]


print(" The matrix is :", annotate(garden))
                        

            