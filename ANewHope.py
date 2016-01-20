from __future__ import division
import math
import unittest

# https://arena.topcoder.com/#/u/practiceCode/16656/45873/13585/1/327836

class ANewHope:
    def count(self, firstWeek, lastWeek, D):
        N = len(firstWeek)
        target={}
        for idx,val in enumerate(lastWeek):
            target[val] = idx
        result=0
        for idx,val in enumerate(firstWeek):
            result = max(result, math.ceil((idx-target[val])/(N-D)))
        return result + 1

class TestANewHope(unittest.TestCase):
    def driver(self, firstWeek, lastWeek, D, expected):
        result = ANewHope().count(firstWeek, lastWeek, D)
        self.assertEqual(result, expected)
    def test_ANewHope(self):
        self.driver((1,2,3,4),(1,2,3,4),2,1)
        self.driver((1,2,3,4),(4,3,2,1),3,4)
        self.driver((8,5,6,1,7,6,3,2),(2,4,6,8,1,3,5,7),3,3)

if __name__ == "__main__":
    unittest.main()
