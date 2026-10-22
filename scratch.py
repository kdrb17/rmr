# code for generating an array of random numbers
# import random

wklychoice = [0, 0 , 0, 0, 0]
for x in range(6):
        wklychoice[x-1] = rvar1 = random.randint(1, 5)
            
print(wklychoice)

# code for writing each selected book to the readings table
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