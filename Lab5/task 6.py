def func(number):
	digit1 = number //1000
	number = number % 1000
	digit2 = number // 100
	number = number % 100
	digit3 = number // 10
	number = number % 10
	digit4 = number

	digit01= (digit1 + 7) %10
	digit02= (digit2 + 7) %10
	digit03= (digit3 + 7) %10
	digit04= (digit4 + 7) %10


	return (digit03,digit04,digit01,digit02 )
def main():
	number1 = input("Enter a four digit number:")
	try:
	 	number1 = int(number1)	
	 	if len(number1)!= 5 :
	 		raise Exception ("Number greater or less than 4 digits")
	except Exception as e:
	 	print(e)
	else:
	 	number1 = int(number1)
	print ("The encrypted form is:",(func(number1)))
main()	 				


