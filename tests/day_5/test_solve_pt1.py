
import unittest
from common import file_lines
from day_5.solve_pt1_take_2 import Almanac

from day_5.solve_pt1_take_2 import DayFivePartOneTakeTwoSolver


class TestDay5Part1(unittest.TestCase):
    def setUp(self):
        self.solver = DayFivePartOneTakeTwoSolver.solve
        self.web_example_lines = [
            'seeds: 79 14 55 13',
            '',
            'seed-to-soil map:',
            '50 98 2',
            '52 50 48',
            '',
            'soil-to-fertilizer map:',
            '0 15 37',
            '37 52 2',
            '39 0 15',
            '',
            'fertilizer-to-water map:',
            '49 53 8',
            '0 11 42',
            '42 0 7',
            '57 7 4',
            '',
            'water-to-light map:',
            '88 18 7',
            '18 25 70',
            '',
            'light-to-temperature map:',
            '45 77 23',
            '81 45 19',
            '68 64 13',
            '',
            'temperature-to-humidity map:',
            '0 69 1',
            '1 0 69',
            '',
            'humidity-to-location map:',
            '60 56 37',
            '56 93 4',
        ]
        self.almanac = Almanac()

    def test_web_example(self):
        ans = self.solver(self.web_example_lines)
        self.assertEqual(35, ans)

    def test_navigate_no_mappings(self):
        ans = self.almanac.navigate(1)
        self.assertEqual(1, ans)

    def test_seed_to_soil(self):
        lines = [
            '50 98 2',
            '52 50 48',
        ]
        for line in lines:
            self.almanac.add_mapping_from_line(line)

        cases = [
            (79, 81),
            (14, 14),
            (55, 57),
            (13, 13),
        ]

        for source, dest in cases:
            ans = self.almanac.navigate(source)
            self.assertEqual(dest, ans)

    def test_soil_to_fertilizer(self):
        lines = [
            '0 15 37',
            '37 52 2',
            '39 0 15',
        ]
        for line in lines:
            self.almanac.add_mapping_from_line(line)

        cases = [
            (81, 81),
            (14, 53),
            (57, 57),
            (13, 52),
        ]

        for source, dest in cases:
            ans = self.almanac.navigate(source)
            self.assertEqual(dest, ans)


    def test_fertilizer_to_water(self):
        lines = [
            '49 53 8',
            '0 11 42',
            '42 0 7',
            '57 7 4',
        ]
        for line in lines:
            self.almanac.add_mapping_from_line(line)

        cases = [
            (81, 81),
            (53, 49),
            (57, 53),
            (52, 41),
        ]

        for source, dest in cases:
            ans = self.almanac.navigate(source)
            self.assertEqual(dest, ans)

    def test_water_to_light(self):
        lines = [
            '88 18 7',
            '18 25 70',
        ]
        for line in lines:
            self.almanac.add_mapping_from_line(line)

        cases = [
            (81, 74),
            (49, 42),
            (53, 46),
            (41, 34),
        ]

        for source, dest in cases:
            ans = self.almanac.navigate(source)
            self.assertEqual(dest, ans)

    def test_light_to_temperature(self):
        lines = [
            '45 77 23',
            '81 45 19',
            '68 64 13',
        ]
        for line in lines:
            self.almanac.add_mapping_from_line(line)

        cases = [
            (74, 78),
            (42, 42),
            (46, 82),
            (34, 34),
        ]

        for source, dest in cases:
            ans = self.almanac.navigate(source)
            self.assertEqual(dest, ans)

    def test_temperature_to_humidity(self):
        lines = [
            '0 69 1',
            '1 0 69',
        ]
        for line in lines:
            self.almanac.add_mapping_from_line(line)

        cases = [
            (78, 78),
            (42, 43),
            (82, 82),
            (34, 35),
        ]

        for source, dest in cases:
            ans = self.almanac.navigate(source)
            self.assertEqual(dest, ans)

    def test_humidity_to_location(self):
        lines = [
            '60 56 37',
            '56 93 4',
        ]
        for line in lines:
            self.almanac.add_mapping_from_line(line)

        cases = [
            (78, 82),
            (43, 43),
            (82, 86),
            (35, 35),
        ]

        for source, dest in cases:
            ans = self.almanac.navigate(source)
            self.assertEqual(dest, ans)


    def test_navigate_one_line_mapping(self):
        self.almanac.add_mapping_from_line("50 98 2")
        cases = [
            (97, 97),
            (98, 50),
            (99, 51),
            (100, 100),
        ]
        for source, dest in cases:
            ans = self.almanac.navigate(source)
            self.assertEqual(dest, ans)

    def test_navigate_two_mappings_from_example(self):
        self.almanac.add_mapping_from_line("50 98 2")
        self.almanac.add_mapping_from_line("52 50 48")
        cases = [
            (0, 0),
            (1, 1),
            (48, 48),
            (49, 49),
            (50, 52),
            (51, 53),
            (96, 98),
            (97, 99),
            (98, 50),
            (99, 51),
        ]
        for source, dest in cases:
            ans = self.almanac.navigate(source)
            self.assertEqual(dest, ans)

    def test(self):
        file_path = './day_5/input.txt'
        ans = DayFivePartOneTakeTwoSolver.solve(file_lines(file_path))
        self.assertIsNotNone(ans)
