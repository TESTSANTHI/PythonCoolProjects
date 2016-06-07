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

CREATE TABLE IF NOT EXISTS webexamples
(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
ExampleName STR NULL,
ExampleText STR NULL,
FilePath STR NULL);
''')
    conn.commit()

#Store data in database
def storeExample(exampleName,exampleText,filepath):
    val_str = (exampleName,exampleText,filepath)
    print (str(val_str))
    ifnotexist = ('''
INSERT INTO webexamples(ExampleName,ExampleText,FilePath) 
SELECT '{}','{}','{}' 
WHERE NOT EXISTS(SELECT ExampleName FROM webexamples WHERE ExampleName = '{}' 
);'''.format(exampleName,exampleText,filepath,exampleName))

    ifexist = ('''
INSERT INTO webexamples(ExampleText,FilePath) 
SELECT '{}','{}'
WHERE (SELECT ExampleName FROM webexamples WHERE ExampleName = '{}' \
);'''.format(exampleText,filepath,exampleName,exampleText,filepath))

    print("Number of Rows: {}".format(countAll()))
    conn.execute(ifnotexist)
    conn.execute(ifexist)
    
    
    conn.commit()

#retrieve data from data base
def retrieveExample(exampleID='1'):

    sql_str = "SELECT * FROM webexamples WHERE ID = {}"\
              .format(exampleID)
    
    print(sql_str)
    cursor = conn.execute(sql_str)
    exampleFile = cursor.fetchall()
    print (exampleFile)
    print("Number of Rows: '{}'".format(countAll()))
    exampleFile = exampleFile[0]
    
    return exampleFile
  

#Counts the amount of examples
def countAll():
    sql_str = ('''SELECT COUNT(*) FROM webexamples''')
    cursor = conn.execute(sql_str)
    count = cursor.fetchall()
    count = count[0]
    count = count[0]

    return count

#deletes row from database
def droprow(exampleID):
    print("exampleID = {}".format(exampleID))
    del_str = ('''DELETE FROM webexamples WHERE ID = {}; '''.format(exampleID))
    cursor = conn.execute(del_str)
    update_str = ('''
BEGIN TRANSACTION;
CREATE TEMPORARY TABLE t1_backup(
ExampleName STR NULL,
ExampleText STR NULL,
FilePath STR NULL
);
INSERT INTO t1_backup SELECT ExampleName,ExampleText,FilePath FROM webexamples;
DROP TABLE webexamples;
CREATE TABLE IF NOT EXISTS webexamples
(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
ExampleName STR NULL,
ExampleText STR NULL,
FilePath STR NULL);
INSERT INTO webexamples (ExampleName,ExampleText,FilePath)SELECT ExampleName,ExampleText,FilePath FROM t1_backup;
DROP TABLE t1_backup;
COMMIT;

''')
    print(update_str)
    cursor = conn.executescript(update_str)
    
    conn.commit()
    #print(sql_str)
    
    




createtable()

