def main():
	number = int(input("Enter a number between 1 and 30: "))
	try:
		if number<1 and number >130:
			raise Exception ("The number is outside the range")
	except Exception as e:
		print(e)
		print("The value taken is 1")
		number01=1
	else:
		number01 = number
	for var in range(0,number01):
		var="*"
		print(var)
main()
