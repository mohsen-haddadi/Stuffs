import module_2, module_3, pickle
"""
This module demostrate that:
1. Whenver shifting into another module to call a function (like: module_2.update_variable_1())
   use save_variables() right before that line and load_variables() right after that line.
   so when you use save_variables() at the end of a function, it save real updated variables.
2. Use save_variables() inside each function seperatly that changes a variable. 
3. Don't global variables inside a function which they are not assigned. It's useless.
   you can read or use variables in a function without globaling them. 
   like functions module_3.update_variable_2() or save_variables().
"""

def load_variables() :
    global main_module_variable_1, main_module_variable_2 ,v3,  check_mode
    main_module_variable_1, main_module_variable_2 ,v3,  check_mode= pickle.load( open( "pickled variables.p", "rb" ) )

def save_variables() :
	pickle.dump( [main_module_variable_1 , main_module_variable_2, v3, check_mode ], open( "pickled variables.p", "wb" ) )

def set_variables():
	global main_module_variable_1, main_module_variable_2, v3, check_mode
	main_module_variable_1 = 1
	main_module_variable_2 = 10
	v3 = 20
	check_mode = False
	save_variables()


def update_all():
	load_variables()

	save_variables()
	module_2.update_variable_1()
	module_3.update_variable_2_3()
	load_variables() # it's better to define another function for print and use load_variables() at its first line

	save_variables()
	print_variables()
	return module_2.function_2()

def print_variables():
	load_variables()
	print( '1:', main_module_variable_1, main_module_variable_2, v3, check_mode )

if __name__ == '__main__':
	set_variables()
	print( '2:', update_all() )

	load_variables() # it's better to define another function for print and use load_variables() at its first line
	print( '3:', main_module_variable_1, main_module_variable_2, v3, check_mode ) # should print: '3: 2 2 12 True'