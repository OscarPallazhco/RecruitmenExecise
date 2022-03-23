
from typing import Dict
from classes.schedules import Schedules

class BusinessLogic:

    employees_work_days = []

    def __init__(self, schedules_source: Schedules):
        self.employees_work_days = schedules_source.load_employees_schedules()

    def calculateAmountEmployeesCoincidents(self) -> Dict:
        checked = []
        resultsTable = {}
        for employee_work_days in self.employees_work_days:
            for temp_employee_work_days in checked:
                if employee_work_days != temp_employee_work_days:
                    employee1 = employee_work_days.employee
                    employee2 = temp_employee_work_days.employee
                    amount = employee_work_days.getCantOfWorkDaysCoincidents(
                        temp_employee_work_days)
                    if amount > 0:
                        employeeCouple = (employee1, employee2)
                        resultsTable[employeeCouple] = amount
            checked.append(employee_work_days)
        return resultsTable
