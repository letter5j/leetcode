import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_findRotateSteps_top_down(self):
        self.assertEqual(
            167,
            self.solution.maxCoins_top_down(nums=[3, 1, 5, 8])
        )

    def test_findRotateSteps_top_down1(self):
        self.assertEqual(
            10,
            self.solution.maxCoins_top_down(nums=[1, 5])
        )


if __name__ == '__main__':
    unittest.main()
