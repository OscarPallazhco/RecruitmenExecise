
import sys
from classes.business_logic import BusinessLogic

if __name__ == '__main__':
    if len(sys.argv) == 2:
        bLogic = BusinessLogic(sys.argv[1])
        resultsTable = bLogic.calculate()
        bLogic.showResults(resultsTable)
    else:
        print('Error: Se necesita el nombre del archivo')
        sys.exit(0)