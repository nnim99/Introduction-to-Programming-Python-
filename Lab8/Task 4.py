import random
def guess(number02):
	tries = 5
	for var in range (0,tries):
		number01 = int(input("Your guess: ",))
		if number01 != number02:
			print("That is incorrect. Guess again.!")
			continue
			
		print("Thats right! You guessed it.")

def main():
	number = random.randint(1,10)
	print("Enter a number from 1 to 10! Guess the number!")
	
	guess(number)
	print(guess)
main()


