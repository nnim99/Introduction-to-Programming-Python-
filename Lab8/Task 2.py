def main():
	number = int(input("Enter number of enteries: "))
	list01 = []

	for var in range(0,number):
		number01 = int(input("Enter a number: "))
		list01.append(number01)

	length = len(list01)

	index = 0
	if list01[index] < list01[index+1]:
		smallestNumber =  list01[index]
	else:
		smallestNumber =list01[index+1]
	for index in range(1,length-1):	
		if smallestNumber < list01[index]:
			smallestNumber =smallestNumber
		else:
			smallestNumber = list01[index]
		index+=1


	print("The minimum value is: ",smallestNumber)
main()



