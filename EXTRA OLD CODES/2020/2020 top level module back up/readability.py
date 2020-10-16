# creating readable functions is non sense.
def is_read_my_cards_readable():
	if 'Unknown' in read_my_cards():
		return False
	else:
		return True

def is_ocr_bet_readable():
	pass

def is_fold_button_readable():
	pass

# in main file:
if is_read_my_cards_readable():
	my_1th_card, my_2th_card = read_my_cards()
else:
	game_is_fixed, check_mode = fix_game_disruption()
	if game_is_fixed and not check_mode:
		is_read_my_cards_readable():
			my_1th_card, my_2th_card = read_my_cards()
		else:
			check_mode = True
			screen_shot_error("can't read cards")
	elif game_is_fixed and check_mode:
		pass #check_mode is True now
	elif not game_is_fixed:
		raise Exception #call operator