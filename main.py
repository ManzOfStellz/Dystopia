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

rooms.slowprint("Welcome to dystopia.")

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
        if x == "1":
            rooms.room1()
        if x == "2":
            rooms.room2()
        if x == "3":
            rooms.room3()
        if x == "4":
            rooms.room4()
        if x == "5":
            rooms.room5()
        if x == "6":
            rooms.room6()
        if x == "7":
            rooms.room7()
        if x == "8":
            rooms.room8()
        if x == "9":
            rooms.room9()
except Exception:
	rooms.slowprint(str(Exception))  #Error catching
#MadeByKeshuvVishram

