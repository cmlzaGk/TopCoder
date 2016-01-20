# https://arena.topcoder.com/#/u/practiceCode/16527/48825/13918/2/326683
# F(initial, target)={False if len(target) < len(initial),
#                     initial == target if len(target) == len(initial),
#                     F(initial, target[:-1]) if target[-1:] == "A",
#                     F(initial, reversed(target[:-1])) if target[-1:] == "B"}

import unittest
class ABBA:
    def canObtain(self, initial, target):
        isReversed = False
        start = 0
        end = len(target) - 1
        while len(initial) < (end - start + 1):
            currentTail = target[start] if isReversed else target[end]
            if isReversed:
                start += 1
            else:
                end -= 1
            if currentTail == "B":
                isReversed = not isReversed
        matchString = initial[::-1] if isReversed else initial
        if matchString == target[start:end+1]:
            return "Possible"
        return "Impossible"

class TestABBA(unittest.TestCase):

    def driver(self, initial, target, expected):
        self.assertEqual(ABBA().canObtain(initial, target), expected)

    def test_ABBA(self):
        self.driver("AB", "ABB", "Impossible")
        self.driver("BBAB", "ABABABABB", "Impossible")
        self.driver("BBBBABABBBBBBA", "BBBBABABBABBBBBBABABBBBBBBBABAABBBAA", \
                    "Possible")
        self.driver("A", "BB", "Impossible")
        self.driver("A", "AA", "Possible")

if __name__ == "__main__":
    unittest.main()

