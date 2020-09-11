def func():
	fiveDigitNumber= input("Enter five digit number:")
	value= int(fiveDigitNumber)
	#using modulus to get remainder 
	fifthDigit= value % 10
	#using integer division by 10 to get quotient part
	value= value//10
	fourthDigit = value % 10 
	value= value // 10 
	thirdDigit= value % 10 
	value= value // 10
	secondDigit= value % 10 
	value= value // 10
	firstDigit= value % 10

	#comma itself gives one space
	print (fifthDigit, " ",fourthDigit," ",thirdDigit," ",secondDigit," ",firstDigit)
func()	

