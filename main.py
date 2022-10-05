#MadeByKeshuvVishram
import os
import time
import random
import sys
import rooms
import databasefunctions
#Title screen, asks if they want to play before checking for save
rooms.logoprint(rooms.logo)

time.sleep(3)

os.system('clear')

rooms.slowprint("Welcome to Dystopia.")

time.sleep(2)

rooms.slowprint("Shall we begin? y/n: ")

cont = input("")

cont = rooms.checkinput(cont, "y", "n")

if cont.lower() == "n":
    rooms.slowprint("Very well. Come back again when you are ready.")
    exit()
time.sleep(1)
os.system('clear')
rooms.checkforsave(
)  #Checks for save and prompts if they wish to continue if save is found
#Main code execution
try:  # Error catching
  while (True):
        x = databasefunctions.getfield('roomnumber')
        if x == "0":
            rooms.startingroom()
        elif x == "1":
            rooms.room1()
        elif x == "2":
            rooms.room2()
        elif x == "3":
            rooms.room3()
        elif x == "4":
            rooms.room4()
        elif x == "5":
            rooms.room5()
        elif x == "6":
            rooms.room6()
        elif x == "7":
            rooms.room7()
        elif x == "8":
            rooms.room8()
        elif x == "9":
            rooms.room9()
except Exception as e:
	rooms.slowprint("Fatal error has occured! Please restart program. Your progress should have saved. Exception (for debugging): "+str(e)+" Roomnumber (for manual progress rollback): "+databasefunctions.getfield('roomnumber'))  #Error catching
#MadeByKeshuvVishram

