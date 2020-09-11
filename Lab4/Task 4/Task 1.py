def func():
	noOfHours  = float(input("Enter Number of hours:",))

	pay        = 20000
	payPerHour = 20000/40 #it will be 500 Rs per day
	if noOfHours == 40: 
		payment = int(pay)
		tax     = int(0.28*payment)
		print ("Gross Pay=", payment, "Rs")
		print ("Taxes=", tax, "Rs")
		print ("Net Pay=", payment - tax,"Rs")
	elif (noOfHours > 40) and (noOfHours <= 45):
		extraHours = noOfHours - 40
		payment = int(pay + (extraHours*payPerHour*1.5))
		tax     = int(0.28*payment)
		print ("Gross Pay=", payment, "Rs")
		print ("Taxes=", tax, "Rs")
		print ("Net Pay=", payment - tax,"Rs") #Net pay is difference between GrossPay and Taxes
		
	elif noOfHours > 45:
		extraHours = noOfHours - 40
		payment = int(pay + (extraHours*payPerHour*2))
		tax     = int(0.28*payment)
		print ("Gross Pay=", payment, "Rs")
		print ("Taxes=", tax, "Rs")
		print ("Net Pay=", payment - tax,"Rs")
	else:
		print("Number of hours spent are not sufficient to get salary")
func()	
	
