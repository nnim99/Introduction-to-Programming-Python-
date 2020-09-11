def func():
	number = input("Enter an integer number:")

	try:
		number = int(number)
		if number%2 == 0:
			result = (number*3) + 1
		else:
			result = number/2
	except Exception as e:
		print("Invalid Input")
		print(e)
	else:
		print("The result is:",result)
func()		
