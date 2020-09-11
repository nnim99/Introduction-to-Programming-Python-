def addition(number):
	if number > 0:
		return number + addition(number-1)
	else:
		return 0 
def main():
	number = input("Enter the integer till you want to have sum: ")
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
	print("The sum till the number: ",addition(number))
main()