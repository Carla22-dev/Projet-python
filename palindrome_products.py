
def reversed_digits(n):
    revnum=0
    while n>0:
        revnum=revnum*10 + n%10
        n=n//10
    return revnum

def palindrome (min_factor , max_factor):
    result_product=[]
    result_number_multipl=[]
    position=0
    dict_factor={}
    already_exist=False

    for i in range (min_factor,max_factor+1):
        for j in range (min_factor,max_factor+1):
            product_btw_value=i*j
            new_pair=sorted([i,j])
            if product_btw_value==reversed_digits(product_btw_value):
                if product_btw_value not in dict_factor:
                    dict_factor[product_btw_value]=[]
                already_exist=False
                for pair in dict_factor[product_btw_value]:
                    if sorted(pair)==new_pair:
                        already_exist=True
                        break
                if not already_exist:
                    dict_factor[product_btw_value].append([i,j])
                
                if product_btw_value not in result_product:
                    result_product.append(product_btw_value)
    return dict_factor     


def largest(min_factor, max_factor):
    
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    result_palindrome=palindrome(min_factor,max_factor)
    max_namber=max(result_palindrome)
    tup=()
    tup=(max_namber,list(result_palindrome[max_namber]))
    return tup

def smallest(min_factor, max_factor):
    
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    result_palindrome=palindrome(min_factor,max_factor)
    min_number=min(result_palindrome)
    tup=()
    tup=(min_number,list(result_palindrome[min_number]))
    return tup
    


print(f"value of list{palindrome(10,99)} small {smallest(10,99)}  largest {largest(10,99)}:", )

