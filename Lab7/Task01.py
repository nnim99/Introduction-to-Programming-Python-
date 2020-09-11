def main():
	names  = ["Ali", "Ahsan", "Ahmed", "Zubair"]
	print(names)
	name01 = names[0]
	name02 = names[1]
	name03 = names[2]
	name04 = names[3]
	name1  = input("Enter a name which you want to appear first in list: ")
	name1  = name1.upper()
	names.pop(0)
	names.insert(0,name1)
	name2 = input("Enter a name which you want to appear second in list: ")
	name2 = name2.upper()
	names.pop(1)
	names.insert(1,name2)
	name3 = input("Enter a name which you want to appear thrd in list: ")
	name3 = name3.upper()
	names.pop(2)
	names.insert(2,name3)
	name4 = input("Enter a name which you want to appear last in list: ")
	names.pop(3)
	names.insert(3,name4)
	print(names)
	secondLastName = names[-2]
	print(secondLastName)
main()


