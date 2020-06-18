import module_2, module_3, pickle
"""
This module demostrate that:
1. Use save_variables() inside any function that changes a variable. 
   don't use save_variables() all at once in such lines like gate ways.
2. Don't global variables inside a function which they are not assigned. It's useless.
   you can read or use variables in a function without globaling them. 
   like functions module_3.update_variable_2() or save_variables().
"""


def load_variables() :
    global main_module_variable_1, main_module_variable_2
    main_module_variable_1, main_module_variable_2 = pickle.load( open( "pickled variables.p", "rb" ) )

def save_variables() :
    pickle.dump( [main_module_variable_1 , main_module_variable_2], open( "pickled variables.p", "wb" ) )

def set_variables():
	global main_module_variable_1, main_module_variable_2
	main_module_variable_1 = 1
	main_module_variable_2 = 10
	save_variables()

def update_variable_1():
	global main_module_variable_1
	load_variables()
	main_module_variable_1 += 1
	save_variables()

def function_main():
	update_variable_1()
	module_3.update_variable_2()

	load_variables() # it's better to define another function for print and use load_variables() at its first line
	print( '1:', main_module_variable_1, main_module_variable_2 )
	#save_variables() # Don't use save_variables() all at once in such lines like gate ways.
	# Use save_variables() separtly for each function that changes a variable. 
	return module_2.function_2()

if __name__ == '__main__':
	set_variables()
	print( '2:', function_main() )

	load_variables() # it's better to define another function for print and use load_variables() at its first line
	print( '3:', main_module_variable_1, main_module_variable_2 )