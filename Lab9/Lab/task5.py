def main():
	print("Enter space after every entery/element")
	m1row1 = input("Enter the first row of the matrix: ").split()
	m1row2 = input("Enter the second row of the matrix: ").split()
	m1row3 = input("Enter the third row of the matrix: ").split()

	m2row1 = input("Enter the first row of the matrix: ").split()
	m2row2 = input("Enter the second row of the matrix: ").split()
	m2row3 = input("Enter the third row of the matrix: ").split()

	m1row1 = list(map(int, m1row1))
	m2row1 = list(map(int, m2row1))
	m1row2 = list(map(int, m1row2))
	m2row2 = list(map(int, m2row2))
	m3row3 = list(map(int, m1row3))
	m3row3 = list(map(int, m2row3))

	matrix1 = [m1row1,m1row2,m1row3]
	matrix2 = [m2row1,m2row2,m2row3]

	for rowsM1 in matrix1:
		eachRowM1 = ""
		for elementM1 in rowsM1:
			enteryM1 = str(elementM1) + "	"
			eachRowM1 += enteryM1
		print (eachRowM1)

	print("")
	for rowsM2 in matrix2:
		eachRowM2 = ""
		for elementM2 in rowsM2:
			enteryM2 = str(elementM2) + "	"
			eachRowM2 += enteryM2
		print (eachRowM2)
	print("")

	for i in range(3):
		productRow = ""
		for j in range(3):
			element = matrix1[i][j] * matrix2[j][i]
			productRow = productRow + str(element) +"	"
		print(productRow)
main()


