import pickle 

def save_variables() :
	# no need to use global variables line here, because we are not about to modify variables or introduce variables as global
	# load_variables() # using it here leads to wrong answers. it will load old variables
	pickle.dump([monitoring_variable , check_mode, GAME_POSITION], open( "pickled variables.p", "wb" ) )

def load_variables() :
    global monitoring_variable, check_mode, GAME_POSITION # This line is a must, because we are about to modify variables or introduce variables as global
    monitoring_variable, check_mode, GAME_POSITION = pickle.load( open( "pickled variables.p", "rb" ) )

def find_game_position():
	global GAME_POSITION
	load_variables()
	GAME_POSITION = 'GAME_POSITION'
	print('GAME_POSITION is set')
	save_variables()

def setup_coordinates(): #like sushigoround bot
    global monitoring_variable , check_mode, GAME_POSITION #This line is a must
    load_variables()
    monitoring_variable = GAME_POSITION + ' + ' + monitoring_variable 
    save_variables()

def check_game_connectivity(): #vital_signs #non pure function; pure function uses return; non pure uses save_variables
	global check_mode, GAME_POSITION # use this line to resist potential UnboundLocalError
	#this line is not a must anymore, by using read_game_variables() in main moduleand save variables there
	#This line is a must, otherwise monitoring_variable is known as local, therefore assigments are localy and does not affects saved_variables
	load_variables() #load GAME_POSITION

	check_mode  = 'check_mode is True'
	print('check_mode is set')
	save_variables() #use save variables at the end of all function which may have side effects
	#return check_mode

