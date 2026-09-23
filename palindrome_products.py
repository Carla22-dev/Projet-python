
def reversed_digits(n):
    revnum=0
    while n>0:
        revnum=revnum*10 + n%10
        n=n//10
    return revnum

def palindrome (min_factor , max_factor):
    result_product=[]

    for i in range (1,max_factor+1):
        #print(i)
        for j in range (1,max_factor+1):
            product_btw_value=i*j
            #print(product_btw_value)
            if product_btw_value==reversed_digits(product_btw_value):
                print(product_btw_value)
                if product_btw_value not in result_product:
                    result_product.append(product_btw_value)
            continue
    return result_product     


def largest(min_factor, max_factor):
    
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    result_palindrome=palindrome(min_factor,max_factor)
    return max(result_palindrome)

def smallest(min_factor, max_factor):
    
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    result_palindrome=palindrome(min_factor,max_factor)
    return min(result_palindrome)


print(f"value of list{palindrome(10,99)} small {smallest(10,99)}  largest {largest(10,99)}:", )

