import b
from b import pi
#pi = 2

def g():
	global pi
	pi = 1
	return pi
#g()
print(pi)

###defect :
##b.f()
##print(pi) #print's out 3.14 while we suppose 4.14