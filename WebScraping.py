##Using python 2.7.11
##Final project Get powerball numbers
##
##Create a scrpt that
##when executed
##retrieves the most recent powerballnumbers
##and displayes them to the shell
##
##
##
##


#Imports
import urllib2, wx
from bs4 import BeautifulSoup
from datetime import datetime,timedelta

# Declares the frame class and opens the window
class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(150,100))

        #Creates the Panels
        mainPanel = wx.Panel(self)
        self.panel = wx.Panel(mainPanel,-1, size=(150,100))

        #prints powerball numbers
        self.webNameLabel = wx.StaticText\
                       (self.panel, -1, label="Powerall Numbers:",pos=(0,5))
        self.webNameLabel = wx.StaticText\
                       (self.panel, -1, label="{}".format(getpowerballnums()),pos=(0,25))



#Formats the day so the webscraper can find the right day
def formatday(timestamp):
    #sets the publish time to day of drawing
    timestamp = timestamp-timedelta(hours =24)
    month = timestamp.strftime("%m")
    day = timestamp.strftime("%d")
    year = timestamp.strftime("%Y")
    #removes the '0' on numbers less then ten
    if int(month) < 10:
        month= month.replace('0', '')    
    if int(day) < 10:
        day = day.replace('0','')

    date = "{}/{}/{}".format(month,day,year)
    
    return date

#finds the last drawing publish time
def lastDrawTime():
    #finds last wednesday
    today = datetime.now() 
    wednesday = (datetime.weekday(today) - 3) % 7    
    last_wednesday = today - timedelta(days=wednesday)
    
    #finds last saturday 
    saturday = (datetime.weekday(today) - 6) % 7
    last_saturday = today - timedelta(days=saturday)

    #tests to find last drawing time
    if today-last_wednesday < today-last_saturday:
        date = formatday(last_wednesday)        
    elif today-last_wednesday > today-last_saturday:
        date = formatday(last_saturday)
    else:
        print "something went wrong"
    
    return date

#scrapes the web to find the powerball numbers
def getpowerballnums():
    # Open webpage
    webpage = urllib2.urlopen("http://www.powerball.com/powerball/pb_numbers.asp")

    # Convert to BeautifulSoup
    soup = BeautifulSoup(webpage, "html.parser")
    #print soup
    # Get the contents of table containing powerballs
    date = lastDrawTime()
    date = soup.find('b',text='{}'.format(date))    #finds a specific identifier
    cursor = date
    whiteballs = []

    #collects info for all the white balls
    for i in range(5):
        cursor = cursor.findNext('font')
        text = cursor.get_text()
        whiteballs.append(int(text))
        
    #collects the red ball
    redball = int(cursor.findNext('font').get_text())

    #adds red ball to whiteballs
    powerball = whiteballs
    powerball.append(redball)
    strpowerball = ""

    #converts to an easy to read string
    for i in range(len(powerball)):
        strpowerball = strpowerball + "{} ".format(powerball[i])

    return strpowerball

#Main loop 
app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()











    

