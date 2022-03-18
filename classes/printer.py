class Printer:
     
    @staticmethod
    def showResults(resultsTable):
        for employeeCouple, amountCoincidentDays in resultsTable.items():
            print("{}-{}: {}".format(employeeCouple[0], employeeCouple[1], amountCoincidentDays))
