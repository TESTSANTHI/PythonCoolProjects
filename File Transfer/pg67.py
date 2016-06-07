#PG 67/76
#
#check a file for recently modified files and place any
#that have been created or modified in the last 24 hours to
#a new folder
#

import shutil
from Tkinter import *
import os,os.path,time
from datetime import datetime, timedelta

class createwindow:
    def __init__(self,master):
        #Declares the frame
        self.frame = Frame(win)
        
        self.frame.pack()

        self.b1 = Button(self.frame, text = "Copy")
        self.b2 = Button(self.frame, text = "Trash")

        self.b1.config(command = self.but1)
        self.b2.config(command = self.but2)

        self.b1.pack(side=LEFT)
        self.b2.pack(side=LEFT)

        self.l = Label(win,text="Press a button to move files.")
        self.l.pack()


    def but1(self):
        outdir = "C:\Users\Owner\Desktop\A\\"
        out = os.listdir("C:\Users\Owner\Desktop\A")
        into = "C:\Users\Owner\Desktop\B"
        curtime = datetime.now()
        yesterday = curtime-timedelta(hours =24)
        tomorrow = curtime+timedelta(hours =24)
        oneday = curtime - yesterday

        
        for files in out:
            fpath = (str(outdir)+str(files))
            t = datetime.fromtimestamp(os.path.getmtime(fpath))
            age = curtime - t

            #if file is newer than 24 hrs copy to new floder
            if age < oneday:
                print ("a young file")
                shutil.copy(fpath, into)
            else:
                print files
                print ("is too old")
            
           
            
            #print ("File: {}, Modified: {}, Created: {}".format(files,filestat,filestatm))
            
        #print ("Moved files from: {}".format(outdir))
        #print ("Into: {}".format(into))

    def but2(self):
        outdir = "C:\Users\Owner\Desktop\B\\"
        out = os.listdir("C:\Users\Owner\Desktop\B")
        into = "Recycle Bin"
        for files in out:
            fpath = (str(outdir)+str(files))
            shutil.move(fpath, into)
            
        print ("Moved files from: {}".format(outdir))
        print ("Into: {}".format(into))

win = Tk()
fun = createwindow(win)
win.mainloop()
