userId   = "Nimra.12"
pin      = 1234
amount   = 2000
def func():
	global userId
	global pin

	userName = input("Enter user ID :")
	pin01    = input("Enter Pin:")
	
	try:
		if userName != userId:
			raise Exception ("user ID is not valid")
	except Exception as e:
		print (e)
	else:
		print(userName)
		if pin01 != int(pin) and len(pin01)!=4: 
			print("The lenght of pin is Invalid")
			func()
		else:
			print("Pin is valid")
func()				

def transection():
	global amount

	transection = input("Enter amount for transection:")
	try:
		transection = int(transection)
		if transection > amount: 
			raise Exception ("Amount requested for transection is greater than available balance!")
	except Exception as e:
		print(e)
		transection()
	else:
		result = amount - transection
		print ("The available balance is:", result)
transection()					

