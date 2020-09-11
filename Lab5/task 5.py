def func(numb):
	try:
		if len(str(numb)) != 5:
			raise Exception ("Enter a five digit integer only!")
		numb=int(numb)

	except Exception as e:
		print("Invalid Input")
		print(e)

	else:
		numb=int(numb)
		a=number//10000
		digit1=a%10000
		b=digit1//1000
		digit2=b%1000
		c=digit2//100
		digit3=c%100
		d=digit3//10
		digit4=d%10
		e=digit4//1
		digit5=e%10

		
		if digit1 == digit5 or digit2 == digit4:
			print("The given integer is a palindrome!")
		else:
			print("The entered integer is not a palindrome!")
		

		
def main():
	number=input("Enter a five digit number: ")
	func(number)
main()