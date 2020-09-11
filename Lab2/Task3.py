import math
def myfunc():

	valueOne= float(input("Enter a positive Number:"))
	valueTwo= float(input("Enter another negative Number:"))
	print (("Signs get swaped of two numbers:"), math.copysign(valueOne, valueTwo))
	print (("Absolute value is returned of negative number:"), math.fabs(valueTwo))
	print (("The square root of positive number is:"), math.sqrt(valueOne))
	print (("Negative number is power of positive number so the answer is:"), math.pow (valueOne, valueTwo))
	print (("If value One is entered in decimals then next largest possible integer value is:"), math.ceil(valueOne))
	print (("If value Two is entered in decimals then the smallest possible integer value is:"), math.floor(valueTwo))
	print (("The log of positive number entered with base 10 is:"), math.log10(valueOne))
	print (("The sine of value One is:"), math.sin(valueOne))
	print (("The cosine of value One is:"), math.cos(valueOne))
	print (("The tangent of value Two is:"), math.tan(valueTwo))

myfunc()		
