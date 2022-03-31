import sys

from classes.employee_work_days import EmployeeWorkDays
from classes.schedules import Schedules
from utils.exceptions.exceptions import InvalidFormatError
from utils.parsers.parseData import parseWorkDay

class SchedulesFile(Schedules):

    employees_work_days = []

    def __init__(self, employees_work_days):
        self.employees_work_days = employees_work_days
    
    def load_employees_schedules(self) -> list:
        return self.employees_work_days


class SchedulesFileModel(SchedulesFile):

    def __init__(self, filename):
        self.filename = filename
        rawWorkingSchedules = self.__loadWorkingSchedules()
        employees_work_days = self.__parseSchedulesToEmployeeWorkDays(rawWorkingSchedules)
        super().__init__(employees_work_days)

    def __loadWorkingSchedules(self):
        try:
            f = open(self.filename, 'r')
        except OSError:
            print("Error: No se puede abrir el archivo:", self.filename)
            sys.exit()
        with f:
            lines = f.readlines()
            f.close()
            return lines

    def __parseSchedulesToEmployeeWorkDays(self, rawWorkingSchedules):
        result = []
        try:
            for line_index in range(len(rawWorkingSchedules)):
                employee_name, work_days = rawWorkingSchedules[line_index].strip("\n").split("=")
                employee_work_days = EmployeeWorkDays(employee_name)
                for work_day_raw in work_days.split(","):
                    employee_work_days.addWorkDay(parseWorkDay(work_day_raw))
                result.append(employee_work_days)
            return result
        except Exception:
            raise InvalidFormatError()
