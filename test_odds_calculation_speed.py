import time
import decision_making.rules_and_info.odds as odds

board_cards = ['7s', '9h', '9d']
my_hole_cards = ['6s', '9s']

print('board cards are: %s' %board_cards)
print('my hole cards are: %s' %my_hole_cards)

t0 = time.time()

print(f'win_odds is: {odds.win_odds(board_cards, my_hole_cards)}')
all_possible_win_odds_list = odds.all_possible_win_odds(board_cards, my_hole_cards) 
print(f'next_win_odds_average is: {odds.next_win_odds_average(all_possible_win_odds_list)}')
print(f'draw_odds is: {odds.draw_odds(all_possible_win_odds_list, 95)}')

print(f'Time consumption is: {round((time.time() - t0), 2)}')

