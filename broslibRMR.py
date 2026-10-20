import sqlite3
import random
import datetime as dt
from datetime import timedelta

#def convert_date(val):
#    """Convert ISO 8601 date to datetime.date object."""
#return date.fromisoformat(val.decode())

#sqlite3.register_converter("date", convert_date)

startdayvalue = dt.date(2026,10,20)
startdayvaluenextday = startdayvalue + timedelta(days=1)
startdayvaluestr = startdayvalue.strftime("%Y-%m-%d")
startdayvaluenextdaystr = startdayvaluenextday.strftime("%Y-%m-%d")
print("the current startdate is: ", startdayvaluestr)
print("the current startdate+1 is: ", startdayvaluenextdaystr)
startdaynum = (startdayvalue).isoweekday()
match (startdaynum):
    case(1):
        startdayabbrev = "MON"
    case(2):
        startdayabbrev = "TUE"
    case(3):
        startdayabbrev = "WED"
    case(4):
        startdayabbrev = "THU"
    case(5):
        startdayabbrev = "FRI"
    case(6):
        startdayabbrev = "SAT"
    case(7):
        startdayabbrev = "SUN"
con = sqlite3.connect("broslibDB.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cur = con.cursor()
cur1 = con.cursor()
cur.execute("SELECT booknum, room, bcase, shelf, position, title, author FROM books")
records = cur.fetchall()
print("Total current books are:  ", len(records))


rvar1 = random.randint(1, 15)
rvar2 = (rvar1, )

cur.execute("SELECT booknum, room, bcase, shelf, position, title, author FROM books WHERE booknum =?",  (rvar2))
records = cur.fetchall()
print("Number of selected books:  ", len(records))
print("Printing each selected book")
for row in records:
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
    print(row[4])
    print(row[5])
    print(row[6])
    bookdata = [
    (startdayabbrev, startdayvaluestr, row[0], row[1], row[2], row[3], row[4], row[5], row[6], "good read")
    ]
    cur.executemany("INSERT INTO readings VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", bookdata)
con.commit()
cur.execute("SELECT day, date, booknum, room, bcase, shelf, position, title, author, notes FROM readings")
records = cur.fetchall()
print("Total current readings are:  ", len(records))
print("Printing each reading")
for row in records:
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
    print(row[4])
    print(row[5])
    print(row[6])
    print(row[7])
    print(row[8])
    print(row[9])
cur.close()