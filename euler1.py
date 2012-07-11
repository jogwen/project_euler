#!/usr/bin/env python

# Add all the natural numbers below one thousand that are multiples of 3 or 5.

import utils

limit = 1000
factors = [3,5]
result = utils.result_of_multiples(factors, limit)

print "The sum of all the natural numbers below %d that are multiples of %s is %d" % (limit, factors, result)

