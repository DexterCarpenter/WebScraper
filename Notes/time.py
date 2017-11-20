#
# Time

"""
#MAIN SNIPPET:

def main():
	

if __name__ == "__main__":
	main()

"""

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import calendar

"""
#year, time, weekday, etc
def main():
	## DATE OBJECTS
	# get todays date
	
	today = date.today()
	print "Today's date is", today
	print "Today's date is", today.day, today.month, today.year
	print "Today's weekday is", today.weekday()
	today = datetime.now()
	print "the current date and time is ", today
	
	t = datetime.time(datetime.time.now())
	print "the current time is ", t
	
if __name__ == "__main__":
	main()
"""
	
"""
#weekday
def main():
	
	# weekday returns 0 (monday) through 6 (sunday)
	wd = date.weekday(today)  
	# Days start at 0 for Monday 
	days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
	print "Today is day number %d" % wd
	print "Which is a " + days[wd]

	
if __name__ == "__main__":
	main()
"""


"""
#formatting
def main():
	# Times and dates can be formatted using a set of predefined string
	# control codes 
	now = datetime.now() # get the current date and time
	
	# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
	print now.strftime("%Y") # full year with century
	print now.strftime("%a, %d %B, %y") # abbreviated day, num, full month, abbreviated year
	
	# %c - locale's date and time, %x - locale's date, %X - locale's time
	print now.strftime("%c")
	print now.strftime("%x")
	print now.strftime("%X")

	
if __name__ == "__main__":
	main()
"""

"""
#time delta
def main():
	# construct a basic timedelta and print it
	print timedelta(days=365, hours=5, minutes=1)
	
	# print today's date
	print "today is: " + str(datetime.now())
	
	# create a timedelta that uses more than one argument
	print "in two weeks and 3 days it will be: " + str(datetime.now() + timedelta(weeks=2, days=3))
	
	# calculate the date 1 week ago, formatted as a string
	t = datetime.now() - timedelta(weeks=1)
	s = t.strftime("%A %B %d, %Y")
	print "one week ago it was " + s
	
	today = date.today()  # get today's date
	afd = date(today.year, 4, 1)  # get April Fool's for the same year
	# use date comparison to see if April Fool's has already gone for this year
	# if it has, use the replace() function to get the date for next year
	if afd < today:
		print "April Fool's day already went by %d days ago" % ((today-afd).days)
		afd = afd.replace(year=today.year + 1)  # if so, get the date for next year
		
	# Now calculate the amount of time until April Fool's Day  
	time_to_afd = abs(afd - today)
	print time_to_afd.days, "days until next April Fools' Day!"

if __name__ == "__main__":
	main()
"""


#calendar
def main():
	# create a plain text calendar
	c = calendar.TextCalendar(calendar.SUNDAY)
	str = c.formatmonth(2017, 10, 0, 0)
	print str
	
	"""
	# create an HTML formatted calendar
	hc = calendar.HTMLCalendar(calendar.SUNDAY)
	str = hc.formatmonth(2013, 1)
	print str
	"""
	
	"""
	# loop over the days of a month
	# zeroes mean that the day of the week is in an overlapping month
	for i in c.itermonthdays(2017, 10):
		print i
	"""
	 
	"""
	# The Calendar module provides useful utilities for the given locale,
	# such as the names of days and months in both full and abbreviated forms
	for name in calendar.month_name:
		print name
	
	print "----------next block----------"
	
	for day in calendar.day_name:
		print day
	
	print "----------next block----------"
	
	"""
	
	# Calculate days based on a rule: For example, consider
	# a team meeting on the first Friday of every month.
	# To figure out what days that would be for each month,
	# we can use this script:
	for m in range(1,13):
	  # returns an array of weeks that represent the month
	  cal = calendar.monthcalendar(2013, m)
	  # The first Friday has to be within the first two weeks
	  weekone = cal[0]
	  weektwo = cal[1]
	   
	  if weekone[calendar.FRIDAY] != 0:
		meetday = weekone[calendar.FRIDAY]
	  else:
		# if the first friday isn't in the first week, it must be in the second
		meetday = weektwo[calendar.FRIDAY]
		  
	  print "%10s %2d" % (calendar.month_name[m], meetday)

if __name__ == "__main__":
	main()





























