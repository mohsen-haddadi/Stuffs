import pickle
import file_level_5th_monitoring_and_ocr

def save_variables() :
	# no need to use global variables line here, because we are not about to modify variables or introduce variables as global
	# load_variables() # using it here leads to wrong answers. it will load old variables
	pickle.dump([monitoring_variable , check_mode, GAME_POSITION], open( "pickled variables.p", "wb" ) )

def load_variables() :
    global monitoring_variable, check_mode, GAME_POSITION # This line is a must, because we are about to modify variables or introduce variables as global
    monitoring_variable, check_mode, GAME_POSITION = pickle.load( open( "pickled variables.p", "rb" ) )

def set_all_varibales_to_None():
    global monitoring_variable , check_mode, GAME_POSITION #This line is a must
    # here write a command to delete 'pickled variables.p' file if it's been already existed; to make sure all variables are cleared
    monitoring_variable , check_mode, GAME_POSITION = (None,'check_mode is False',None)
    save_variables()

def read_game_variables(): # use all pure functions (pixel matching, ocr, card search and...) here
	global monitoring_variable, check_mode #This line is a must, otherwise variables are known as local,
	#therefore assigments are localy and does not affects saved_variables
	load_variables()
	monitoring_variable = file_level_5th_monitoring_and_ocr.pixel_matching()

#	my_1th_card, my_2th_card = read_my_cards(my_seat, xth_card)
#	if 'Unknown' in my_1th_card or 'Unknown' in my_2th_card:
#		file_level_1o5th_game_coordinates.check_game_connectivity()
#		my_1th_card, my_2th_card = read_my_cards(my_seat, xth_card)
#		if 'Unknown' in my_1th_card or 'Unknown' in my_2th_card or Flop():
#			Check_Mod_On("Read_My_Cards():My_1th_Card")

	save_variables()
