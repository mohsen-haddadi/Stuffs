import pickle
def load_variables() :
    global main_module_variable_1, main_module_variable_2
    main_module_variable_1, main_module_variable_2 = pickle.load( open( "pickled variables.p", "rb" ) )

def save_variables() :
	pickle.dump( [main_module_variable_1 , main_module_variable_2], open( "pickled variables.p", "wb" ) )


def update_variable_2():
	global main_module_variable_2
	load_variables()
	main_module_variable_2 = main_module_variable_1 # Works fine, without globaling main_module_variable_1
	save_variables()

def function_3() :
	load_variables()
	return main_module_variable_1, main_module_variable_2