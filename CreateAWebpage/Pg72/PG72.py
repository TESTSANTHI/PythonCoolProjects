#HTML page creation
#
##Create a gui with with wx
##Allow useres to imput their own  body text
##
##
##
##

import webbrowser,os.path,wx

# Declares the frame class and opens the window
class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None,\
          title=title, size=(800,600))
        
        #creates the wx panel
        panel = wx.Panel(self)

        # Creating the file menu bar
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        publishItem = fileMenu.Append(wx.NewId(), "Publish")
        clearItem = fileMenu.Append(wx.NewId(), "Clear")
        exitItem = fileMenu.Append(wx.NewId(), "Exit")
        menuBar.Append(fileMenu, "File")

        # Binds the file menue options
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.publishWebpage, publishItem)
        self.Bind(wx.EVT_MENU, self.clearBoxes, clearItem)
        self.Bind(wx.EVT_MENU, self.exitProgram, exitItem)
        
        self.CreateStatusBar()

        # Labels
        self.webNameLabel = wx.StaticText\
                       (panel, -1, label="What do you want to name you webpage?",pos=(90,50))
        self.webContentLabel = wx.StaticText\
                          (panel, -1, label="Enter the content of your webpage:",pos=(90,130))
        # Single line text boxes
        self.websiteName = wx.TextCtrl(panel, size=(450, -1), pos=(90,70))

        # Multi line text box
        self.multiText = wx.TextCtrl\
                    (panel, -1,"test",size=(600, 275), pos=(90,150), style=wx.TE_MULTILINE)
        self.multiText.SetInsertionPoint(0)

        # Buttons
        createWebpage = wx.Button(panel, label="Create New Webpage", pos=(555, 69))
        publishBtn = wx.Button(panel, label="Publish", pos=(605, 450))
        clearBtn = wx.Button(panel, label="Clear", pos=(90, 450))

        # Bind delete button to function
        publishBtn.Bind(wx.EVT_BUTTON, self.publishWebpage)
        clearBtn.Bind(wx.EVT_BUTTON, self.clearBoxes)
        createWebpage.Bind(wx.EVT_BUTTON, self.createWebpage)

    #Exit the program
    def exitProgram(self, event):
        self.Destroy()
        
    #Creates an html file for given filename
    def createWebpage(self,event):
        self.filename = self.websiteName.GetValue() + ".html"
        if self.filename != '':
            self.output = open(self.filename,"w")
            self.output.close()
        print("Create web page")
    # Clear all boxes
    def clearBoxes(self,event):
        self.websiteName.Clear()
        self.multiText.Clear()
        print("Clear the boxes")

    #Create a new html file if one doesnt exist and outputs content
    def publishWebpage(self,event):
        self.filename = self.websiteName.GetValue() + ".html"
        self.text = self.multiText.GetValue()
        self.content = self.formatText(self.filename, self.text)
        
        if self.filename != '':
            self.output = open(self.filename,"w")
            self.output.write(self.content)
            self.output.close()
        self.browseLocal(self.filename)
        
        print("Publish webpage")

    #Opens the html file in a webbrowser for the user to see
    def browseLocal(self, filename):        
        webbrowser.open("file:///" + os.path.abspath(filename))

        
#-----------------------TEXT FORMAT-----------------------------
#Formats the conent before outputting to html file
    def formatText(self, filename,text):
        self.contentBeg = '''
<html>
<head>
<title>
'''
        self.contentMid = '''
</title>
</head>
<body>
'''
        self.contentEnd = '''
</body>
</html>
'''
        self.text = self.contentBeg + filename + self.contentMid + text + self.contentEnd
        print(self.text)
        return self.text
        
#-----------------------TEXT FORMAT-----------------------------
        


#Main loop 
app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()




