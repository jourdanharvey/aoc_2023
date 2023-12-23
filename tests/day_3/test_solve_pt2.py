import unittest
from day_3.solve_pt2 import DayThreePartTwoSolver, scan_for_number


class TestDay3Part1(unittest.TestCase):
    def setUp(self):
        self.solver = DayThreePartTwoSolver.solve

    def test_surrounded_horizontal(self):
        lines = ["2*3"]
        ans = self.solver(lines)
        self.assertEqual(6, ans)

    def test_wings_up(self):
        lines = [
            "10.10",
            "..*..",
        ]
        ans = self.solver(lines)
        self.assertEqual(100, ans)

    def test_wings_down(self):
        lines = [
            "..*..",
            "10.10",
        ]
        ans = self.solver(lines)
        self.assertEqual(100, ans)

    def test_three_numbers(self):
        lines = [
            "..*1.",
            "10.10",
        ]
        ans = self.solver(lines)
        self.assertEqual(0, ans)

    def test_given_example(self):
        lines = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
        ]
        ans = self.solver(lines)
        self.assertEqual(467835, ans)