import sys
from classes.employee_work_days import EmployeeWorkDays

class BusinessLogic:

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
            for i in range(len(rawWorkingSchedules)):
                employee_name, work_days = rawWorkingSchedules[i].strip("\n").split("=")
                employee_work_days = EmployeeWorkDays(employee_name)
                for work_day in work_days.split(","):
                    date = work_day[0:2]
                    hours = work_day[2:]
                    entry, departure = hours.split("-")
                    entry = int(entry.replace(":", ""))
                    departure = int(departure.replace(":", ""))
                    employee_work_days.addWorkDay(date, entry, departure)
                self.employees_work_days.append(employee_work_days)
        except Exception as exc:
            print("Error: Estructura del archivo no es válida.\nEjemplo:\nJUAN=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00")
            sys.exit(0)

    def calculate(self):
        checked = []
        resultsTable = {}
        for employee_work_days in self.employees_work_days:
            for temp_employee_work_days in checked:
                if employee_work_days != temp_employee_work_days:
                    employee1 = employee_work_days.employee
                    employee2 = temp_employee_work_days.employee
                    amount = employee_work_days.getCantOfWorkDaysCoincidents(temp_employee_work_days)
                    if amount > 0:
                        employeeCouple = (employee1, employee2)
                        resultsTable[employeeCouple] = amount
            checked.append(employee_work_days)
        return resultsTable
    
    def showResults(self, resultsTable):
        for employeeCouple, amountCoincidentDays in resultsTable.items():
            print("{}-{}: {}".format(employeeCouple[0], employeeCouple[1], amountCoincidentDays))
