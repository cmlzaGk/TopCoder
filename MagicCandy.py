# https://community.topcoder.com/stat?c=problem_statement&pm=11706
# Lemma 1: Number of elements between two squares is x?^2-(x-1)^2=2x-1
# Lemma 2: If n was a perfect square say x^2 it would take 2 iterations
# to reduce n to a size of (x-1)^2
# Assume n is a perfect square x^2
# Number of elements at the end of the array between index a[(x-1)^2 ]
# and a[x^2 ]by lemma 1 is 2x-1. Lets call this subarray the tail.
# Consider first two iterations where we remove perfect square locations
# and resize the array
# In the first iteration we will remove exactly 1 element from tail
# at position a[x^2]
# Now there will be no element at x^2 and the new element in (x-1)^2
# will be (x-1)^2+x-1) which will get deleted.
# After every two iterations by lemma 2 we would get a new array of perfect
# square (x-1)^2. The new tail is 2x+1 by lemma 1 which is exactly original
# tail-2 elements that we removed.
# We can see that original tail is made up two subarrays first containing x-1,
# second containing x elements and we remove the last element of both these
# subarrays in every two iterations and when the array reduces to a size
# (x-1)^2, the tail reduces to two subarrays x-2 and x-1 for a total of
# 2*(x-1)-1
# As we recurse down to an array of 4 we are left with a tail of size 3
# as it takes 2*(x-2)iterations , at each iterations we have reduced
# x-2 elements from each subarray. Hence this tail is made up of exactly
# three elements first two elements of the first subarray of the original
# tail and first element of the last array of the original tail.
# The array of size 4 would look like a[dontcare],a[(x-1)^2+1], a[x^2-x+1],
# a[x^2-x+2]which basically indicates that the last remaining element will be
# a[x^2-x+1]
# For cases where n is not a perfect square we can just stub out the tail of
# n to a perfect square. Since we are always reducing from the end of the
# subarrays of the tails,
# we can simply ignore the stubbed out numbers as they will get reduced to
# the above array of 4 in the same manner irrespective of whatever the value
# of n is between (x-1)^2 and x^2. However when reduced to this form and n
# was less than x^2-x+1 , we are actually left with only two elements less
# than n in which case a[(x-1)^2+1]would be the remaining element.

import math
import unittest

class MagicCandy:
    def whichOne(self, n):
        x = math.ceil(math.sqrt(n))
        return ((x-1)*(x-1) +1) if n < x*x-x+1 else x*x-x+1

class MagicCandyTest(unittest.TestCase):
    def driver(self, n, expected):
        self.assertEqual(MagicCandy().whichOne(n), expected)
    def test_MagicCandy_range(self):
        for n in range(1,65):
            inArr=[i for i in range(1,n+1)]
            while len(inArr) != 1:
                sqrtroot = int(math.sqrt(len(inArr)))
                for i in range(sqrtroot,0,-1):
                    del inArr[(i*i)-1]
            self.driver(n,inArr[0])
    def test_MagicCandy_examples(self):
        self.driver(5, 5)
        self.driver(9, 7)
        self.driver(20, 17)
        self.driver(5265, 5257)
        self.driver(20111223, 20110741)

if __name__ == "__main__":
    unittest.main()
