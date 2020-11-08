import pickle
# modules like: supporting_functions, straight, flush, and... uses pickled variables 
# and therefore do not need to import other pixel matching modules.

def load_variables() :
	global monitoring_variable, check_mode, GAME_POSITION # This line is a must, because we are about to modify variables or introduce variables as global
	monitoring_variable, check_mode, GAME_POSITION = pickle.load( open( "pickled variables.p", "rb" ) )

def supporting_function():
	load_variables()
	return (monitoring_variable, check_mode)