def main():
	list0 = []
	one   = float(input("Enter a number: "))
	two   = float(input("Enter a number: "))
	three = float(input("Enter a number: "))
	four  = float(input("Enter a number: "))
	five  = float(input("Enter a number: "))
	six   = float(input("Enter a number: "))
	seven = float(input("Enter a number: "))
	eight = float(input("Enter a number: "))
	nine  = float(input("Enter a number: "))
	ten   = float(input("Enter a number: "))
	list0.append(one)
	list0.append(two)
	list0.append(three)
	list0.append(four)
	list0.append(five)
	list0.append(six)
	list0.append(seven)
	list0.append(eight)
	list0.append(nine)
	list0.append(ten)
	print(list0)

	length = len(list0)
	print ("The length of list: ", length)

	maximum = max(list0)
	print ("The maximum number from list: ", maximum)

	minimum = min(list0)
	print ("The minimum number from list: ", minimum)

	difference = maximum - minimum
	print ("The difference between the max and min: ", difference)

	sumOfList = sum(list0)
	print ( "The sum of list number is: ", sumOfList)

	average = sumOfList/length
	print ("The average of list numbers is: ", average)

	sort0 = sorted(list0)
	print ("The sorted list: ", sort0)

	index0 = list0.index(maximum)
	del list0[index0]
	
	print(list0)
main()	




