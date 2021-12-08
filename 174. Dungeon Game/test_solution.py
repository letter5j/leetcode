import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_calculateMinimumHP_top_down(self):
        self.assertEqual(
            7,
            self.solution.calculateMinimumHP_top_down(dungeon=[[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
        )
        self.assertEqual(
            1,
            self.solution.calculateMinimumHP_top_down(dungeon=[[0]])
        )
        self.assertEqual(
            3,
            self.solution.calculateMinimumHP_top_down(dungeon=[[1, -3, 3], [0, -2, 0], [-3, -3, -3]])
        )

    def test_calculateMinimumHP_bottom_up(self):
        self.assertEqual(
            7,
            self.solution.calculateMinimumHP_bottom_up(dungeon=[[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
        )
        self.assertEqual(
            1,
            self.solution.calculateMinimumHP_bottom_up(dungeon=[[0]])
        )
        self.assertEqual(
            3,
            self.solution.calculateMinimumHP_bottom_up(dungeon=[[1, -3, 3], [0, -2, 0], [-3, -3, -3]])
        )

    def test_calculateMinimumHP_bottom_up_compress(self):
        self.assertEqual(
            7,
            self.solution.calculateMinimumHP_bottom_up_compress(dungeon=[[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
        )
        self.assertEqual(
            1,
            self.solution.calculateMinimumHP_bottom_up_compress(dungeon=[[0]])
        )
        self.assertEqual(
            3,
            self.solution.calculateMinimumHP_bottom_up_compress(dungeon=[[1, -3, 3], [0, -2, 0], [-3, -3, -3]])
        )

if __name__ == '__main__':
    unittest.main()
