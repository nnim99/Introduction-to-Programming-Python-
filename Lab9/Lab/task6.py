def main():
    rows = int(input("Enter the number of rows: "))
	columns = int(input("Enter the number of columns: "))
	matrix01 = []
	for c in range(1,rows+1):
		rowlist =[]
		for row in range(1,columns+1):
			print("Enter the element in ",row,"row",c,': ', end='')
			rowlist.append(input())
		matrix01.append(rowlist)
	for c in range(rows):
		for row in range(columns):
			print(matrix01[c][row], ' ',end='')
		print("\n")
	for c in range(columns):
		for row in range(rows):
			print(matrix01[row][c], ' ',end='')
		print("\n")
main()

 
