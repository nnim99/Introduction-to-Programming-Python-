def transpose(matrix01,rows,coloumns):
	i = 0
	matrix02 = []
	while i < coloumns:
		transposeRow = []
		j = 0
		while j < rows:
			element = matrix01[j][i]
			transposeRow.append(element)
			j += 1
		matrix02.append(transposeRow)
		i +=1
	return matrix02

def symmetric(matrix01,matrix02):
	if matrix01 == matrix02:
		return True	
	else:
		return False

def addition(matrix01,matrix02,rows,coloumns):
	i = 0 
	
	matrix03 = []
	while i < rows:
		addRow = []
		j = 0
		while j < coloumns:
			element = matrix01[i][j] + matrix02[i][j]
			addRow.append(element)
			j +=1
		matrix03.append(addRow)
		i += 1
	return matrix03

def subtraction(matrix01,matrix02,rows,coloumns):
	i = 0 
	
	matrix03 = []
	while i < rows:
		addRow = []
		j = 0
		while j < coloumns:
			element = matrix01[i][j] - matrix02[i][j]
			addRow.append(element)
			j += 1
		matrix03.append(addRow)
		i +=1
	return matrix03

def multiplication(matrix01,matrix02,rows,coloumns,coloumns2):
	matrix03 = []
	for k in range(rows):
		row01 = []
		i = 0 
		while i < coloumns2: #coloumn of second matrix
			j=0
			element01 = 0
			element = 0
			while j < coloumns: #coloumn of first matrix
				element = (matrix01[k][j] * matrix02[j][i])
				element = element01 + element
				element01 = element
				j +=1
			row01.append(element)
			i += 1
		matrix03.append(row01)
	return(matrix03)

def matrix(matrix01):
	result = ""
	for i in matrix01:
		matrixRow = ""
		for j in i:
			element = j
			element = str(element)
			matrixRow += element + "     "
		result += (matrixRow + "\n")
	return(result) 
