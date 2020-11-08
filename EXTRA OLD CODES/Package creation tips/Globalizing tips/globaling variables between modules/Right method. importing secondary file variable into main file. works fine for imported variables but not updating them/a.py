import b
from b import pi
#pi = 2

def g():
	global pi
	pi = 1
	return pi
g()
print(pi)

###defect 1:
#b.f()
#print(pi) #prints out 3.14 while we suppose 4.14

###solution:
##the only way is to use only ***b.pi*** instead of ***pi***
##to to modify variables on other modules from another modules.
b.f()
pi = pi + 10 #this has no effect on b.pi
#b.pi = 20 we can modify b.pi variable from main module too
#b.f() # but it is better to update b.pi variable from b module by b functions instead of main module directly
print(b.pi)

###defect 2:
##can not update global variable ***b.pi*** with a function.
#def h():
#	global b.pi
#	b.pi = 1
#	return pi