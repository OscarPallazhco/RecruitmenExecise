import unittest
import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.employee import Employee
from classes.workday import WorkDay
from classes.employee_work_days import EmployeeWorkDays
from classes.business_logic import BusinessLogic

class WorkDayTest(unittest.TestCase):
    def test_isCoincident_differentDaysHoursCoincident(self):
        w0 = WorkDay("MO", 1000, 1200)
        w1 = WorkDay("TU", 900, 1300)
        self.assertEqual(w0.isCoincident(w1), False)

    def test_isCoincident_differentDaysHoursNotCoincident(self):
        w0 = WorkDay("MO", 1000, 1200)
        w1 = WorkDay("TU", 1200, 1400)
        self.assertEqual(w0.isCoincident(w1), False)

    def test_isCoincident_sameDaysHoursCoincident(self):
        w0 = WorkDay("MO", 1300, 1700)
        w1 = WorkDay("MO", 900, 1400)
        self.assertEqual(w0.isCoincident(w1), True)

    def test_isCoincident_sameDaysHoursNotCoincidents(self):
        w0 = WorkDay("MO", 1300, 1700)
        w1 = WorkDay("MO", 900, 1100)
        self.assertEqual(w0.isCoincident(w1), False)

class EmployeeWorkDaysTest(unittest.TestCase):
    def test_getCantOfWorkDaysCoincidents_correctAmountOfCoincidentDays(self):
        emp1 = Employee('JUAN')
        emp2 = Employee('PEDRO')
        work_day_0 = WorkDay("MO", 1300, 1700)
        work_day_1 = WorkDay("TU", 900, 1100)
        work_day_2 = WorkDay("TU", 1000, 1200)
        work_day_3 = WorkDay("WED", 900, 1100)
        empl_work_days_0= EmployeeWorkDays(emp1, [work_day_0, work_day_1])
        empl_work_days_1 = EmployeeWorkDays(emp2, [work_day_0, work_day_1, work_day_2, work_day_3])
        expected_coincident_days = 3
        self.assertEqual(empl_work_days_0.getCantOfWorkDaysCoincidents(empl_work_days_1), expected_coincident_days)

class BusinessLogicTest(unittest.TestCase):
    def test_calculate_correctAmountOfEmployeeCouple(self):
        fileLocation = os.path.join(SCRIPT_DIR, "..", "data", "data3.txt")
        bLogic = BusinessLogic(fileLocation)
        resultsTable = bLogic.calculate()
        amount_of_employee_couple = len(resultsTable)
        self.assertEqual(amount_of_employee_couple, 13)
        

            
      
if __name__ == '__main__':
   unittest.main()