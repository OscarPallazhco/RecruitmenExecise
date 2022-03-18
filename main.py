
import sys
from classes.schedules_file import SchedulesFile
from classes.business_logic import BusinessLogic
from classes.printer import Printer

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        schedules_source = SchedulesFile(filename)
        b_logic = BusinessLogic(schedules_source)
        results_table = b_logic.calculateAmountEmployeesCoincidents()
        Printer.showResults(results_table)
    else:
        print('Error: Se necesita el nombre del archivo')
        sys.exit(0)