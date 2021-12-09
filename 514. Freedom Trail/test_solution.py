import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_findRotateSteps_top_down(self):
        self.assertEqual(
            4,
            self.solution.findRotateSteps_top_down(ring="godding", key="gd")
        )
        self.assertEqual(
            13,
            self.solution.findRotateSteps_top_down(ring="godding", key="godding")
        )


if __name__ == '__main__':
    unittest.main()
