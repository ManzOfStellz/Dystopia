#MadeByKeshuvVishram
import xml.etree.ElementTree as ET #Imports an xml handling module, allowing it to be referred to as ET

fileName = 'datastore.xml' #sets filename to be used

tree = ET.parse(fileName) #calls/registers (parses) entire xml file
root = tree.getroot() #Gets contents of xml file
#A lot of these functions work in a similar way, just altered for different things, so I will comment only where relevant
def updateintfield(field, increment):
	for i in root.iter(field): #iterates through the xml file looking for the specified field
		int_i = int(i.text) + increment #Adds the increment value to the previous value in the intfield
		i.text = str(int_i)
	tree.write(fileName) #Saves changes

def updateStringfield(field, change):
	for i in root.iter(field):
		i.text = change
	tree.write(fileName)

def getfield(fieldname):
	root = tree.getroot()
	for i in root.iter(fieldname):
		return i.text #returns the requested field

def overwriteintfield(field, increment):
	for i in root.iter(field):
		int_i = increment
		i.text = str(int_i)
	tree.write(fileName)

def formatsave(): #This function sets each field of the database to the default values using the updateStringfield function above
	updateStringfield("shirt", "")
	updateStringfield("carkey", "")
	updateStringfield("weapon", "")
	updateStringfield("name", "")
	overwriteintfield("health", "100")
	overwriteintfield("roomnumber", "0")
#MadeByKeshuvVishram
#MadeByKeshuvVishram