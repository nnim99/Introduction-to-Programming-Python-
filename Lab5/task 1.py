def main():
	year = input("Enter an year:")

	try:
		year = int(year)
	except Exception as e:
		print ("Invalid year")
		print (e)
	else:
		if year % 4 == 0:
			print ("This is leap year:", year)
		else:
			print ("This is not a leap year:", year)
	finally:
		print("Program finished")
main()							