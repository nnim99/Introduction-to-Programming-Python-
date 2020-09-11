def main():
	value01 = 0
	value02 = 1
	for var in range(10):
		if var == 0:
			print("0")
		elif var == 1:
			print("1")
		else: 
			value03 = value01 + value02
			value01 = value02
			value02 = value03
			print(value03)
main()
