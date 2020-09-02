import time
import config , d


def main():
	#config.update_screen_var_1()
	config.var1 = 5
	while True:
		time.sleep(1)
		
		config.var1 += 20
		print(d.decide())

if __name__ == '__main__':
	main()