def func():
	print("Enter three different values:")
	valueOne= input ("value One:")
	valueTwo= input ("value Two:")
	valueThree= input ("value Three:")
	#sum of values = valueOne+ valueTwo +valueThree
	sumOfValues=int(valueOne) + int(valueTwo) + int(valueThree)
	print ("Sum is:", sumOfValues)
	average = sumOfValues / 3
	print (average)
func()