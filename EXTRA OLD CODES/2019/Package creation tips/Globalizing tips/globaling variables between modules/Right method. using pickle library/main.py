import module_2 ,pickle

main_module_variable_1 = 1
main_module_variable_2 = "a string"

def pickle_variables() :
    pickle.dump( [main_module_variable_1 , main_module_variable_2], open( "pickled variables.p", "wb" ) )

def update_variable():
	global main_module_variable_1

	main_module_variable_1 += 1

def function_main():
	update_variable()
	print( main_module_variable_1 )
	pickle_variables() #write this line to save updated variables when you are about to use them
	#in the other modules at the next line(Gate ways to other modules) 
	return module_2.function_2()

if __name__ == '__main__':
	print( function_main() )