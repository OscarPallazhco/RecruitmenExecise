import sys

from classes.employee_work_days import EmployeeWorkDays
from classes.schedules import Schedules
from utils.parsers.parseData import parseWorkDay

class SchedulesFile(Schedules):

    employees_work_days = []

    def __init__(self, filename):
        self.filename = filename
        self.__parseSchedulesToEmployeeWorkDays()

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

    def __parseSchedulesToEmployeeWorkDays(self):
        rawWorkingSchedules = self.__loadWorkingSchedules()
        try:
            for line_index in range(len(rawWorkingSchedules)):
                employee_name, work_days = rawWorkingSchedules[line_index].strip("\n").split("=")
                employee_work_days = EmployeeWorkDays(employee_name)
                for work_day_raw in work_days.split(","):
                    employee_work_days.addWorkDay(parseWorkDay(work_day_raw))
                self.employees_work_days.append(employee_work_days)
        except Exception as exc:
            print("Error: Estructura del archivo no es válida.\nEjemplo:\nJUAN=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00")
            sys.exit(0)
    
    def load_employees_schedules(self) -> list:
        return self.employees_work_days
