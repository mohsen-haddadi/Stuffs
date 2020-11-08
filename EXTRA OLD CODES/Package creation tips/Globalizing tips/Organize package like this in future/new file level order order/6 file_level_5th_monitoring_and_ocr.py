import pickle

def load_variables() :
    global monitoring_variable, check_mode, GAME_POSITION
    monitoring_variable, check_mode, GAME_POSITION = pickle.load( open( "pickled variables.p", "rb" ) )

def pixel_matching() :
	global monitoring_variable, GAME_POSITION # use this line to resist potential UnboundLocalError
	#this line is not a must anymore, by using read_game_variables() in main module and save variables there
	#This line is a must, otherwise monitoring_variable is known as local, therefore assigments are localy and does not affects saved_variables
	load_variables() #load GAME_POSITION
	monitoring_variable = 'monitoring_variable'
	print('monitoring_variable is set')
	#print(monitoring_variable)
	#save_variables() #for pixel matching, ocr, buttons, vital_signs; use the returned values at read_game_variables() and save_variables() them there
	return monitoring_variable

