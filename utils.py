#!/usr/bin/env python

# Utility functions for Project Euler problems

def isfactorof(factor_candidate, n):
    """
    Returns True if factor_candidate is a factor of n, else returns False
    
    >>> isfactorof(3, 3)
    True
    >>> isfactorof(2, 3)
    False
    >>> isfactorof('3', 3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "utils.py", line 16, in isfactorof
        if n % factor_candidate == 0:
    TypeError: unsupported operand type(s) for %: 'int' and 'str'
    """
    if n % factor_candidate == 0:
        return True
    else:
        return False

def sum_of_multiples(factors, limit):
    """
    Return sum of all natural numbers below limit that are multiples of one of the integers in factors.

    >>> sum_of_multiples([3,5], 10)
    23
    >>> sum_of_multiples([3,5], 1000)
    233168
    """
    sum = 0
    for n in range(limit):
        for factor in factors:
            if isfactorof(factor, n):
                sum += n
                break
    return sum

def sum_of_even_fibonacci_terms(max_number):
    """
    Return sum of all even-valued Fibonacci terms not exceeding max_number.

    >>> sum_of_even_fibonacci_terms(89)
    44
    """
    a, b = 1, 2
    # Don't need initial value of a because it's odd
    result = 0
    while (a <= max_number and b <= max_number):
        if b % 2 == 0: result += b 
        new_b = a + b
        a, b = b, new_b
    return result

def strip_divisible_by(intList, factor):
    """
    Returns a new list of integers which is the input list of integers minus any integers divisible by factor.

    >>> strip_divisible_by(range(1, 9), 3)
    [1, 2, 4, 5, 7, 8]
    """
    newIntList = []
    for i in intList:
        if not i % factor == 0:
            newIntList.append(i)
    return newIntList
            
def primes_up_to(max, smaller_primes=[]):
    """
    Returns a list of primes not exceeding max, and building upon smaller_primes if supplied
    
    >>> primes_up_to(11)
    [2, 3, 5, 7, 11]
    """
    primes = []
    candidates = range(2,max+1)
    while len(candidates) > 0:
        p = candidates[0]
        primes.append(p)
        del(candidates[0])
        candidates = strip_divisible_by(candidates, p)
    return primes        

def largest_prime_factor_of(number):
    """
    Return the largest prime factor of number.
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()

