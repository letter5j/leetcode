import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_findRotateSteps_top_down(self):
        self.assertEqual(
            2,
            self.solution.superEggDrop_top_down(k=1, n=2)
        )
        self.assertEqual(
            3,
            self.solution.superEggDrop_top_down(k = 2, n = 6)
        )
        self.assertEqual(
            4,
            self.solution.superEggDrop_top_down(k = 3, n = 14)
        )
        self.assertEqual(
            2,
            self.solution.superEggDrop_top_down(k = 2, n = 2)
        )


if __name__ == '__main__':
    unittest.main()
