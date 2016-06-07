#DAtabase stuffs
#
#

import sqlite3

#connect to the database
conn = sqlite3.connect('webStorage.db')
c = conn.cursor()


#creates a table
def createtable():
    c.executescript('''
DROP TABLE IF EXISTS webexamples;

CREATE TABLE IF NOT EXISTS webexamples
(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
ExampleName STR NULL,
ExampleText STR NULL,
FilePath STR NULL);
''')
    conn.commit()

#Store data in database
def storeExample(exampleName="test",exampleText="testt",filepath="test.html"):
    val_str = (exampleName,exampleText,filepath)
    c.executescript('''
INSERT INTO webexamples
(ExampleName, ExampleText,FilePath)
VALUES
{};'''.format(val_str))
    conn.commit

#retrieve data from data base
def retrieveExample(exampleID="1"):
    sql_str = "SELECT ExampleName,ExampleText,FilePath FROM webexamples WHERE ID = {}"\
              .format(exampleID)
    cursor = conn.execute(sql_str)
    exampleFile = cursor.fetchall()
    return exampleFile

#Counts the amount of examples
def countAll():
    sql_str = ('''SELECT COUNT(*) FROM webexamples''')
    cursor = conn.execute(sql_str)
    count = cursor.fetchall()
    count = count[0]
    count = count[0]
    
    return count









createtable()
storeExample()
storeExample()
retrieveExample()
countAll()
