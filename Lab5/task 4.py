def func(marks):
	number = marks

	if number > 90:
		grade = "A"
	elif number > 80 and number < 90:
		grade = "B"				
	elif number > 70 and number < 80:
		grade = "C"
	elif number > 60 and number <70:
		grade = "D"
	else:
		grade = "F"
	return grade
			
def main():
	mark = input("Enter marks:")
	try:
		if int(mark) > 100:
			raise Exception ("The marks are greater than 100")
		mark = int(mark)	
	except Exception as e:
		print (e)
	else:
		print ("Grade is:", (func(mark)))
main()
				
