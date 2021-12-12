import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_findRotateSteps_top_down(self):
        self.assertEqual(
            False,
            self.solution.isMatch_top_down(s="aa", p="a")
        )
        self.assertEqual(
            True,
            self.solution.isMatch_top_down(s="aa", p="a*")
        )
        self.assertEqual(
            True,
            self.solution.isMatch_top_down(s="ab", p=".*")
        )
        self.assertEqual(
            True,
            self.solution.isMatch_top_down(s="aab", p="c*a*b")
        )
        self.assertEqual(
            False,
            self.solution.isMatch_top_down(s="mississippi", p="mis*is*p*.")
        )
        self.assertEqual(
            False,
            self.solution.isMatch_top_down(s="ab", p=".*c")
        )
        self.assertEqual(
            True,
            self.solution.isMatch_top_down(s="a", p="ab*")
        )
        self.assertEqual(
            True,
            self.solution.isMatch_top_down(s="bbbba", p=".*a*a")
        )
        self.assertEqual(
            False,
            self.solution.isMatch_top_down(s="a", p=".*..a*")
        )
        self.assertEqual(
            False,
            self.solution.isMatch_top_down(s="b", p="aaa.")
        )


if __name__ == '__main__':
    unittest.main()
