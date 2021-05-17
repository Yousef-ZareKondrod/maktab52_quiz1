import jdatetime
from datetime import datetime

# part 1========================================================================
class TimeOpen:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)

        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        Time = jdatetime.datetime.now()
        # print(Time)
        self.file = open(self.filename, 'a')
        self.file.write(str(Time))
        self.file.close()


with TimeOpen('test2.txt', 'w') as f:
    f.write('hi it changed')


# part2==================================================================
class IteratorClass:

    def __init__(self, start_date, end_date, week_day):
        self.start_date = start_date
        self.end_date = end_date
        self.week_day = week_day

    def __iter__(self):
        return self

    def __next__(self):
        pass
