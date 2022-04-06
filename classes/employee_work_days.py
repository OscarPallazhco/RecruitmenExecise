from classes.employee import Employee
from classes.workday import WorkDay
from utils.exceptions.exceptions import InvalidFormatError


class EmployeeWorkDays:
    def __init__(self, employee_name, work_days = []):
        self.employee = Employee(employee_name)
        self.work_days = list(work_days)

    def __str__(self):
        return str(self.employee) + str(self.work_days)
    
    def __eq__(self, other):
        return self.employee == other.employee and \
            self.work_days == other.work_days
    def __repr__(self):
        return self.__str__()

    def addWorkDay(self, date:str, entry:int, departure:int):
        is_valid_data = self.__validate_work_day(date, entry, departure)
        if is_valid_data:
            self.work_days.append(WorkDay(date, entry, departure))
        else:
            raise InvalidFormatError()

    def addWorkDay(self, workDay: WorkDay):
        is_valid_data = self.__validate_work_day(workDay.date, workDay.entry, workDay.departure)
        if is_valid_data:
            self.work_days.append(workDay)
        else:
            raise InvalidFormatError()

    def getCantOfWorkDaysCoincidents(self, employee_work_days):
        amount = 0
        for work_day in self.work_days:
            for temp_work_day in employee_work_days.work_days:
                if work_day.isCoincident(temp_work_day):
                    amount+=1
        return amount
    
    def __validate_work_day(self, date:str, entry:int, departure:int):
        are_correct_types = type(date) == str and type(entry) == type(departure) == int
        if len(date) > 1 and are_correct_types:
            return True
        return False
