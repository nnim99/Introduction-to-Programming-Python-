def main():
	string01  = str(input("Enter a sentence:",))
	string02  = str(input("Enter another sentence:",))
	sentence  = string01 + " " + string02 + " "
	sentence *= 3 
	print (sentence)
main()