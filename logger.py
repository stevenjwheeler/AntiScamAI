from datetime import datetime

def log(message):
   now = datetime.now()
   datetimestring = now.strftime("%d/%m/%Y %H:%M:%S")

   logfile = open("log.txt", "a")
   logfile.write("{0} - {1}\n".format(datetimestring, message))
   logfile.close()