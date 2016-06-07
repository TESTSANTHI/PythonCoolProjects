##A program that will store job applications into a data base
##
##
##
##
##
##
##
##

import sqlite3
from datetime import datetime

conn = sqlite3.connect("Storelogs.db")
c=conn.cursor()

#create the table if it doesnt exsist
def CreateTable():
    #Creates te table to store checkpoints if doesn't exists already
    #c.execute('''DROP TABLE IF EXISTS Checkpoints''')
    c.execute('''CREATE TABLE IF NOT EXISTS sentApplications\
                    (\
                    Applications INTEGER PRIMARY KEY,\
                    Date text,\
                    Company text,\
                    Website text,\
                    Position text,
                    PostID INTEGER
                    )''')
    
    conn.commit()

def SaveApply(postID, company = "", website = "", position = ""):

    curdate = datetime.now()
    curdate = curdate.strftime('%m/%d/%Y')

    values = [(curdate, company, website, position, postID)]

    c.executemany('INSERT INTO sentApplications \
                  (Date, Company, Website, Position, PostID)\
                  VALUES(?,?,?,?,?)',values)

CreateTable()

