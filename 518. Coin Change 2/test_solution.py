import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_change_top_down(self):
        self.assertEqual(
            4,
            self.solution.change_top_down(amount=5, coins=[1, 2, 5])
        )
        self.assertEqual(
            0,
            self.solution.change_top_down(amount=3, coins=[2])
        )
        self.assertEqual(
            1,
            self.solution.change_top_down(amount=10, coins=[10])
        )

    def test_change_bottom_up(self):
        self.assertEqual(
            4,
            self.solution.change_bottom_up(amount=5, coins=[1, 2, 5])
        )
        self.assertEqual(
            0,
            self.solution.change_bottom_up(amount=3, coins=[2])
        )
        self.assertEqual(
            1,
            self.solution.change_bottom_up(amount=10, coins=[10])
        )

    def test_change_bottom_up_compress(self):
        self.assertEqual(
            4,
            self.solution.change_bottom_up_compress(amount=5, coins=[1, 2, 5])
        )
        self.assertEqual(
            0,
            self.solution.change_bottom_up_compress(amount=3, coins=[2])
        )
        self.assertEqual(
            1,
            self.solution.change_bottom_up_compress(amount=10, coins=[10])
        )


if __name__ == '__main__':
    unittest.main()
