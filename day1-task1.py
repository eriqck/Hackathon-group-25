#imports datetime library to display current's day date
import time
import datetime
from datetime import date
date = date.today()
day = datetime.date.today().strftime("%A")[0:3]
print("Date : ", date)
print("Day  : ", day)

#if else condition to determine fare charged per specific day
if day == 'Sat':
  print("Fare :  60")
else :
  if (day == 'Sun'):
    print("Fare :  80")
  else :
      print("Fare :  100")
