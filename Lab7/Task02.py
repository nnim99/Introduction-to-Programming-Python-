def func(one,two,three,four):
	try:
		one  = int(one)
		two  = int(two)
		three = int(three)
		four  = int(four)
	except Exception as e:
		print(e)
	else:
		list01 =  one,two,three,four

	list01 = list(list01)
	return list01
def main():

	print("First list elements!")
	one    = int(input("Enter marks in first:"))
	two    = int(input("Enter marks in second:"))
	three  = int(input("Enter marks in third:"))
	four   = int(input("Enter marks in fourth:"))
	list01 = func(one,two,three,four)

	print("Second list elements!")
	one01    = int(input("Enter marks in first:"))
	two01    = int(input("Enter marks in second:"))
	three01  = int(input("Enter marks in third:"))
	four01   = int(input("Enter marks in fourth:"))
	list02   = func(one01,two01,three01,four01)
	lists = list01 + list02 
	print(lists)
	list1  = lists[0:4]
	list1  = list(list1)
	list2  = lists[4:8]
	lists2 = list(list2)
	print("The first list entered was: ", list1)
	print("The second list entered was: ", list2)
main()