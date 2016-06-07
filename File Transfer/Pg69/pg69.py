##PG 69/76
##
##Create a database  and table
##record last time the program ran the backup save in the table
##display last backup time on the gui
##use wxpython
##use sqlite

import shutil, tkFileDialog, wx, sqlite3, db_program
from Tkinter import *
import os,os.path,time
from datetime import datetime, timedelta

class createwindow:
    def __init__(self,master):
        #------------------Frame 1-------------------------
        #Declares the frame
        self.frame = Frame(win,height = 10, width= 200)
        self.frame.pack()

        #declares a label
        self.l = Label(win)
        self.l2 = Label(win,text="Back up wich directory?")

        self.LabelLastCp()
        
        self.l.pack()
        self.l2.pack()

        #------------------Frame 2---------------------------
        #Declares the frame
        self.frame1 = Frame(win, height = 500, width = 200)
        self.frame1.pack()

        #Declare the Entry box
        self.eb1 = Entry(self.frame1, width=20)
        self.eb2 = Entry(self.frame1, width=20)

        #declares the label
        self.l1 = Label(self.frame1,text="To wich directory?")        

        #Declare the Browse button
        self.b3 = Button(self.frame1, text = "Browse")
        self.b4 = Button(self.frame1, text = "Browse")
        self.b1 = Button(self.frame1, text = "Backup")
        self.b2 = Button(self.frame1, text = "Clear")

        #configures the buttons
        self.b1.config(command = self.but1)
        self.b2.config(command = self.but2)
        self.b3.config(command = self.but3)
        self.b4.config(command = self.but4)

        #packs the objects
        #self.filebox.pack()
        self.eb1.grid(row=0,column=0,columnspan =3, sticky=(W))
        self.b3.grid(row=0,column =3, sticky=(E))

        self.l1.grid(row=1,column = 1, columnspan =2)
        
        self.eb2.grid(row=2,column=0,columnspan =3, sticky=(W))
        self.b4.grid(row=2,column =3, sticky=(E))
        
        self.b1.grid(row=3,column=0,columnspan=2)
        self.b2.grid(row=3,column=2,columnspan=2)

        #self.eb1.insert(0,"C:\Users\Owner\Desktop\A")
        #self.eb2.insert(0,"C:\Users\Owner\Desktop\A")

#------------------------Saves files------------------------------
#Finds the path from and to then copies files that are new and leaves old files
    def but1(self):
        
        self.o = self.eb1.get()         #gets the dir path to copy from        
        self.out = os.listdir(self.o)   #Makes it readable by the for loop by declaring it as a directory
        self.outdir = self.o + "/"      #Adds a / to the end so files can be added to the end        
        self.into = self.eb2.get()      #Gets the destination file        

        self.curtime = datetime.now()                           #Gets Current time
        #self.yesterday = self.curtime-timedelta(hours =24)      #Gets a 24 hour period
        #self.oneday = self.curtime - self.yesterday             #Another form of one day
        
        self.lastcp = db_program.RetriveCp()

        
        print("self.lastcp : {}".format(self.lastcp))      
        #print (self.outdir)

        #For every file in directory check if new or old copy new
        for self.files in self.out:
            self.fpath = (str(self.outdir)+str(self.files))                 #Builds the path to each file
            self.t = datetime.fromtimestamp(os.path.getmtime(self.fpath))   #Gets time stampof file
            self.age = self.curtime - self.t                                #Checks the age of the file

            #if age of file is newer than 24 hrs copy to new floder
            if self.age < self.lastcp:
                #print ("Copied a young file {} to {}".format(self.files,self.into))
                shutil.copy(self.fpath, self.into)  #Performs the copy (from,to)
            else:
                #print ("{} is too old".format(self.files))
                pass
        #clears the Entry boxes  
        self.eb1.delete(0,END)
        self.eb2.delete(0,END)
                
        db_program.Checkpoint(self.curtime)
        self.LabelLastCp()



    def LabelLastCp(self):
        self.llcp = db_program.LastTime()
        print self.llcp
        self.l.config(text="Last backup: {} ".format(self.llcp))
        
                        
        

        

    #------------------------Empty Folder-------------------------
    #Empties the backupfolder to prove that test has been compleated.
    def but2(self):
        
        outdir = "C:\Users\Owner\Desktop\B\\"           #Dir to backup formatted to add file extention
        out = os.listdir("C:\Users\Owner\Desktop\B")    #Dir to backup formatted for the for loop
        into = "Recycle Bin"                            #Dir to trash can
        #For every file in backup move to trash
        for files in out:
            fpath = (str(outdir)+str(files))    #Dir to specific file
            shutil.move(fpath, into)            #Moves files to the trash
            
        print ("Moved files from: {}".format(outdir))
        print ("Into: {}".format(into))
        #Clears the entry boxes just for fun
        self.eb1.delete(0,END)
        self.eb2.delete(0,END)

    #---------------------------------Browse Buttons---------------------------------
    #Browse for Dir to check folder
    def but3(self):
        #Gui that allws user to select dir
        dirpath=tkFileDialog.askdirectory(parent=win,initialdir="/",title='Please select a directory')
        self.eb1.insert(0,dirpath)      #Fill entry box with dir
    #Brows for destination folder
    def but4(self):
        #GUI to allow user to select directory
        dirpath=tkFileDialog.askdirectory(parent=win,initialdir="/",title='Please select a directory')
        self.eb2.insert(0,dirpath)      #Fill entry box wit dir

#this is the main loop start and end
win = Tk()
fun = createwindow(win)
win.mainloop()
