import unittest

from day_4.solve_pt2 import DayFourPartTwoSolver


class TestDay4Part2(unittest.TestCase):
    def setUp(self):
        self.solver = DayFourPartTwoSolver.solve
        self.web_example_lines = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        ]

        """     1 2 3 4 5 6 instances
        1: 4 m: 0 0 0 0 0 0 1
        2: 2 m: 1 0 0 0 0 0 2
        3: 2 m: 1 1 0 0 0 0 4
        4: 1 m: 1 1 1 0 0 0 8
        5: 0 m: 1 0 1 1 0 0 14
        6: 0 m: 0 0 0 0 0 0 1
                       sum: 30

                1 2 3 4 5  6
          1:    1 1 1 1 1  1
          2:    0 2 2 2 2  0
          3:    0 0 4 4 0  0
          4:    0 0 0 8 8  0
          5:    0 0 0 0 14 0
          6:    0 0 0 0 0  1
        """

    def test_web_example(self):
        ans = self.solver(self.web_example_lines)
        self.assertEqual(30, ans)

    def test_one_row_one_overlap(self):
        ans = self.solver(self.web_example_lines[5:6])
        self.assertEqual(1, ans)

