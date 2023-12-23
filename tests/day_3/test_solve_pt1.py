import unittest
from day_3.solve_pt1 import DayThreePartOneSolver
from day_3.solve_pt1_dave import DayThreePartOneDaveSolver
from day_3.solve_pt1_take_2 import DayThreePartOneTakeTwoSolver, surrounding_points

class TestDay3Part1(unittest.TestCase):
    def setUp(self):
        self.solver = DayThreePartOneSolver.solve

    def test_empty(self):
        lines = []
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
        self.assertEqual(4361, ans)

    def test_given_example_numbers_at_end(self):
        lines = [
            "467..114.",
            "...*.....",
            "..35..633",
            "......#..",
            "617*.....",
            ".....+.58",
            "..592....",
            "......755",
            "...$.*...",
            ".664.598.",
        ]
        ans = self.solver(lines)
        self.assertEqual(4361, ans)

    def test_symbol_right(self):
        lines = ['1#']
        ans = self.solver(lines)
        self.assertEqual(1, ans)

    def test_symbol_left(self):
        lines = ['#1']
        ans = self.solver(lines)
        self.assertEqual(1, ans)

    def test_symbol_above(self):
        lines = ['#','1']
        ans = self.solver(lines)
        self.assertEqual(1, ans)

    def test_symbol_below(self):
        lines = ['1','#']
        ans = self.solver(lines)
        self.assertEqual(1, ans)

    def test_symbol_upper_left(self):
        lines = ['#.','.1']
        ans = self.solver(lines)
        self.assertEqual(1, ans)

    def test_symbol_upper_right(self):
        lines = ['.#','1.']
        ans = self.solver(lines)
        self.assertEqual(1, ans)

    def test_newline(self):
        lines = ['1\n']
        ans = self.solver(lines)
        self.assertEqual(0, ans)

    def test_symbol_lower_left(self):
        lines = ['.1','#.']
        ans = self.solver(lines)
        self.assertEqual(1, ans)

    def test_symbol_lower_right(self):
        lines = ['1.','.#']
        ans = self.solver(lines)
        self.assertEqual(1, ans)

    def test_symbol_between(self):
        lines = ['1#1']
        ans = self.solver(lines)
        self.assertEqual(2, ans)

    def test_no_symbol_between(self):
        lines = ['1.1']
        ans = self.solver(lines)
        self.assertEqual(0, ans)

    def test_symbol_uppper_between(self):
        lines = [
            '.#.',
            '1.1',
        ]
        ans = self.solver(lines)
        self.assertEqual(2, ans)

    def test_symbol_lower_between(self):
        lines = [
            '1.1',
            '.#.',
        ]
        ans = self.solver(lines)
        self.assertEqual(2, ans)

    def test_symbol_around(self):
        """
        Checks we only count part number once
        """
        lines = ['#1#']
        ans = self.solver(lines)
        self.assertEqual(1, ans)

    def test_double_digit(self):
        lines = ['10#']
        ans = self.solver(lines)
        self.assertEqual(10, ans)

    def test_double_digit_left(self):
        lines = ['#10']
        ans = self.solver(lines)
        self.assertEqual(10, ans)

    def test_no_symbol(self):
        lines = ['1']
        ans = self.solver(lines)
        self.assertEqual(0, ans)

    def test_surrounded_vertically(self):
        ans = self.solver(list("#1#1#"))
        self.assertEqual(2, ans)

    def test_two_surrounded_numbers(self):
        lines = [
            '#####',
            '#1#1#',
            '#####',
        ]
        ans = self.solver(lines)
        self.assertEqual(2, ans)

    def test_surrounded_double_digit(self):
        lines = [
            '####',
            '#10#',
            '####',
        ]
        ans = self.solver(lines)
        self.assertEqual(10, ans)

    def test_not_surrounded_double_digit(self):
        lines = [
            '....#',
            '.10..',
            '.....',
        ]
        ans = self.solver(lines)
        self.assertEqual(0, ans)

    def test_negative_number(self):
        ans = self.solver(["-10#"])
        self.assertEqual(10, ans)

    def test_double_digit_symbol_right(self):
        ans = self.solver(["10#"])
        self.assertEqual(10, ans)

    def test_double_digit_symbol_left(self):
        ans = self.solver(["#10"])
        self.assertEqual(10, ans)

    def test_large_number_symbol_diagonally_adjacent(self):
        lines = [
            '#....',
            '.1234',
        ]
        ans = self.solver(lines)
        self.assertEqual(1234, ans)

    def test_numbers_diagonally_opposite(self):
        lines = [
            '1.',
            '.1',
        ]
        ans = self.solver(lines)
        self.assertEqual(0, ans)

    def test_numbers_diagonally_opposite_with_symbol(self):
        lines = [
            '1#',
            '.1',
        ]
        ans = self.solver(lines)
        self.assertEqual(2, ans)

    def test_some_reddit_example(self):
        ans = self.solver(['*100.100*100.100.100*'])
        self.assertEqual(400, ans)

    def test_some_reddit_example_2(self):
        ans = self.solver([
            '....221',
            '......*'
        ])
        self.assertEqual(221, ans)


class TestDay3Part1Take2(TestDay3Part1):
    def setUp(self):
        self.solver = DayThreePartOneTakeTwoSolver.solve

    def test_surrounding_points(self):
        origin = (0,0)
        self.assertTrue(origin not in set(surrounding_points(*origin)))

class TestDay3Part1Dave(TestDay3Part1):
    def setUp(self):
        self.solver = DayThreePartOneDaveSolver.solve
