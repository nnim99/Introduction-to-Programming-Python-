import random
def main():
	print("Welcome to Nimra's blackjack program")
	number01 = random.randint(2,11)
	number02 = random.randint(2,11)
	number03 = random.randint(2,11)
	number04 = random.randint(2,11)
	sum01 = number01 + number02
	sum02 = number03 + number04
	if sum01>=21:
		print("The dealer wins. Game is over!", "The two numbers were",number01,number02,"So total:",sum01)
	if sum02>=21:
		print("The dealer wins. Game is over!","The two numbers for dealer were",number03,number04,"So total:",sum02)
	else:

		print("You get a",number01,"and a",number02)
		print("Your total is:",sum01)
	
		print("The dealer has a",number03,"showing, and a hidden card")
		print("His total is hidden too.")
		for i in range(1,100):
			hitOrStay= input("	Would you like to hit or stay? ")
			if hitOrStay == "hit":
				number0 = random.randint(2,11)
				sum01 += number0
				print("You drew a",number0)
				print("Your total is:",sum01)
				result = 1
				if sum01>=21:
					result = 2
					break
			elif hitOrStay=="stay":
				result = 3
				print("Okay, dealer's turn")
				print("His hidden card was a",number04)
				print("His total is: ",sum02)
				break
		if result == 2:
			print("You lose!")
		else:
			for j in range(1,100):
				if sum02<16:
					print("Dealer chooses to hit.")
					number05 = random.randint(2,11)
					sum02 += number05
					print("His total is: ",sum02)
					if sum02>=21:
						print("You win")
						break
				else: 
					print("Dealer stays")
					print("Dealer total is:",sum02)
					print("Your total is:",sum01)
					if sum01>sum02 and sum01<21:
						print("You win!")
					elif sum02>sum01 and sum02<21:
						print("Dealer wins!")
					else:
						print("Dealer wins!")	
					break
	



main()
