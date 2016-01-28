# https://arena.topcoder.com/#/u/practiceCode/16665/50689/14122/1/327920
import unittest

class FiringEmployees:
    def fire(self, manager, salary, productivity):
        profit = [0 for i in range(len(manager)+1)]
        for i in reversed(range(len(manager))):
            profit[i+1] += productivity[i] - salary[i]
            profit[i+1] = 0 if profit[i+1] < 0 else profit[i+1]
            profit[manager[i]] += profit[i+1]
        return profit[0]

class FiringEmployeesTest(unittest.TestCase):
    def driver(self, manager, salary, productivity, expected):
        result = FiringEmployees().fire(manager, salary, productivity)
        self.assertEqual(result, expected)
    def test_FiringEmployees(self):
        self.driver((0,0,0),(1,2,3),(3,2,1),2)
        self.driver((0,1),(1,10),(5,5),4)
        self.driver((0,1,2,1,2,3,4,2,3),\
                    (5,3,6,8,4,2,4,6,7),\
                    (2,5,7,8,5,3,5,7,9),\
                    6)
        self.driver((0,0,1,1,2,2), \
                    (1,1,1,2,2,2), \
                    (2,2,2,1,1,1), \
                    3)

if __name__ == "__main__":
    unittest.main()
