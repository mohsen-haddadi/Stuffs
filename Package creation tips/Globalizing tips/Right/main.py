import time
import screen_vars 
from decision_making.decide import decide 

def main():
	while True:
		time.sleep(1)
		screen_vars.update_screen_var_1()
		print(decide())

if __name__ == '__main__':
	main()