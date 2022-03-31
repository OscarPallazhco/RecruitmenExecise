
import sys
from classes.schedules_file import SchedulesFileModel
from classes.business_logic import BusinessLogic
from classes.printer import Printer
from utils.exceptions.exceptions import InvalidFormatError

if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            filename = sys.argv[1]
            schedules_source = SchedulesFileModel(filename)
            b_logic = BusinessLogic(schedules_source)
            results_table = b_logic.calculateAmountEmployeesCoincidents()
            Printer.showResults(results_table)
        except InvalidFormatError as e:
            print("Something was wrong: ", e)
    else:
        print('Error: Se necesita el nombre del archivo')
        sys.exit(0)