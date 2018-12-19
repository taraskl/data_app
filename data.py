# Read a CSV file in Python, libe-by-line, by Jeff Heaton (http://www.jeffheaton.com/tutorials/)
import codecs
import csv

import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

# Delete table
# c.execute("DROP TABLE data")

# Check, create table
try:
    c.execute("SELECT * FROM data")
    print('Data table already exist')
except:    
    c.execute('''CREATE TABLE data
        (entity text, value real, string text)''')
    print('Data table was created')



FILENAME = "data/test-1.csv"

ENCODING = 'cp437'
with codecs.open(FILENAME, "r", ENCODING) as fp:
    reader = csv.reader(fp)
    headers = next(reader)
    s=headers[0][9:]

if s == 'cp437':
    ENCODING = 'cp437'
    with codecs.open(FILENAME, "r", ENCODING) as fp:
        reader = csv.reader(fp)

    #     # read CSV headers
        headers = next(reader)
        print(headers)

        # # read rest of file
        for row in reader:
            # Print each row
            print(row[0], row[1], row[2])
            c.execute("INSERT INTO data VALUES (?, ?, ?)", (row[0], row[1], row[2]))
            conn.commit()

        #     # Print individual fields of the row
        #     # print("{},{},{},{} = {}".format(row[0],row[1],row[2],row[3],row[4]))

elif s == 'utf-8':
    ENCODING = 'utf-8'
    with codecs.open(FILENAME, "r", ENCODING) as fp:
        reader = csv.reader(fp)

    #     # read CSV headers
        headers = next(reader)
        print(headers)

        # # read rest of file
        for row in reader:
            # Print each row
            print(row[0], row[1], row[2])
            c.execute("INSERT INTO data VALUES (?, ?, ?)", (row[0], row[1], row[2]))
            conn.commit()

elif s == 'ascii':
    ENCODING = 'ascii'
    with codecs.open(FILENAME, "r", ENCODING) as fp:
        reader = csv.reader(fp)

    #     # read CSV headers
        headers = next(reader)
        print(headers)

        # # read rest of file
        for row in reader:
            # Print each row
            print(row[0], row[1], row[2])
            c.execute("INSERT INTO data VALUES (?, ?, ?)", (row[0], row[1], row[2]))
            conn.commit() 

conn.close()