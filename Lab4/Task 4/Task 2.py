def func():
	firstName     = str(input("Enter first name of the customer:",))
	lastName      = str(input("Enter last name of the customer:", ))
	numberOfTapes = int(input("Enter Number of tapes:",))
	day           = str(input("Is this a value day? (Yes or No)",))
	day = day.lower()

	customer      = str(input("Is this a special Customer? (Yes or No)"))
	customer =customer.lower()

	totalAmount   = numberOfTapes*1.5
	discountPrice = totalAmount - 0.5

	if (customer == "yes") and (day == "yes" or "no"):
		print("The amount before discount is:",totalAmount, "$")
		print("The total amount after dicount is:",discountPrice, "$")
	elif (customer == "no") and (day == "yes"):
		print("The amount before discount is:",totalAmount, "$")
		print("The total amount after dicount is:",discountPrice, "$")
	elif (customer == "no") and (day == "no"):
		print("The amount before discount is:",totalAmount, "$")
	else:
		print ("None")
func()
