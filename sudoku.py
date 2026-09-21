from itertools import combinations


def combination(target, size, exclude):

#def combinations_with_sum(target,size):
    result=[]
    if size==1 :
       result.append(target)
       return result
    
    for combination in combinations(range (1,10),size):
        list_combination=sorted(list(combination))
        #print("a lista ",list_combination)
        if any(digit in exclude for digit in combination) :
           continue
        # for num in exclude:
        #     print("the exclude is ", num)
        #     for comb in list_combination:
        #         print("the list is ", comb)
        #         if num==comb:
        #             break
        if sum(combination)==target:
            result.append(combination)   
    return result

print(f"The combination is : {combination(10, 2, [1, 4])}")


