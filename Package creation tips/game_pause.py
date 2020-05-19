import keyboard , time 
""" source: https://stackoverflow.com/questions/24072790/detect-key-press-in-python """

def game_is_puased():
	""" if game is paused, check_mode gets True """
	#t0 = time.time()
	if keyboard.is_pressed("end"): 
		print("game is paused") 
		#here DON'T assign check_mode to True, becuase if Just_Seated is 
		#True before cards are dealt,on begining of new hand it will just check and folds. 
		return True
	#print("keyboard.is_pressed time consuption:",time.time()-t0)
	return False

print("hold 'End' button to pause the game")

while True: #main loop
	print("main loop")
	while True: #loops such as pixel matching for my turn or starting new hand
		if game_is_puased():
			input("press Enter to countinue...") 
			#here run check_connectivity() function (Just_Seated and check_mode will be assigned True in check_connectivity() if needed)
			break 
		time.sleep(2) #program excection(pixel matching)
		print("in sub loop")
		