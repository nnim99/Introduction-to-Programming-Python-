def factorial(userInput,number01):
	userInput *= number01
	return userInput
def func():
	number = int(input("Enter number for which you want to calculate factorial: "))
	var01  = 1
	print ("x","    ","Factorial of x")
	for var in range(1,number+1):
		result = factorial(var01,var)
		var01 = result
		
		print (var,"   ",result)
func()


