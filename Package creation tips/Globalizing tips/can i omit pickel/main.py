from decision_making.decide import decide

def main():
	monitoring_variable = 0
	while True:
		monitoring_variable += 1
		print(decide())

if __name__ == '__main__':
	main()