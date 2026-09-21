
# def base_two (decimal_number,output_base):
#     out_digits=[]
#     while decimal_number>0: 
#         out_digits.append(decimal_number%output_base)
#         decimal_number//=output_base
#     out_digits.reverse()
#     return out_digits

def base_128 (decimal_number,output_base):
    print(f" o valor é {decimal_number}")
    out_digits=[]
    if decimal_number==0:
        return [0]
    while decimal_number>0: 
        out_digits.append(decimal_number%output_base)
        decimal_number//=output_base
    out_digits.reverse()
    return out_digits

# def encode(numbers):
#     numbers=[0]
#     out_digits=[]
#     out_digits=base_two(numbers,128)

#     for i,digit in enumerate( out_digits):
#         print(f" this is digit{digit}")
#         if i != len(out_digits)-1:
#             out_digits[i]= digit | 128
#         else:
#             pass
#     for i, digit in enumerate( out_digits):
#         out_digits[i]=hex(digit)
#     return out_digits
  

# def encode (numbers):
#     out_digits=[]
#     out=[]
#     for number in numbers:
#         out_digits=base_128(number,128)
#         print(f"O valor {out_digits}")
#         for i,digit in enumerate(out_digits):
#             if i!= len(out_digits)-1: 
#                 out_digits[i]= digit | 128
#                 print(f"Digit dentro do for_: {out_digits}")
#             else:
#                 pass
#     for i, digit in enumerate( out_digits):
#           out_digits[i]=hex(digit)
#         #out.extend(out_digits)
#     return out_digits
#         # print(f"position ={digit} - the number is {number}")
#         # out_digits=base_two(number,128)
#         # print(f"The out_digits {out_digits}")

def decode(bytes):
    result=0

    for digit in bytes:
        print(f"out digit {bytes}")
        #print(f"indice i = {i}, value = {bytes}")
        digit= digit & 127
        result=(result << 7)| digit
        print(f"The result {result}")
        print(f"qual  valor do digit {digit}")
        
print(f"This bits is : {decode([0xC0,0x0])}")