import pickle, file_level_1o5th_game_coordinates, file_level_1o6th_game_variables
import file_level_2th_buttons
#import file_level_5th_monitoring_and_ocr
#only import the modules which are needed

def main():
	file_level_1o6th_game_variables.set_all_varibales_to_None()
	file_level_1o5th_game_coordinates.find_game_position()
	file_level_1o6th_game_variables.read_game_variables() #when it's my turn, run this function
	file_level_1o5th_game_coordinates.setup_coordinates() #setup coordiante should be placed one line upper
	print(file_level_2th_buttons.click_button())

if __name__ == '__main__':
	main()