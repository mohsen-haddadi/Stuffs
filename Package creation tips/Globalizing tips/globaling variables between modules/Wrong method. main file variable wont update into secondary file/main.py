import module_2

main_module_variable = 1

def update_variable():
	global main_module_variable

	main_module_variable += 1

def function_main():
	update_variable()
	print( main_module_variable )
	return module_2.function_2()

if __name__ == '__main__':
	print( function_main() )