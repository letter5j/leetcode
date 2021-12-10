import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_findRotateSteps_top_down(self):
        self.assertEqual(
            200,
            self.solution.findCheapestPrice_top_down(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2,
                                                     k=1)
        )
        self.assertEqual(
            500,
            self.solution.findCheapestPrice_top_down(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2,
                                                     k=0)
        )
        self.assertEqual(
            1,
            self.solution.findCheapestPrice_top_down(3, [[0, 1, 2], [1, 2, 1], [2, 0, 10]], 1, 2, 1)
        )


if __name__ == '__main__':
    unittest.main()
