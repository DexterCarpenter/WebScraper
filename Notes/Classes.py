#
# Classes

"""
#MAIN SNIPPET:

def main():
	

if __name__ == "__main__":
	main()

"""

"""
class MyClass():
	def method(self):
		print "MyClass method!"
	
	def method2(self, something):
		print "MyClass method 2" + something

def main():
	c = MyClass()
	c.method()
	c.method("This is a string")

	
if __name__ == "__main__":
	main()
"""



class MyClass():
	def method(self):
		print "MyClass method!"
	
	def method2(self, something):
		print "MyClass method 2" + something

class anotherclass(MyClass):
	def method2(self):
		print "anotherclass method2"
		
	def medthod1(self):
		myClass.method1(self):
		print "anotherclass method1"
		
def main():
	c = MyClass()
	c.method()
	c.method("This is a string")

	
if __name__ == "__main__":
	main()

"""
everything in the above section, may be wrong, it is wrong......
"""