def main():
	for i in range(10000000000000000000000):
		print("Select a number for performing operation")
		print("1. Calculate Transpose")
		print("2. Check whether matrix is symmetric")
		print("3. Adding the two given matrixes")
		print("4. Subtracting the two given matrixes")
		print("5. Multiplication of the two given matrixes")
		print("6. To Calculate Square of the Matrix")
		print("7. To switch off the calculator")
		number = int(input("Choose a number: "))
		if number == 1:
			print("Enter matrix size!")
			rows = int(input("Enter number of rows: " ))
			coloumns = int(input("Enter number of columns: "))
			i = 0 
			matrix01 = []
			while i < rows:
				theRow = []
				j = 0 
				while j < coloumns:
					print("The",i+1,"row enter element",j+1)
					element01 = input("Enter an element: ")
					theRow.append(element01)
					j += 1
				matrix01.append(theRow)
				i += 1
			transposeMatrix = transpose(matrix01,rows,coloumns)
			print("The origional matrix: ")
			print(matrix(matrix01))
			print("The transpose matrix: ")
			print(matrix(transposeMatrix))
		if number == 2:
			print("Note! symmetric matrix is always a square matrix.")
			print("Enter matrix size! ")
			rows = int(input("Enter number of rows: " ))
			coloumns = int(input("Enter number of columns: "))
			i = 0 
			matrix01 = []
			while i < rows:
				theRow = []
				j = 0 
				while j < coloumns:
					print("The",i+1,"row enter element",j+1)
					element01 = input("Enter an element: ")
					theRow.append(element01)
					j += 1
				matrix01.append(theRow)
				i += 1
			if rows != coloumns:
				print(matrix(matrix01))
				print("The given matrix is not symetric")
			else:
				transposeMatrix = transpose(matrix01,rows,coloumns)
				if matrix01 == transposeMatrix:
					print(matrix(matrix01))
					print("The given matrix is symmetric!")
				else:
					print(matrix(matrix01))
					print("The given matrix is not symmetric!")
		if number == 3:
			print("Warning! The size of the two matrixes must be equal!")
			print("Enter matrix one! ")
			row01 = int(input("Enter number of rows: " ))
			coloumn01 = int(input("Enter number of columns: "))
			i = 0 
			matrix01 = []
			while i < row01:
				theRow = []
				j = 0 
				while j < coloumn01:
					print("The",i+1,"row enter element",j+1)
					element01 = float(input("Enter an element: "))
					theRow.append(element01)
					j += 1
				matrix01.append(theRow)
				i += 1
			print("Enter matrix two! ")
			row02 = int(input("Enter number of rows: " ))
			coloumn02 = int(input("Enter number of columns: "))
			i = 0 
			matrix02 = []
			while i < row02:
				theRow = []
				j = 0 
				while j < coloumn02:
					print("The",i+1,"row enter element",j+1)
					element01 = float(input("Enter an element: "))
					theRow.append(element01)
					j += 1
				matrix02.append(theRow)
				i += 1
			if row01 != row02 and coloumn01 != coloumn02:
				print(matrix(matrix01),matrix(matrix02))
				print("Their sizes are not equal! They cannot be added!")
			else:
				resultantMatrix = addition(matrix01,matrix02,row01,coloumn01)
				print(matrix(matrix01))
				print( "    +   ")
				print(matrix(matrix02),"   =   ")
				print(matrix(resultantMatrix))
		if number == 4:
			print("Warning! The size of the two matrixes must be equal!")
			print("Enter matrix one! ")
			row01 = int(input("Enter number of rows: " ))
			coloumn01 = int(input("Enter number of columns: "))
			i = 0 
			matrix01 = []
			while i < row01:
				theRow = []
				j = 0 
				while j < coloumn01:
					print("The",i+1,"row enter element",j+1)
					element01 = float(input("Enter an element: "))
					theRow.append(element01)
					j += 1
				matrix01.append(theRow)
				i += 1
			print("Enter matrix two! ")
			row02 = int(input("Enter number of rows: " ))
			coloumn02 = int(input("Enter number of columns: "))
			i = 0 
			matrix02 = []
			while i < row02:
				theRow = []
				j = 0 
				while j < coloumn02:
					print("The",i+1,"row enter element",j+1)
					element01 = float(input("Enter an element: "))
					theRow.append(element01)
					j += 1
				matrix02.append(theRow)
				i += 1
			if row01 != row02 and coloumn01 != coloumn02:
				print(matrix(matrix01),matrix(matrix02))
				print("Their sizes are not equal! They cannot be subtracted!")
			else:
				resultantMatrix = subtraction(matrix01,matrix02,row01,coloumn01)
				print(matrix(matrix01))
				print( "   -   ")
				print(matrix(matrix02),"   =   ")
				print(matrix(resultantMatrix))
		if number == 5:
			print("Warning! The coloumn of first matrix and the row of second matrix must be equal!")
			print("Enter matrix one! ")
			row01 = int(input("Enter number of rows: " ))
			coloumn01 = int(input("Enter number of columns: "))
			i = 0 
			matrix01 = []
			while i < row01:
				theRow = []
				j = 0 
				while j < coloumn01:
					print("The",i+1,"row enter element",j+1)
					element01 = float(input("Enter an element: "))
					theRow.append(element01)
					j += 1
				matrix01.append(theRow)
				i += 1
			print("Enter matrix two! ")
			row02 = int(input("Enter number of rows: " ))
			coloumn02 = int(input("Enter number of columns: "))
			i = 0 
			matrix02 = []
			while i < row02:
				theRow = []
				j = 0 
				while j < coloumn02:
					print("The",i+1,"row enter element",j+1)
					element01 = float(input("Enter an element: "))
					theRow.append(element01)
					j += 1
				matrix02.append(theRow)
				i += 1
			if coloumn01 != row02:
				print(matrix(matrix01),"and")
				print(matrix(matrix02))
				print("Cannot be multiplied!")
			else:
				resultantMatrix = multiplication(matrix01,matrix02,row01,coloumn01,coloumn02)
				print(matrix(matrix01))
				print(matrix(matrix02))
				print("The multiplication of the two given matrixes is:")
				print(matrix(resultantMatrix))
		if number == 6:
			print("Warning! The matrix should be a Square Matrix")
			print("Enter matrix! ")
			row01 = int(input("Enter number of rows: " ))
			coloumn01 = int(input("Enter number of columns: "))
			i = 0 
			matrix01 = []
			while i < row01:
				theRow = []
				j = 0 
				while j < coloumn01:
					print("The",i+1,"row enter element",j+1)
					element01 = float(input("Enter an element: "))
					theRow.append(element01)
					j += 1
				matrix01.append(theRow)
				i += 1
			row02     = row01
			coloumn02 = coloumn01
			matrix02  = matrix01
			if coloumn01 != row02:
				print(matrix(matrix01))
				print("The Square of the Matrix cannot be calculated!")
			else:
				resultantMatrix = multiplication(matrix01,matrix02,row01,coloumn01,coloumn02)
				print(matrix(matrix01))
				print("The Square of the Matrix is:")
				print(matrix(resultantMatrix))
		if number == 7:
			break

main()




