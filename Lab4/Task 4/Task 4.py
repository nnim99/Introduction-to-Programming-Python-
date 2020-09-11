def func():
	health = str(input("Is patient's health is excellent or poor?"))
	health = health.lower()
	gender = str(input("Male or Female?"))
	gender = gender.lower()
	age    = int(input("Enter patient's age?",))
	city   = str(input("City or Village?"))
	city   = city.lower()

	if (gender == "male") and ((age > 25) and (age < 35)) and (city == "city") and (health == "excellent"):
		print ("The person can be insured.")
		print ("Premium rate = Rs 4 per thousand ")
		print ("Maximum amount = 2 lakhs")
	elif (gender == "female") and ((age > 25) and (age < 35)) and (city == "city") and (health == "excellent"):
		print ("The person can be insured.")
		print ("Premium rate = Rs 3 per thousand ")
		print ("Maximum amount = 1 lakhs")
	elif (gender == "male") and ((age > 25) and (age < 35)) and (city == "village") and (health == "poor"):
		print ("The person can be insured.")
		print ("Premium rate = Rs 6 per thousand ")
		print ("Maximum amount = 10,000 ") 
	else:	
	 	print("Person cannot be insured")

func()