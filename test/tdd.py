import unittest
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.workday import WorkDay
from utils.parsers.parseData import parseWorkDay
from utils.exceptions.exceptions import InvalidFormatError


class ParseDataTest(unittest.TestCase):

    def test__parseWorkDay__raise_an_exception__when_format_is_invalid(self):
        work_day_input = "MO10:0s-12:00"
        with self.assertRaises(InvalidFormatError):
            parseWorkDay(work_day_input)
    
    def test__parseWorkDay__give_a_WorkDay__when_format_is_valid(self):
        work_day_input = "MO10:00-12:00"
        work_day_parsed = parseWorkDay(work_day_input)
        self.assertIsInstance(work_day_parsed, WorkDay)

    
if __name__ == '__main__':
    unittest.main()