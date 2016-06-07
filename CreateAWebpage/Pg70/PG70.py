#HTML page creation
#
##Create a gui with with wx
##Allow useres to imput their own  body text
##
##
##
##

import wx


class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None,\
          title=title, size=(800,600))
        panel = wx.Panel(self)

        # Creating the menu bar
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.NewId(), "Exit")
        menuBar.Append(fileMenu, "File")
        
        self.SetMenuBar(menuBar)
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

        # Bind delete button to onDelete function
        publishBtn.Bind(wx.EVT_BUTTON, self.publishWebpage)
        clearBtn.Bind(wx.EVT_BUTTON, self.clearBoxes)
        createWebpage.Bind(wx.EVT_BUTTON, self.createWebpage)

    def exitProgram(self, event):
        self.Destroy()

    def createWebpage(self,event):
        filename = self.websiteName.GetValue() + ".html"
        output = open(filename,"w")
        output.close()
        print("Create web page")

    def clearBoxes(self,event):
        self.websiteName.Clear()
        self.multiText.Clear()
        print("Clear the boxes")

    def publishWebpage(self,event):
        self.createWebpage(event)
        print("Publish webpage")
        

    






app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()

##Content = '''
##<html>
##<body>
##Stay tuned for our amazing summer sale!
##</body>
##</html>
##'''
##
##def main():
##    browseLocal(Content)
##
##def strToFile(text, filename):
##    output = open(filename,"w")
##    output.write(text)
##    output.close()
##
##def browseLocal(webpageText, filename='PG70.html'):
##    import webbrowser,os.path
##    strToFile(webpageText, filename)
##    webbrowser.open("file:///" + os.path.abspath(filename))
##
##main()
