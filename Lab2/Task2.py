import math
def volumeOfCylinder(valueOne, valueTwo):
	volume= valueOne**2 *math.pi * valueTwo
	return volume

def func():
	varOne= float(input("Enter diameter:"))
	varOne /= 2
	VarTwo = float(input("Enter Height:"))
	print (volumeOfCylinder(varOne, VarTwo))

func()