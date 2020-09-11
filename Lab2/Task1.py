def heightFromInToCm(valueOne):
	heightInCm= valueOne*2.54
	return heightInCm

def heightFromInTOFeets(valueTwo):
	heightInFeets= valueTwo/12
	return heightInFeets

def func():
	valOne= float(input("Enter height in inches:"))
	print (("Height in Cm"), heightFromInToCm(valOne))
	print (("Height in Feets"), heightFromInTOFeets(valOne))
func()
