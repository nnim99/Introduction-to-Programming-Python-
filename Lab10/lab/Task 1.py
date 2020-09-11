def main():
	list01 = []
	i = 0 
	while i < 10:
		element= int(input("Enter element in list"))
		list01.append(element)
		i +=1
	index = 0
	length = 10
	while index < length:
		element01 = list01[index]
		element02 = list01[index+1]
		if element01 > element02:
			maximum = element01
			location = index
		else:
			maximum = element02
			location = index+1
	print("The maximum number is:",maximum)
	print("The location is:",location)
main()



