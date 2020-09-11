def main():
	list01 = []
	list02 = []
	i = 0 
	while i < 20:
		number = int(input("Enter element between 10 and 100: "))
		list01.append(number)
		i += 1
	print("The elements are:",list01)
	j = 0
	k = 1
	length = 20
	count = 0
	while j< length:
		element01 = list01[j]
		list02.append(element01)
		

		while k <length:
			element02 = list01[k]
			if element01 != element02:
				count= count
			else:
				count += 1
			k +=1
		
			if count == 0:
				list02.append(element01)
			else:
				list02.append(element02)
		j += 1
	list02 = list02.sort()
	print(list02)
main()












