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
#print(pi) #print's out 3.14 while we suppose 4.14

###solution:
##the only way is to use only ***b.pi*** instead of ***pi***
##to to modify variables on other modules from another modules.
b.f()
pi = pi + 1
print(b.pi)

###defect 2:
##can not update global variable ***b.pi*** with a function.
#def h():
#	global b.pi
#	b.pi = 1
#	return pi