def Power(valueOne, valueTwo, valueThree):
	result= valueOne**valueTwo % valueThree
	return result

def func():
	VarOne= float(input("Input value one:"))
	varTwo= float(input("Input value Two:"))
	varThree= float(input("Input value Three:"))
	print (Power(VarOne,varTwo,varThree))

func()	