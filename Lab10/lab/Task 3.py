def main():
	i = 0 
	j = 0
	row01 = []
	row02 = []
	row03 = []
	row04 = []
	row05 = []
	row06 = []
	matrix01 = []
	matrix02 = []
	print("Matrix One: ")
	print("Row 1 element")
	while i < 3:
		element = float(input("Enter element: "))
		row01.append(element)
		i += 1
	print("Row 2 element")	
	i = 0
	while i < 3:
		element = float(input("Enter element: "))
		row02.append(element)
		i += 1
	print("Row 3 element")
	i = 0
	while i < 3:
		element = float(input("Enter element: "))
		row03.append(element)
		i += 1
	
	i = 0
	print("Matrix two: ")
	print("Row 1 element")
	while i < 3:
		element = float(input("Enter element: "))
		row04.append(element)
		i += 1
	print("Row 2 element")
	i = 0

	while i < 3:
		element = float(input("Enter element: "))
		row05.append(element)
		i += 1
	print("Row 3 element")
	i = 0
	while i < 3:
		element = float(input("Enter element: "))
		row06.append(element)
		i += 1
	
	matrix01.append(row01)
	matrix01.append(row02)
	matrix01.append(row03)
	matrix02.append(row04)
	matrix02.append(row05)
	matrix02.append(row06)
	element01 = 0
	row07 = []
	row08 = []
	row09 = []
	matrix03 = []
	k = 0
	while k < 1:
		element01 = 0
		while j<3:
			product = matrix01[k][j] * matrix02 [j][k]
			element01 += product
			j+=1
		k +=1
		row07.append(element01)
		print(row07)
	k = 1
	while k < 2:
		element01 = 0
		while j<3:
			product = matrix01[k][j] * matrix02 [j][k]
			element01 += product
			j+=1
		k +=1	
		print(row07)
	
	k = 2
	while k < 3:
		element01 = 0
		while j<3:
			product = matrix01[k][j] * matrix02 [j][k]
			element01 += product
			j+=1
			row07.append(element01)
		k+=1
		
		print(row07)
main()


