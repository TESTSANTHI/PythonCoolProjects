#PG 68/76
#
#check a file for recently modified files and place any
#that have been created or modified in the last 24 hours to
#a new folder
#
#Introduce a gui that allows users to find a specific file and
#update as needed.

import shutil, tkFileDialog
from Tkinter import *
import os,os.path,time
from datetime import datetime, timedelta

class createwindow:
    def __init__(self,master):
        #------------------Frame 1-------------------------
        #Declares the frame
        self.frame = Frame(win)
        self.frame.pack()

        #declares a label
        self.l = Label(win,text="Back up wich directory?")
        self.l.pack()



        #------------------Frame 2---------------------------
        #Declares the frame
        self.frame1 = Frame(win)
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
        self.eb1.grid(row=0,column=0,columnspan =3)
        self.b3.grid(row=0,column =3)

        self.l1.grid(row=1,column = 1, columnspan =2)
        
        self.eb2.grid(row=2,column=0,columnspan =3)
        self.b4.grid(row=2,column =3)
        
        self.b1.grid(row=3,column=0,columnspan=2)
        self.b2.grid(row=3,column=2,columnspan=2)


    def but1(self):

        self.o = self.eb1.get()
        self.out = os.listdir(self.o)
        self.outdir = self.o + "/"        
        self.into = self.eb2.get()
        self.curtime = datetime.now()
        self.yesterday = self.curtime-timedelta(hours =24)
        self.tomorrow = self.curtime+timedelta(hours =24)
        self.oneday = self.curtime - self.yesterday
        print (self.outdir)
        
        for self.files in self.out:
            self.fpath = (str(self.outdir)+str(self.files))
            self.t = datetime.fromtimestamp(os.path.getmtime(self.fpath))
            self.age = self.curtime - self.t

            #if file is newer than 24 hrs copy to new floder
            if self.age < self.oneday:
                print ("Copied a young file {} to {}".format(self.files,self.into))
                shutil.copy(self.fpath, self.into)
            else:
                print ("{} is too old".format(self.files))
            
        self.eb1.delete(0,END)
        self.eb2.delete(0,END)
            
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
        self.eb1.delete(0,END)
        self.eb2.delete(0,END)

    def but3(self):
        dirpath=tkFileDialog.askdirectory(parent=win,initialdir="/",title='Please select a directory')
        self.eb1.insert(0,dirpath)

    def but4(self):
        dirpath=tkFileDialog.askdirectory(parent=win,initialdir="/",title='Please select a directory')
        self.eb2.insert(0,dirpath)
        
win = Tk()
fun = createwindow(win)
win.mainloop()
