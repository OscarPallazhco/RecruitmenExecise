
from classes.workday import WorkDay
from utils.exceptions.exceptions import InvalidFormatError

def parseWorkDay(raw_work_day):
    try:
        date = raw_work_day[0:2]
        hours = raw_work_day[2:]
        raw_entry, raw_departure = hours.split("-")
        entry = int(raw_entry.replace(":", ""))
        departure = int(raw_departure.replace(":", ""))
        return WorkDay(date, entry, departure)
    except:
        raise InvalidFormatError()
