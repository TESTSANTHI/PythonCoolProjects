#DataBASE PROGRAM FOR GUI project

import sqlite3, types
from datetime import datetime, timedelta

conn = sqlite3.connect("Storelogs.db")
c=conn.cursor()

#Creates the table if it doesn't exist
def CreateTable():
    #Creates te table to store checkpoints if doesn't exists already
    #c.execute('''DROP TABLE IF EXISTS Checkpoints''')
    c.execute('''CREATE TABLE IF NOT EXISTS Checkpoints\
                    (Saves INTEGER PRIMARY KEY,\
                    UniStamp text,\
                    DateTime text)''')
    
    conn.commit()
    #print("created table")
    
#Saves the checkpoint
def Checkpoint(ustamp=datetime.now()):
    ustamp = ustamp                                     #Gets Current time
    date = ustamp.strftime("%m/%d/%Y %H:%M:%S")         #Formats ustamp as MM/DD/YYYY H:M:S
    values = [(ustamp,date)]                            #Places values in array
    print("Ustamp = {}".format(ustamp))
    print("Date = {}".format(date))  

    c.executemany('INSERT INTO Checkpoints\
                    (UniStamp, DateTime)\
                    VALUES(?,?)',values)
    
    #print("Saved Checkpooint")
    conn.commit()
    
    


##Retrieves last checkpoint from database
def RetriveCp():
    #Variables
    curtime = datetime.now()
    yesterday = curtime-timedelta(hours =24)
    lastcpu = conn.execute("SELECT * FROM Checkpoints").fetchall()
    i = len(lastcpu)-1
    #print i
    try:
        print (lastcpu[i])
        lastcpu = lastcpu[i]
        print (lastcpu[1])
        print (curtime)
        lastcpu = lastcpu[1]
        lastcpu = curtime - datetime.strptime(lastcpu, '%Y-%m-%d %H:%M:%S.%f')
        #type(lastcpu) is types.UnicodeType
        
        #self.lastcp = self.curtime - datetime.strptime(self.lastcp, '%Y-%m-%d %H:%M:%S.%f')                                               #2016-04-27 13:02:39.734000
    except:
        print ("didn't work")
        lastcpu = curtime - yesterday
    return lastcpu
     
    conn.commit()
    conn.close()

def LastTime():
    lastcpu = conn.execute("SELECT * FROM Checkpoints").fetchall()
    i = len(lastcpu)-1
    #print i
    try:
        #print lastcpu[i]
        lastcpu = lastcpu[i]
        return  lastcpu[2]
    except:
        return "Unkown"


CreateTable()
