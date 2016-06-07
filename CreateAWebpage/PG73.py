#!/usr/bin/env python3.4
## In python 3.4
#HTML page creation
#
##PG72
##
##Create a gui with with wx
##Allow useres to imput their own  body text
##
##PG73
##
##Needs to show premade content
##storage of pre-made content,
##choose from that pre-made content
## creation of a database that can store the content
##controls for creating new body text
##a set of controls for fetching all content from the database
## displaying that content in a grid
## selecting one of the content choices
##and using that selection in creating a new web page
##
##


import webbrowser,os.path,wx,db_program

# Declares the frame class and opens the window
class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(800,600))
        


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

        #creates the Panels
        mainPanel = wx.Panel(self)
        self.panel = wx.Panel(mainPanel,-1, size=(800,600))
        self.mid = wx.Panel(mainPanel,-1, size=(1,600))
        self.prefabPanel = wx.Panel(mainPanel,-1,size=(400,600))
        self.mid.SetBackgroundColour('Black')
        
        #-----------------------PANEL ONE------------------------------------        

        # Labels
        self.webNameLabel = wx.StaticText\
                       (self.panel, -1, label="What do you want to name you webpage?\
 (Will create a new HTML file if one does not exist)",pos=(90,50))
        self.webContentLabel = wx.StaticText\
                          (self.panel, -1, label="Enter the content of your webpage:\
 (Will add to Pre existing content)",pos=(90,130))
        # Single line text boxes
        self.websiteName = wx.TextCtrl(self.panel, size=(450, -1), pos=(90,70))

        # Multi line text box
        self.multiText = wx.TextCtrl\
                    (self.panel, -1,"test",size=(600, 275), pos=(90,150), style=wx.TE_MULTILINE)
        self.multiText.SetInsertionPoint(0)

        # Buttons
        createWebpage = wx.Button(self.panel, label="Create New Webpage", pos=(555, 69))
        publishBtn = wx.Button(self.panel, label="Publish", pos=(605, 450))
        clearBtn = wx.Button(self.panel, label="Clear", pos=(90, 450))
        self.addBtn = wx.Button(self.panel, label="Show Examples", pos=(360, 450))
        self.addBtn.myname = "show"
        self.hideBtn = wx.Button(self.panel, label="Hide Examples", pos=(430, 450))
        self.removex = wx.Button(self.panel, label="Remove Example Content", pos=(225, 450))

        self.removex.Hide()
        self.hideBtn.myname = "hide"
        self.hideBtn.Hide()

        # Bind delete button to function
        publishBtn.Bind(wx.EVT_BUTTON, self.publishWebpage)
        clearBtn.Bind(wx.EVT_BUTTON, self.clearBoxes)
        createWebpage.Bind(wx.EVT_BUTTON, self.createWebpage)
        self.addBtn.Bind(wx.EVT_BUTTON, self.buttonPush)
        self.hideBtn.Bind(wx.EVT_BUTTON, self.buttonPush)
        self.removex.Bind(wx.EVT_BUTTON, self.removeText)

        #------------------------PANEL TWO-----------------------
        #create stuff in self.prefabPanel = wx.Panel(mainPanel,-1,size=(400,600))
        #Labels
        self.prefabPanel.Hide()
        self.mid.Hide()
        self.webNameLabel = wx.StaticText\
                       (self.prefabPanel, -1, label="Pre existing content:",pos=(90,50))

        # Setup the Table UI
        # Setup table as listCtrl
        self.listCtrl = wx.ListCtrl\
                        (self.prefabPanel, size=(220,360), \
                         pos=(90,70), style=wx.LC_REPORT |wx.BORDER_SUNKEN)
        
        #Adds columns to the listCtrl        
        self.listCtrl.InsertColumn(0, "ID", )
        self.listCtrl.InsertColumn(1, "Name")
        self.listCtrl.SetColumnWidth(0,-2)
        self.listCtrl.SetColumnWidth(1,-2)
        

        #Fills with data
        self.fillListCtrl()

        #run on selection
        self.listCtrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSelect)
        
        #Adds buttons
        removeBtn = wx.Button(self.prefabPanel, label="Remove", pos=(50, 450))
        exampleBtn = wx.Button(self.prefabPanel, label="Example", pos=(150, 450))
        addtoBtn = wx.Button(self.prefabPanel, label="Add", pos=(250, 450))

        #Bind buttons
        removeBtn.Bind(wx.EVT_BUTTON, self.droprow)
        exampleBtn.Bind(wx.EVT_BUTTON, self.exampleText)
        addtoBtn.Bind(wx.EVT_BUTTON, self.addText)
        


        #------------------------SIZERS---------------------------
        #Sizers
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.sizer.Add(self.prefabPanel,0,wx.EXPAND|wx.ALL,border=0)
        self.sizer.Add(self.mid,0,wx.EXPAND|wx.ALL,border=0)
        self.sizer.Add(self.panel,0,wx.EXPAND|wx.ALL,border=0)
        #self.mid = wx.Panel(mainPanel,-1, size=(1,600))

        mainPanel.SetSizer(self.sizer)

