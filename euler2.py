#!/usr/bin/env python

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

import utils

max_value = 4 * (10 ** 6)

result = utils.sum_of_even_fibonacci_terms(max_value)

print "The sum of the even-valued terms of the Fibonacci sequence whose values do not exceed %d is %d" %(max_value, result)

