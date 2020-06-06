""" Refrence: https://realpython.com/python-scope-legb-rule/ """
"""
There are 2 ways to create a global scope
1. simply assign the variable outside functions
2. global it inside a function but don't remember to run that funtion 
before using that variable inside or ouside other funcions to resist NameError.
"""
#x = 10 #global scope

def globaling_x(): #no need to use this function
	global x
	x = 10

def myfunc_1():
	"""
	x is already globaled because it has been define outside functions at line 1.
	but x cant be modified inside a function(ex: myfunc4)
	unless it's been globaled inside that function(ex: myfunc3)
	"""
	print(x)

def myfunc_2():
	x = 300 #local scope, does not change global scope x
	x = x + 1
	print(x)

def myfunc_3():
	global x #global scope x can now be modified
	x = x + 1
	print(x)

def myfunc_4(): #Errors
	x = x + 1 #x is local and has not been defined
	print(x)

def myfunc_5(): #Errors
	#global x #this makes it ok
	globaling_x() 
	x = x + 1 #x is still local and has not been defined
	print(x)

def main():
	myfunc_1()
	myfunc_2()
	myfunc_3()
	myfunc_4()
	myfunc_5()
	
globaling_x()

main()
