#💊 : means edited

def click_coordinates(game_position, name):
    if name == 'fold': #💊
        coordinate = ( game_position[0]+187, game_position[1]+468 )
    elif name == 'check': #💊
        coordinate = ( game_position[0]+303, game_position[1]+471 )
    elif name == 'call': #💊
        coordinate = ( game_position[0]+297, game_position[1]+466 )
    elif name == 'bet': #💊
        coordinate = ( game_position[0]+416, game_position[1]+466 )
    elif name == 'raise': #💊
        coordinate = ( game_position[0]+430, game_position[1]+466 )
    elif name == 'type_blinds': #💊
        coordinate = ( game_position[0]+455, game_position[1]+408 )
    elif name == 'half_pot': #💊
        coordinate = ( game_position[0]+332, game_position[1]+375 )
    elif name == 'pot': #💊
        coordinate = ( game_position[0]+379, game_position[1]+378 )
    elif name == 'all_in': #💊
        coordinate = ( game_position[0]+431, game_position[1]+375 )


    elif name == 'available_seat_1': #💊
        coordinate = ( game_position[0]+107, game_position[1]+238 )
    elif name == 'available_seat_2': #💊
        coordinate = ( game_position[0]-98, game_position[1]+176 )
    elif name == 'available_seat_3': #💊
        coordinate = ( game_position[0]-98, game_position[1]+34 )
    elif name == 'available_seat_4': #💊
        coordinate = ( game_position[0]+108, game_position[1]-29 )
    elif name == 'available_seat_5': #💊
        coordinate = ( game_position[0]+314, game_position[1]+34 )
    elif name == 'available_seat_6': #💊
        coordinate = ( game_position[0]+316, game_position[1]+178 )

    elif name == 'exit': #💊
        coordinate = ( game_position[0]+173, game_position[1]-263 )
    elif name == 'menu': #💊
        coordinate = ( game_position[0]-136, game_position[1]-257 )
    elif name == 'buy_in': #💊
        coordinate = ( game_position[0]-40, game_position[1]+317 )
    elif name == 'max_buy_in': #💊
        coordinate = (game_position[0]+214, game_position[1]+141)
    elif name == 'min_buy_in': #💊
        coordinate = (game_position[0]+124, game_position[1]+141)
    elif name == 're_buy': #💊
        coordinate = ( game_position[0]+358, game_position[1]-208 )
    elif name == 'i_am_back': #💊
        coordinate = ( game_position[0]+168, game_position[1]+473 )
        
    return coordinate


