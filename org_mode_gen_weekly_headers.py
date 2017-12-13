# Generate weekly todo headings for the whole year.
#
# Usage:
#   python gen_year.py > TODO.org
#

import datetime

dt = datetime.date.today()
(year, month, day, h, m, s, weekday, yd, x) = dt.timetuple()


# Find the first Monday in the year
dt = datetime.date(year, 1, 1)
while True:
    (year, month, day, h, m, s, weekday, yd, x) = dt.timetuple()
    # print("{0}-{1:02d}-{2:02d} {3}".format(year, month, day, weekday))
    if weekday == 0:  # weekday == 0 is Monday
        break
    dt = dt + datetime.timedelta(days=1)

# Print out the weeks in org-mode format
for week in range(52):
    (year, month, day, h, m, s, weekday, yd, x) = dt.timetuple()
    print("* Week {0:2d} <{1}-{2:02d}-{3:02d}>"
          .format(week + 1, year, month, day))
    dt = dt + datetime.timedelta(weeks=1)
