import unittest
from Solution import Solution

class Test(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 1])

    def test_case_2(self):
        nums = [3, 2, 4]
        target = 6
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [1, 2])

    def test_case_3(self):
        nums = [3, 3]
        target = 6
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 1])

if __name__ == "__main__":
    unittest.main()
