def module_function_1():
	global x1 , x2#This line is a must; to affect variables into save_variables()
	load_variables()#Use it; to resist probable saving outdated varibales
	# assign x1 and x2
	save_variables()

def module_function_2():
	global x1 , x2#This line is a must; to resist potential UnboundLocalError
	load_variables()#Use it; if you need to use a variable like GAME_POSITION
	# assign x1 and x2
	return x1

def module_function_3():
	global x1 , x2
	# assign global variables x1 and x2
	return x1

def module_function_4():
	# just use global variables x1 and x2
	return x1

def set_variables_to_None(): #exeption when there is no need to use load_variables()
    global x1 , x2, x3 #This line is a must; to affect variables into save_variables()
    x1, x2, x3 = 3*(0,) 
    save_variables()

#pure functions uses return; non pure uses save_variables