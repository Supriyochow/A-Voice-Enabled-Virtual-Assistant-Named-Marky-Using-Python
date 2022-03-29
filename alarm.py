import random
import time
import webbrowser

from datetime import datetime
import subprocess

#lines = open("C:\Python_code\Links.txt").read().splitlines()
#mylines = random.choice(lines)
#print(mylines)

time_input = str(input("Please enter the time in HH:MM:SS format: "))
current_date = str(input("Please enter the date in YYYY/MM/DD format: "))
selected_time = datetime.strptime('%s %s'%(current_date, time_input),"%Y/%m/%d  %H:%M:%S")
print ("Time selected: ",selected_time)

while True:
  if selected_time == time.localtime():
      print ("Alarm Now")
      webbrowser.open(mylines)
      break
  else:
      pass