#-------------------------------------defs-------------------------------------------------------

    #deletes a row in the database
    def droprow(self, event):
        exampleFile = self.findExampleFile()
        exampleID = exampleFile[0]
        db_program.droprow(exampleID)
        self.fillListCtrl()
        
        
    #when an example file is selected
    def onSelect(self, event):
        # Get the id of the selected row
        self.selectedId = event.GetText()
        print (self.selectedId)        
        
    #remove button
    def removeText(self, event):
        content = self.multiText.GetValue()
        examplefile = self.findExampleFile()
        
        content = content.replace(examplefile[2],"")
        self.multiText.Clear()
        self.multiText.AppendText(content)

    #example button function
    def exampleText(self, event):
        exampleFile = self.findExampleFile()
        self.browseLocal(exampleFile[3])
    
    #addto button function
    def addText(self, event):
        #gets the ID number
        exampleFile = self.findExampleFile()       

        self.multiText.AppendText("\n" + exampleFile[2] + "\n")

    #returns the example file as an array
    def findExampleFile(self):
        itemnum = self.listCtrl.GetFocusedItem()        
        exampleID = self.listCtrl.GetItemText(itemnum)
        exampleFile = db_program.retrieveExample(exampleID)
        return exampleFile
        

    #Fill the list box
    def fillListCtrl(self):
        # Delete old data before adding new data
        self.listCtrl.DeleteAllItems()

        #fills the data
        count = db_program.countAll()
        print(count)
        for i in range(count):
            try:
                examplefile = db_program.retrieveExample(i+1)
                useabletext = (examplefile[0],examplefile[1])
                print (examplefile)
                print (useabletext)
                self.listCtrl.Append(useabletext)
            except:
                pass


    #when the add button is pushed
    def buttonPush(self, event):
        name = event.GetEventObject().myname
        if name == "show":
            self.removex.Show()
            
            self.mid.Show()
            
            self.prefabPanel.Show()
            
            self.addBtn.Hide()
            
            self.hideBtn.Show()
            
            self.SetSize(1200,600)

            
        elif name == "hide":
            self.mid.Show()
            self.prefabPanel.Hide()
            self.SetSize(800,600)
            self.addBtn.Show()
            self.hideBtn.Hide()
            self.removex.Hide()


        
        

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

    #Save the data to a database
    def saveData(self,name,cont,filepath):
        db_program.storeExample(name,cont,filepath)
        self.fillListCtrl()

    #Create a new html file if one doesnt exist and outputs content
    def publishWebpage(self,event):
        self.filename = self.websiteName.GetValue()
        self.filepath = self.filename + '.html'
        self.text = self.multiText.GetValue()
        print("DEBUG: " + self.text)
        self.content = self.formatText(self.filename, self.text)
        
        if self.filename != '':
            self.saveData(self.filename,self.text,self.filepath)
            self.output = open(self.filepath,"w")
            self.output.write(self.content)
            self.output.close()
        self.browseLocal(self.filepath)
        
        
        print("Publish webpage")

    #Opens the html file in a webbrowser for the user to see
    def browseLocal(self, filename):        
        webbrowser.open("file:///" + os.path.abspath(filename))

        
#-----------------------TEXT FORMAT-----------------------------
#Formats the conent before outputting to html file
    def formatText(self, filename,text):
        contentBeg = '''
<html>
<head>
<title>
'''
        contentMid = '''
</title>
</head>
<body>
'''
        contentEnd = '''
</body>
</html>
'''
        content = contentBeg + filename + contentMid + text + contentEnd
        print(content)
        return content
        
#-----------------------TEXT FORMAT-----------------------------
        


#Main loop 
app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()




