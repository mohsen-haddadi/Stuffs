import time
import screen_vars 

var1 = 1
def main():
	global var1
	while True:
		time.sleep(1)
		screen_vars.update_screen_var_1()
		print(var1)

if __name__ == '__main__':
	main()