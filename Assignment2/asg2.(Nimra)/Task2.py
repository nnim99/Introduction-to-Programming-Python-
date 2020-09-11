def main():
	name    = ["Ahmed","Sara","Nimra","Saad"]
	pin02   = [4122,7614,5412,1234]
	aNumber = [426582363861236,836329764923734,823423987473945,987324876775482]
	balance = [200000,32456,194852,235764]
	for i in range(1,100000000000):
		name01 = input("Enter name: ")
		for var in name:
			if var == name01:
				index = name.index(name01)
				pin01 = int(input("Enter your four digit pin:"))

				for pin in pin02:
					if  pin == pin01 :
						print("Your account number:",aNumber[index])
						print("Your balance:",balance[index])
						process = input("Do you want to perform transection(T) or tranfer funds(F)? (T or F) ?")
						process = process.lower()
						if process == "t":
							amount = int(input("Enter amount for transection: "))
							if amount> balance[index]:
								print("You cannot perform this transection! Ammount entered is more than your available balance!")
							else:
								newBalance = balance[index] - amount
								print("Available balance is:",newBalance)
						elif process=="f":
							amount = int(input("Enter the amount you want enter funds into your account: "))
							newBalance = balance[index] + amount
							continue
main()



