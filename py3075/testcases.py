import unittest

# Assume the class name is Solution and the method is maximumHappinessSum
class TestSolution(unittest.TestCase):
    def setUp(self):
        # Create an instance of the solution to test
        from zzllib import Solution # Change this to your actual file name
        self.sol = Solution()

    def test_example_1(self):
        # Case: happiness = [1,2,3], k = 2
        # Round 1: Pick 3. Others become [0, 1].
        # Round 2: Pick 1. Total = 3 + 1 = 4.
        self.assertEqual(self.sol.maximumHappinessSum([1, 2, 3], 2), 4)

    def test_example_2(self):
        # Case: all same values. happiness = [1,1,1,1], k = 2
        # Round 1: Pick 1. Others become [0,0,0].
        # Round 2: Pick 0. Total = 1 + 0 = 1.
        self.assertEqual(self.sol.maximumHappinessSum([1, 1, 1, 1], 2), 1)

    def test_example_3(self):
        # Case: k = 1. Just pick the max.
        self.assertEqual(self.sol.maximumHappinessSum([2, 3, 4, 5], 1), 5)

    def test_happiness_not_negative(self):
        # Extra Case: Ensure values don't go below 0
        # happiness = [1, 1, 1], k = 3
        # Pick 1 -> [0, 0] -> Pick 0 -> [0] -> Pick 0. Sum = 1.
        self.assertEqual(self.sol.maximumHappinessSum([1, 1, 1], 3), 1)

    def test_large_numbers(self):
        # Extra Case: Large integers
        self.assertEqual(self.sol.maximumHappinessSum([100, 200, 300], 2), 499)
        # (300) + (200 - 1) = 499

    def test_little_end_numbers(self):
        # Extra Case: little end numbers
        self.assertEqual(self.sol.maximumHappinessSum([2,83,62], 3), 144)
        # (300) + (200 - 1) = 499

if __name__ == '__main__':
    unittest.main()