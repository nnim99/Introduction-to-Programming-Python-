def multiplication(number):
	if number > 0:
		return number * multiplication(number-1)
	else:
		return 1 
def main():
	number = input("Enter the integer till you want to have factorial: ")
	flag = False
	while flag == False:
		try:
			number = int(number)
		except Exception as e:
			print(e)
			number = input("Enter an integer Number: ")
			flag = False
		else:
			number = number
			flag = True
	print("The factorial of the number: ",multiplication(number))
main()