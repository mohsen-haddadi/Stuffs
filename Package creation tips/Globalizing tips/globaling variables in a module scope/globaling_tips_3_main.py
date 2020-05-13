""" Refrence: https://realpython.com/python-scope-legb-rule/ """
"""
This code demostrate globaling using nested functions works as well. 
"""

def globaling_x(): 
	global x
	x = 10

def myfunc_1():
	globaling_x()
	print(x)

def myfunc_3():
	global x #global scope x can now be modified
	myfunc_1()
	x = x + 1
	print(x)

def main():
	myfunc_3()

main()
