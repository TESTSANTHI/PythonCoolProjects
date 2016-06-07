##Create a program that will create a cover letter base off a few
##Key words
##
##
##
##
##

import wx,CLWeb,db_program

PContent = "Dear {},\n\n\
My name is Andrew Earls. I am a software developer with an interest in all things \
computers. I am writing you about you the {} position you posted on craigslist.\n \n\
As I looked into {}, I was impressed by the endless possibilities that I would \
be a part of if I had the chance to work amongst your highly skilled team of \
professionals. This would be a fantastic fit for us as I believe I could be of \
use to your team!\n \n\
I'm attaching my resume. Please take a look and give me a call. It seems like \
you're doing work I really could contribute to.\n \n\
Sincerely,\n\
Andrew"

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(800,600))

        #creates the Panels
        mainPanel = wx.Panel(self)
        self.panel = wx.Panel(mainPanel,-1, size=(800,600))
        
        #-----------------------PANEL ONE------------------------------------
        # Labels
        self.lblManager = wx.StaticText\
                       (self.panel, -1, label="What is the name of the"\
                        + " Hiring manager?",pos=(90,50))
        self.lblEmployer = wx.StaticText\
                       (self.panel, -1, label="What is the name of the"\
                        + " Company?",pos=(90,100))
        self.lblPosition = wx.StaticText\
                       (self.panel, -1, label="What is the name of the"\
                        + " Position?",pos=(90,150))

        # Single line text boxes (SLTB)
        self.tbCraigslist = wx.TextCtrl(self.panel,value = "Craigslist Posting", size=(500, -1), pos=(90,20))
        self.tbManager = wx.TextCtrl(self.panel, size=(600, -1), pos=(90,70))
        self.tbEmployer = wx.TextCtrl(self.panel, size=(600, -1), pos=(90,120))
        self.tbPosition = wx.TextCtrl(self.panel, size=(600, -1), pos=(90,170))

        # Multi line text box (MLTB)
        self.mltbContent = wx.TextCtrl\
                    (self.panel, -1,size=(600, 275), pos=(90,220), style=wx.TE_MULTILINE)
        self.mltbContent.SetInsertionPoint(0)

        # Buttons (BTN)
        fill = wx.Button(self.panel, label="Fill", pos=(90, 500))
        save = wx.Button(self.panel, label="Save", pos=(200, 500))        
        scrape = wx.Button(self.panel, label="Scrape", pos=(600, 20))

        #bind button
        fill.Bind(wx.EVT_BUTTON, self.Fill)
        save.Bind(wx.EVT_BUTTON, self.Save)
        scrape.Bind(wx.EVT_BUTTON, self.Scrape)

    #------------------------------DEF's------------------------------
        
    #Fill in the blank data with data from the tb's
    def Fill(self,event):
        # get data from SLTB's
        Manager = self.tbManager.GetValue()
        Employer = self.tbEmployer.GetValue()
        Position = self.tbPosition.GetValue()

        #check to see if SLTB's are empty
        if (Manager == ""):
            Manager = "Hiring Manager"
        if (Employer == ""):
            Employer = "your company"

        #Delete all values from contents
        self.mltbContent.Clear()
        
        #Fill content box with coverletter
        self.mltbContent.AppendText(PContent.format(Manager,Position,Employer))

    #Scrape designated web page, fill empty SLTB's
    def Scrape(self,event):
        #retrieve the webPath
        webPath = self.tbCraigslist.GetValue()
        Position = CLWeb.findPosition(webPath)

        #check to see if position SLTB is empty
        dummy = self.tbPosition.GetValue()
        if (dummy == ""):
            self.tbPosition.SetValue(Position)

    #commit to database
    def Save(self, event):
        #Gather necessary information
        webPath = self.tbCraigslist.GetValue()
        Employer = self.tbEmployer.GetValue()
        Position = self.tbPosition.GetValue()
        PostID = CLWeb.findPostID(webPath)
        #save to data base
        db_program.SaveApply(PostID,Employer,webPath,Position)
        
        

        
        
    
        


#------------------ Main loop -----------------
app = wx.App()
frame = Frame("Cover Letter")
frame.Show()
app.MainLoop()

