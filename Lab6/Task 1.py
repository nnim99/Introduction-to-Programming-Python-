def main():
	side01 = int(input("Enter an integer value for one side of triangle: ",))
	side02 = int(input("Enter an integer value for second side of triangle: ",))
	side03 = int(input("Enter an integer value for third side of triangle: ",))
	if side01>side02 and side01>side03:
		longLength = side01
		if ((side02**2) + (side03**2)) == longLength**2 :
			print("The three integers are side of the right triangle")
		else:
			print("The three integers are not side of the right triangle")	

	elif side02>side01 and side02>side03:
		longLength = side02
		if ((side01**2) + (side03**2)) == longLength**2 :
			print("The three integers are side of the right triangle")
		else:
			print("The three integers are not side of the right triangle")
	elif side03>side01 and side03>side02:
		longLength = side03
		if ((side01**2) + (side02**2)) == longLength**2 :
			print("The three integers are side of the right triangle")
		else:
			print("The three integers are not side of the right triangle")
main()