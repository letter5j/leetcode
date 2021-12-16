import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_stoneGame(self):
        self.assertEqual(
            True,
            self.solution.stoneGame(piles=[5, 3, 4, 5])
        )
        self.assertEqual(
            True,
            self.solution.stoneGame(piles=[3, 7, 2, 3])
        )


if __name__ == '__main__':
    unittest.main()
