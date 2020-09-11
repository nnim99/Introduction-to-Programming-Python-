def func (userInput1, userInput2):
	userInput2 += userInput1
	return userInput2

def main():
	number = int(input("Enter the number of enteries: "))
	number2 = int(input("Enter a number: "))
	x=1

	while x<number:
		a =int(input("Enter a number: "))
		x=x+1
		sum01 = func(number2,a)
	print("Sum of numbers are: ", sum01)
main()	