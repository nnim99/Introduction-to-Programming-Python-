def func(var01, val01, val02):
	statement = var01[val01:val02]
	return statement
def main():
	sentence = str(input("Enter a sentence:",))
	sentence = sentence.upper()
	number01 = int(input("Select starting index no.:",))
	number02 = int(input("Select ending index no.:", ))
	print ("The selected area is:", func(sentence, number01, number02))
main()	