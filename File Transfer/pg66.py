#PG 66/76
#
#Move the files from one folder to another with the clock of a button
#print out the file path of each file
#Folder A should not contain files anylonger
#
#

import shutil
from Tkinter import *
import os

class createwindow:
    def __init__(self,master):
        #Declares the frame
        self.frame = Frame(win)
        
        self.frame.pack()

        self.b1 = Button(self.frame, text = "A->B")
        self.b2 = Button(self.frame, text = "A<-B")

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
        for files in out:
            fpath = (str(outdir)+str(files))
            shutil.move(fpath, into)
            
        print ("Moved files from: {}".format(outdir))
        print ("Into: {}".format(into))

    def but2(self):
        outdir = "C:\Users\Owner\Desktop\B\\"
        out = os.listdir("C:\Users\Owner\Desktop\B")
        into = "C:\Users\Owner\Desktop\A"
        for files in out:
            fpath = (str(outdir)+str(files))
            shutil.move(fpath, into)
            
        print ("Moved files from: {}".format(outdir))
        print ("Into: {}".format(into))

win = Tk()
fun = createwindow(win)
win.mainloop()
