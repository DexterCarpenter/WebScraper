#
# Examples of Functions

"""
#functions
def funct():
	print "I am a Function"
	
funct()
print funct()
print funct
"""

"""
#Argument Functions
def func2(argl, arg2):
	print argl, " ", arg2
	
func2(10, 20)
print func2(10, 20)
"""

"""
#Cubed Functions
def cube(x):
	return x*x*x
	
print cube(3)
"""

"""
#exponent Functions
def power(num, x=1):
	result = 1;
	for i in range (x):
		result = result * num
	return result

print power(2)
print power(2, 3)
print power(x=3,num=2)
"""

"""
#Sum Functions
def multi_add(*args):
	result=0;
	for x in args:
		result = result + x
	return result

print multi_add(4,7,3,76,2)
"""
