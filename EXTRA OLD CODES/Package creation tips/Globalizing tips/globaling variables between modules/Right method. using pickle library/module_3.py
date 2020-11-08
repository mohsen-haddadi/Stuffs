import pickle, module_2
def load_variables() :
    global main_module_variable_1, main_module_variable_2 ,v3,  check_mode
    main_module_variable_1, main_module_variable_2 ,v3,  check_mode= pickle.load( open( "pickled variables.p", "rb" ) )

def save_variables() :
	pickle.dump( [main_module_variable_1 , main_module_variable_2, v3, check_mode ], open( "pickled variables.p", "wb" ) )


def update_variable_2_3():
	global main_module_variable_2, v3
	load_variables()
	main_module_variable_2 = main_module_variable_1 # Works fine, without globaling main_module_variable_1
	save_variables()
	module_2.reset_check_mode()
	load_variables()
	#save_variables()
	v3 = main_module_variable_1 + 10
	save_variables()


def function_3() :
	load_variables()
	return main_module_variable_1, main_module_variable_2, v3, check_mode