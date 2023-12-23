import unittest

from day_4.solve_pt1 import DayFourPartOneSolver


class TestDay4Part1(unittest.TestCase):
    def setUp(self):
        self.solver = DayFourPartOneSolver.solve
        self.web_example_lines = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        ]

    def test_problem_example(self):
        ans = self.solver(self.web_example_lines)
        self.assertEqual(13, ans)

    def test_four_nums_overlap(self):
        ans = self.solver(self.web_example_lines[0:1])
        self.assertEqual(8, ans)

    def test_two_nums_overlap(self):
        ans = self.solver(self.web_example_lines[2:3])
        self.assertEqual(2, ans)

    def test_one_nums_overlap(self):
        ans = self.solver(self.web_example_lines[3:4])
        self.assertEqual(1, ans)

    def test_no_nums_overlap(self):
        ans = self.solver(self.web_example_lines[4:5])
        self.assertEqual(0, ans)
        ans = self.solver(self.web_example_lines[5:6])
        self.assertEqual(0, ans)

