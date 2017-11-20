#
#

"""
#MAIN SNIPPET:

def main():
	

if __name__ == "__main__":
	main()

"""

"""
#Files
def main():
# Open a file for writing and create it if it doesn't exist
  f = open("textfile.txt","w+")
  
# Open the file for appending text to the end
#  f = open("textfile.txt","a+")

  # write some lines of data to the file
  for i in range(10):
    f.write("This is line %d\r\n" % (i+1))
  
# close the file when done
  f.close()
  
# Open the file back up and read the contents
  f = open("textfile.txt","r")
  if f.mode == 'r': # check to make sure that the file was opened
# use the read() function to read the entire file
    contents = f.read()
	
    
    fl = f.readlines() # readlines reads the individual lines into a list
    for x in fl:
      print x
	  
  print contents
	
if __name__ == "__main__":
	main()
"""



#Path Utilities

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
	# Print the name of the OS
	print os.name;
	
	print "----------next block----------"
	
	# Check for item existence and type
	print "Item exists: " + str(path.exists("textfile.txt"))
	print "Item is a file: " + str(path.isfile("textfile.txt"))
	print "Item is a directory: " + str(path.isdir("textfile.txt"))
	
	print "----------next block----------"
	
	# Work with file paths
	print "Item's path: " + str(path.realpath("textfile.txt"))
	print "Item's path and name: " + str(path.split(path.realpath("textfile.txt")))
	
	print "----------next block----------"
	
	# Get the modification time
	t = time.ctime(path.getmtime("textfile.txt"))
	print t
	print datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
	
	print "----------next block----------"
	
	# Calculate how long ago the item was modified
	td= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
	print "It has been " + str(td) + " Since The file was modified"
	print "Or, " + str(td.total_seconds()) + " seconds"

if __name__ == "__main__":
	main()























