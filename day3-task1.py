#imported date time library to display door's open and lock date & time
from datetime import date
from datetime import datetime
now = datetime.now()
pwd = 4333

#prompts user to enter the password
password = int(input("Enter the password\n"))

#checks the validity of the paaword
while (password != pwd):
  print("Wrong password!\n")
  pwd = int(input("Enter a valid password\n"))
  break

#prompts user to enter an open command
open = str(input("type the command to open the door\n"))

if (open == "open"):
  print("The door is now open", now)
substring = "open" 

# counts the number of open commands entered
count = open.count(substring)

#if similar command entered is > 1, user is notified door is already open
if (count > 1):
  print("The door is already open", now)
#prompts user input to lock the door
close = str(input("type the command to close the door\n"))
if (close == "close"):
  print("The door is now locked", now)
string = "close"
#counts the number of close command entered
count = close.count(string)

#if similar close commands are entered, user is notified the door is already locked
if (count > 1):
  print("The door is already locked", now())

#function to quit the program
def terminate():
  exit = str(input("type quit to exit the program\n"))
  if exit == "quit":
    print("program exited successfully")
  else :
      print("invalid input")
      #executes function terminate() again incase of invalid input
      terminate()

#calls function terminate      
terminate()
