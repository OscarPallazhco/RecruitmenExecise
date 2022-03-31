import unittest
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.workday import WorkDay
from utils.parsers.parseData import parseWorkDay
from utils.exceptions.exceptions import InvalidFormatError
from classes.schedules_file import SchedulesFileModel
from classes.employee_work_days import EmployeeWorkDays


class ParseDataTest(unittest.TestCase):

    def test__parseWorkDay__raise_an_exception__when_format_is_invalid(self):
        work_day_input = "MO10:0s-12:00"
        with self.assertRaises(InvalidFormatError):
            parseWorkDay(work_day_input)
    
    def test__parseWorkDay__give_a_WorkDay__when_format_is_valid(self):
        work_day_input = "MO10:00-12:00"
        work_day_parsed = parseWorkDay(work_day_input)
        self.assertIsInstance(work_day_parsed, WorkDay)
    
    def test__parseSchedulesToEmployeeWorkDays__raise_an_exception__when_format_is_invalid(self):
        file_location = os.path.join(SCRIPT_DIR, "data", "data_incorrect_1.txt")
        with self.assertRaises(InvalidFormatError):
            SchedulesFileModel(file_location)

    def test__parseSchedulesToEmployeeWorkDays__return_a_list__of_schedules(self):
        
        employee_work_days = EmployeeWorkDays("ANDRES")
        wd1 = parseWorkDay("MO10:00-12:00")
        wd2 = parseWorkDay("TH12:00-14:00")
        wd3 = parseWorkDay("SU20:00-21:00")
        employee_work_days.addWorkDay(wd1)
        employee_work_days.addWorkDay(wd2)
        employee_work_days.addWorkDay(wd3)
        
        expected = [employee_work_days]

        file_location = os.path.join(SCRIPT_DIR, "data", "data_correct.txt")
        result = SchedulesFileModel(file_location)
        self.assertEqual(result.employees_work_days, expected)

    
if __name__ == '__main__':
    unittest.main()