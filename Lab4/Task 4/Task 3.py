def func():
	late = int(input("Enter Number of Days a person is late on submitting the book=",))
	day  = int(input("Enter number of days:"))

	if late <=5:
		days = day
		fine = days*0.5
		print ("The fine is:", fine)
	elif late > 5 and late <= 10 :
		days = day 
		fine = days*1
		print ("The fine is:", fine)	
	elif late > 10 and late <= 30 :
		days = day 
		fine = days*5
		print ("The fine is:", fine)
		
	else:
		print ("Your membership is cancelled")
func()
		