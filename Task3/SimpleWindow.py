#This is a simple script for a GUI
#It has no functionality except for a 'quit; button,
#but the base should be good for our project
#
#Created using PyQT open source library for python
#Need to run 'sudo apt-get install python-pip python2.7-dev libxext-dev python-qt4 qt4-dev-tools build-essential' to install PyQt
#Here is a YouTube playlist for a PyQt tutorial:
#https://www.youtube.com/watch?v=JBME1ZyHiP8&list=PLQVvvaa0QuDdVpDFNq4FwY9APZPGSUyR4

#If you get a "cannot connect to x server" error, then run the command 'export DISPLAY=localhost:0.0' and try running again
#You also might need to run XMing if you are not on a Linux machine

######################################################################################################
#																																																		 #
# Need to run 'export BROWSER=/mnt/c/Program\ Files\ \(x86\)/Google/Chrome/Application/chrome.exe'   #
# For the Links to Open in Chrome instead of terminal via w3m																				 #
#																																																		 #
######################################################################################################
import time
import webbrowser
import sys
import simplejson
from urllib2 import *
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
	#constructor
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 1200, 900) #window dimensions
		self.setWindowTitle("Spotify Search Engine") #window name
		self.setWindowIcon(QtGui.QIcon('Spotify-icon.png')) #set icon
		QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique")) #set window style
		self.solrLink = "http://localhost:8983/solr/SpotifyProject/select?q=" #song title search prefix
		self.searchCount = 0
		self.setStyleSheet("background-color: white;")
		self.buttons = {}
		self.home()

	def home(self):
		#SET SEARCH VARIABLES
		self.searchType = "song" #for determing what to search by
		self.query = "" #for taking query input
		
		#SEARCH LOGO
		logo = QtGui.QLabel(self)
		logo.setPixmap(QtGui.QPixmap("spotify_search.png"))
		logo.resize(447, 108)
		logo.move(1200/2-224, 54)
		logo.show()
		
		#NUMBER OF RESULTS
		self.numResultsText = QtGui.QLabel("", self)
		self.numResultsText.move(1200/2-180, 230)
		self.numResultsText.setFont(QtGui.QFont("Times", 18))
		self.numResultsText.resize(400,30)
		self.numResultsText.show()
		
		#DROP DOWN BOX
		searchTypeBox = QtGui.QComboBox(self) #create drop-down box
		#add items to drop down
		searchTypeBox.addItem("Song")
		searchTypeBox.addItem("Artist")
		searchTypeBox.resize(80, 30)
		searchTypeBox.move(1200/2-180, 200) #set position
		searchTypeBox.activated[str].connect(self.set_search_type) #connect drop-down button to function
		#searchTypeBox.setStyleSheet("background-color: white; color: black;")
		
		#SEARCH FIELD
		searchField = QtGui.QLineEdit(self) #create input text field
		searchField.move(1200/2-100, 200)
		searchField.resize(200, 30)
		searchField.setPlaceholderText("Enter Search Query...")
		searchField.textChanged.connect(self.set_query) #conect to function
		#searchField.setStyleSheet("background-color: white; color: black;")
		
		#EXECUTE SEARCH
		searchButton = QtGui.QPushButton("Search", self) #create search button
		searchButton.clicked.connect(self.execute_search) #connect to function
		searchButton.resize(80, 30)
		searchButton.move(1200/2+100, 200)
		#searchButton.setStyleSheet("background-color: white; color: black;")
		
		
		
		#OPEN WINDOW
		self.show() #have window appear on screen
		
	#DROP-DOWN BUTTON FUNCTION
	def set_search_type(self, text):
		self.searchCount += 1
		self.searchType = text
		#print(self.searchType) #line here to make sure dropdown works
		
	def set_query(self, text):
		self.query = text
		#print(self.query) #here for debugging
	
	def execute_search(self):
		print("You searched for: " + str(self.query)) #Verify Search in Terminal
		self.query = str(self.query).strip().replace(" ","*")
		if self.searchCount == 0: #Bug Fix where first search would not be formatted correctly
			self.searchType = "track.name:\"*"
		if self.searchType == "Artist":
			self.searchType = "track.artists.name:\"*"
		if self.searchType == "Song":
			self.searchType = "track.name:\"*"
		self.jsonwt = "*\"&wt=json" #song title search postfix to specify json format
		self.searchCount += 1
		
		#establish network connection
		self.connection = urlopen(self.solrLink.strip() + str(self.searchType).strip() + str(self.query).strip() + self.jsonwt.strip())
		self.response = simplejson.load(self.connection)
		
		self.display_results()
			
	#FOR RESULTS DISPLAY
	def display_results(self):
		#Print Responses in Terminal
		results = []
		songURLs = []
		self.numResults = str(self.response['response']['numFound']).strip() + " documents found."
		print self.numResults
		for document in self.response['response']['docs']:
			resultString = document['track.name'][0].strip() + " by " + document['track.artists.name'][0].strip()
			results.append(resultString)
			songURLs.append(document['track.external_urls.spotify'][0]) #store song URLs
			#print resultString
			
		self.numResultsText.setText(self.numResults + " Showing top 10 results.")
		
		for j in range(10): #num rows
			for i in range(3): #num columns
				if i == 0: #Play self.buttons
					if self.response['response']['numFound'] > j: #in case fewer than 10 results
						self.buttons[(i, j)] = QtGui.QPushButton('Play', self)
						self.buttons[(i, j)].clicked.connect(self.make_open_browser(songURLs[j]))
						self.buttons[(i, j)].move(1200/2-400-30, j*50+300)
						self.buttons[(i, j)].resize(100, 50)
						self.buttons[(i, j)].setFont(QtGui.QFont("Times", 32, QtGui.QFont.Bold)) #set font
						#self.buttons[(i, j)].setStyleSheet("background-color: white; color: black;")
						self.buttons[(i, j)].show()
				elif i == 1: #Song Info self.buttons
					if self.response['response']['numFound'] > j:
						self.buttons[(i, j)] = QtGui.QPushButton(results[j], self)
						self.buttons[(i, j)].move(1200/2-300-30, j*50+300)
						self.buttons[(i, j)].resize(600, 50)
						self.buttons[(i, j)].setFont(QtGui.QFont("Times", 24, QtGui.QFont.Bold))
						#self.buttons[(i, j)].setStyleSheet("background-color: white; color: black;")
						self.buttons[(i, j)].show()
				else: #Similar Song self.buttons
					if self.response['response']['numFound'] > j:
						self.buttons[(i, j)] = QtGui.QPushButton('Similar Songs', self)
						self.buttons[(i, j)].move(1200/2+300-30, j*50+300)
						self.buttons[(i, j)].resize(160, 50)
						self.buttons[(i, j)].setFont(QtGui.QFont("Times", 24, QtGui.QFont.Bold))
						#self.buttons[(i, j)].setStyleSheet("background-color: white; color: black;")
						self.buttons[(i, j)].show()
	
	#function factory to pass argument to open correct URL
	def make_open_browser(self, URL):
		def open_browser():
			webbrowser.open(URL, new=2)
		return open_browser

	def close_app(self):
		sys.exit() #close program

def main():
	app = QtGui.QApplication(sys.argv) #create application object
	GUI = Window() #create Window
	sys.exit(app.exec_()) #end program

main()
