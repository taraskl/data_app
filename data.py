# Read a CSV file in Python, libe-by-line, by Jeff Heaton (http://www.jeffheaton.com/tutorials/)
import codecs
import csv

import sqlite3
import os

conn = sqlite3.connect('data.sqlite3.db')
c = conn.cursor()

# Delete table
try:
    c.execute("DROP TABLE data")
except:
    pass

# Check, create table
try:
    c.execute("SELECT * FROM data")
    print('Data table already exist')
except:    
    c.execute('''CREATE TABLE data
        (entity text, value real, string text)''')
    print('Data table was created')


#WRITE YOUR DIRECTORY OF DATA
path = '/home/taras/work/ActiveWizards/data_app/data'

for FILENAME in os.listdir(path):

    ENCODING = 'cp437'
    with codecs.open(f"data/{FILENAME}", "r", ENCODING) as fp:
        reader = csv.reader(fp)
        headers = next(reader)
        s=headers[0][9:]

    if s == 'cp437':
        ENCODING = 'cp437'
        with codecs.open(f"data/{FILENAME}", "r", ENCODING) as fp:
            reader = csv.reader(fp)
        #     # read CSV headers
            try:
                headers = next(reader)
                # # read rest of file
                for row in reader:
                    # Print each row
                    c.execute("INSERT INTO data VALUES (?, ?, ?)", (row[0], row[1], row[2]))
                    conn.commit()
            except:
                print(f"Was error in file {FILENAME}") 

    elif s == 'utf-8':
        ENCODING = 'utf-8'
        with codecs.open(f"data/{FILENAME}", "r", ENCODING) as fp:
            reader = csv.reader(fp)
        #     # read CSV headers
            try:
                headers = next(reader)
            # # read rest of file
                for row in reader:
                    # Print each row
                    c.execute("INSERT INTO data VALUES (?, ?, ?)", (row[0], row[1], row[2]))
                    conn.commit()
            except:
                print(f"Was error in file {FILENAME}")    
     

    elif s == 'ascii':
        ENCODING = 'ascii'
        with codecs.open(f"data/{FILENAME}", "r", ENCODING) as fp:
            reader = csv.reader(fp)
        #     # read CSV headers
            try:
                headers = next(reader)
                # # read rest of file
                for row in reader:
                    # Print each row
                    c.execute("INSERT INTO data VALUES (?, ?, ?)", (row[0], row[1], row[2]))
                    conn.commit() 
            except:
                print(f"Was error in file {FILENAME}") 

conn.close()