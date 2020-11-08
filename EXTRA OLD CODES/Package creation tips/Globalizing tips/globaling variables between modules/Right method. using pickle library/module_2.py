import pickle, module_3

def load_variables() :
    global main_module_variable_1, main_module_variable_2 ,v3,  check_mode
    main_module_variable_1, main_module_variable_2 ,v3,  check_mode= pickle.load( open( "pickled variables.p", "rb" ) )

def save_variables() :
	pickle.dump( [main_module_variable_1 , main_module_variable_2, v3, check_mode ], open( "pickled variables.p", "wb" ) )
	
def update_variable_1():
	global main_module_variable_1
	load_variables()
	main_module_variable_1 += 1
	save_variables()

def reset_check_mode():
	global check_mode
	load_variables()
	check_mode = True # Works fine, without globaling main_module_variable_1
	save_variables()


def function_2() :
	return module_3.function_3()