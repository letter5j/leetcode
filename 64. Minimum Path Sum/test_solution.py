import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_minPathSum_bottom_up(self):
        self.assertEqual(
            7,
            self.solution.minPathSum_bottom_up(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]])
        )
        self.assertEqual(
            12,
            self.solution.minPathSum_bottom_up(grid=[[1, 2, 3], [4, 5, 6]])
        )

    def test_minPathSum_bottom_up_compress(self):
        self.assertEqual(
            7,
            self.solution.minPathSum_bottom_up_compress(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]])
        )
        self.assertEqual(
            12,
            self.solution.minPathSum_bottom_up_compress(grid=[[1, 2, 3], [4, 5, 6]])
        )

if __name__ == '__main__':
    unittest.main()
