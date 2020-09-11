def bubbleSort(list01):
	length = len(list01)-1
	
	while length !=0:
		k=0 
		while k!=length:
			word = list01[k]
			if list01[k] > list01[k+1]:
				list01[k] = list01[k+1]
				list01[k+1] = word
			k+=1
		length -= 1
		
		print(list01[0:length])
		
	return list01
def main():
	list01 = []
	for i in range(10):
		print("Enter Number",i+1)
		number = input()
		flag = False
		while flag == False:
			try:
				number = int(number)
			except Exception as e:
				print(e)
				number = input("Enter an Integer Number: ")
				flag = False
			else:
				number = number
				flag = True
				list01.append(number)
	print(bubbleSort(list01))
main()


