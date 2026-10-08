
def largest_product(series, size):
    lens=len(series)
    if size > lens :
        raise ValueError("span must not exceed string length")
    if size <=0:
        raise ValueError("span must not be negative")
    if not series.isdigit():
        raise ValueError("digits input must only contain digits")
    
    result=[]
    res=1
    final_produt=[]
    size_count=0
    for serie in range(len(series)-size+1):
        result.append(series[serie:size+serie])
    for i in range (len(result)):
        sequence=result[i]
        for digit in sequence:
            res*=int(digit)
        
        final_produt.append(res)
        res=1
    max_product=max(final_produt)
    return max_product


print(largest_product("0123456789",2))