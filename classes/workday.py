class WorkDay:
    def __init__(self, date, entry, departure):
        self.date = date
        self.entry = entry
        self.departure = departure

    def __str__(self):
        return str(self.date) + str(self.entry) + str(self.departure)

    def __repr__(self):
        return self.__str__()

    def isCoincident(self, work_day):
        same_day = self.date == work_day.date
        firstCase = self.entry < work_day.entry and self.departure > work_day.entry and self.departure <= work_day.departure
        secondCase = self.entry >= work_day.entry and self.departure <= work_day.departure
        thirdCase = self.entry >= work_day.entry and self.entry < work_day.departure and self.departure > work_day.departure
        fourthCase = work_day.entry >= self.entry and work_day.departure <= self.departure
        return same_day and (firstCase or secondCase or thirdCase or fourthCase)
