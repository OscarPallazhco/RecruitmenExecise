from classes.employee import Employee
from classes.workday import WorkDay


class EmployeeWorkDays:
    def __init__(self, employee_name, work_days = []):
        self.employee = Employee(employee_name)
        self.work_days = list(work_days)

    def __str__(self):
        return str(self.employee) + str(self.work_days)

    def __repr__(self):
        return self.__str__()

    def addWorkDay(self, date:str, entry:int, departure:int):
        self.work_days.append(WorkDay(date, entry, departure))
    
    def addWorkDay(self, workDay: WorkDay):
        self.work_days.append(workDay)

    def getCantOfWorkDaysCoincidents(self, employee_work_days):
        amount = 0
        for work_day in self.work_days:
            for temp_work_day in employee_work_days.work_days:
                if work_day.isCoincident(temp_work_day):
                    amount+=1
        return amount
