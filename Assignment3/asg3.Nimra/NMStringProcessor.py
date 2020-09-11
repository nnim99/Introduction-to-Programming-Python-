def capitalize(string):
	index01 = string[0]
	if index01 == "a" or index01 == "A":
		result = "A"
	elif index01 == "b" or index01 == "B":
		result = "B"
	elif index01 == "c" or index01 == "C":
		result = "C"
	elif index01 == "d" or index01 == "D":
		result = "D"
	elif index01 == "e" or index01 == "E":
		result = "E"
	elif index01 == "f" or index01 == "F":
		result = "F"
	elif index01 == "g" or index01 == "G":
		result = "G"
	elif index01 == "h" or index01 == "H":
		result = "H"
	elif index01 == "i" or index01 == "I":
		result = "I"
	elif index01 == "j" or index01 == "J":
		result = "J"
	elif index01 == "k" or index01 == "K":
		result = "K"
	elif index01 == "l" or index01 == "L":
		result = "L"
	elif index01 == "m" or index01 == "M":
		result = "M"
	elif index01 == "n" or index01 == "N":
		result = "N"
	elif index01 == "o" or index01 == "O":
		result = "O"
	elif index01 == "p" or index01 == "P":
		result = "P"
	elif index01 == "q" or index01 == "Q":
		result = "R"
	elif index01 == "r" or index01 == "R":
		result = "R"
	elif index01 == "s" or index01 == "S":
		result = "S"
	elif index01 == "t" or index01 == "T":
		result = "T"
	elif index01 == "u" or index01 == "U":
		result = "U"
	elif index01 == "v" or index01 == "V":
		result = "V"
	elif index01 == "w" or index01 == "W":
		result = "W"
	elif index01 == "x" or index01 == "X":
		result = "X"
	elif index01 == "y" or index01 == "Y":
		result = "Y"
	elif index01 == "z" or index01 == "Z":
		result = "Z"
	else:
		result = index01
	string = result + string[1:]
	return string
def count(string,character):
	count = 0 
	for var in string:
		if var == character:
			count += 1
	return count
def length(string):
	length01 = 0
	for var in string:
		length01 += 1
	return length01
def find(string,word):
	index01 = -1
	flag = False
	for var in string:
		index01 += 1
		if var == word:
			return index01
			flag = True
	if flag != True:
		return -1
def rfind(string,word):
	index01 = -1
	length01 = length(string) -1
	flag = False
	for i in range(length01,0,-1):
		if string[i] == word:
			result = i
			return result
			flag = True
			break
	if flag != True:
		return -1
def findWithBounds(string,word,start,end):
	index01 = -1
	flag = False
	for i in range(start,end+1):
		if string[i] == word:
			result = i
			return result
			flag = True
			break
	if flag != True:
		return -1
def countWithBounds(string,word,start,end):
	count = 0
	string = string[start:end+1]
	for var in string:
		if var == word:
			count +=1
	return count
def index(string,word):
	index01 = -1
	flag = False
	for var in string:
		index01 += 1
		if var == word:
			return index01
			flag = True
	if flag != True:
		return "Error"
	
def rindex(string,word):
	index01 = -1
	length01 = length(string) -1
	flag = False
	for i in range(length01,0,-1):
		if string[i] == word:
			result = i
			return result
			flag = True
			break
	if flag != True:
		return "Error"
	
def indexWithBounds(string,word,start,end):
	index01 = -1
	flag = False
	for i in range(start,end+1):
		if string[i] == word:
			result = i
			return result
			flag = True
			break
		else:
			return "Error"
def swapcase(string):
	capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	small   = "abcdefghijklmnopqrstuvwxyz"
	length01 = length(string)
	for i in range(length01):
		word = string [i]
		if word in small:
			index01 = small.index(word)
			letter = capital[index01]
		elif word in capital:
			index01 = capital.index(word)
			letter = small[index01]
		else:
			letter = word
		if i == 0:
			string = letter + string[i+1 : length01]
		else:
			string = string[0:i]+letter + string[i+1 : length01]
	return string
def upper(string):
	index = -1
	capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	small   = "abcdefghijklmnopqrstuvwxyz"
	length01 = length(string)
	for i in range(length01):
		word = string [i]
		if word in small:
			index01 = small.index(word)
			letter = capital[index01]
		else:
			letter = word
		if i == 0:
			string = letter + string[i+1 : length01]
		else:
			string = string[0:i]+letter + string[i+1 : length01]
	return string
def lower(string):
	index = -1
	capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	small   = "abcdefghijklmnopqrstuvwxyz"
	length01 = length(string)
	for i in range(length01):
		word = string [i]
		if word in capital:
			index01 = capital.index(word)
			letter = small[index01]
		else:
			letter = word
		if i == 0:
			string = letter + string[i+1 : length01]
		else:
			string = string[0:i]+letter + string[i+1 : length01]
	return string
def isalpha(string):
	index = -1
	capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	small   = "abcdefghijklmnopqrstuvwxyz"
	length01 = length(string)
	flag = 1
	for i in range(length01):
		word = string [i]
		if word in capital:
			flag *= 1
		elif word in small:
			flag *= 1
		else:
			flag *= 0
	if flag == 1:
		return 	True
	else:
		return False
def islower(string):
	index = -1
	capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	small   = "abcdefghijklmnopqrstuvwxyz"
	length01 = length(string)
	flag = 1
	for i in range(length01):
		word = string [i]
		if word in capital:
			flag *= 0
		elif word in small:
			flag *= 1
		else:
			flag *= 0
	if flag == 1:
		return 	True
	else:
		return False
def isupper(string):
	index = -1
	capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	small   = "abcdefghijklmnopqrstuvwxyz"
	length01 = length(string)
	flag = 1
	for i in range(length01):
		word = string [i]
		if word in capital:
			flag *= 1
		elif word in small:
			flag *= 0
		else:
			flag *= 0
	if flag == 1:
		return 	True
	else:
		return False
def isdigit(string):
	index = -1
	digit = "0123456789"
	string = str(string)
	length01 = length(string)
	flag = 1
	for i in range(length01):
		word = string [i]
		if word in digit:
			flag *= 1
		else:
			flag *= 0
	if flag == 1:
		return 	True
	else:
		return False
def isspace(string):
	index = -1
	space = " "
	length01 = length(string)
	flag = 1
	for i in range(length01):
		word = string [i]
		if word in space:
			flag *= 1
		else:
			flag *= 0
	if flag == 1:
		return 	True
	else:
		return False
def replace(string,word01,word02):
	length01 = length(string)
	for i in range(length01):
		letter = string[i]
		if letter == word01:
			word = word02
			if i == 0:
				string = word + string [i+1:length01]
			else:
				string = string[0:i] + word + string[i+1:length01]
	return string
def replaceWithBounds(string,word01,word02,start,end):
	length01 = length(string)
	for i in range(start,end+1):
		letter = string[i]
		if letter == word01:
			word = word02
			if i == 0:
				string = word + string [i+1:length01]
			else:
				string = string[0:i] + word + string[i+1:length01]
	return string
def reverse(string):
	string01 = ""
	length01 = length(string)-1
	for i in range(length01,-1,-1):
		string01 += string[i]
	return string01
def lstrip(string,character):
	index = -1
	length01 = length(string)
	for i in range(length01):
		if string[i] == character:
			index +=1
		else:
			break
	string = string[index+1:length01]
	return string
def rstrip(string,character):
	length01 = length(string)
	index = length01-1
	for i in range(length01-1,-1

		,-1):
		if string[i] == character:
			index -=1
		else:
			break
	string = string[0:index+1]
	return string
def strip(string,character):
	string = lstrip(string,character)
	string = rstrip(string,character)
	return string
def startsWith(string,begginning):
	length01 = length(string)
	length02 = length(begginning)
	flag = 1
	for i in range(length02):
		if string[i] == begginning [i]:
			flag *= 1
		else: 
			flag *= 0
	if flag == 1:
		return True
	else:
		return False
def endsWith(string,ending):
	length01 = length(string)
	length02 = length(ending)
	length02 = -1*length02
	flag = 1
	for i in range(length02,-1):
		if string[i] == ending [i]:
			flag *= 1
		else: 
			flag *= 0
	if flag == 1:
		return True
	else:
		return False
def title(string):
	string = capitalize(string)
	index01 = 0
	length01 = length(string)
	for i in range(length01):
		if string[i]== " " and i != length01-1:
			letter = string[i+1]
			letter = upper(letter)
			string = string[0:i+1] + letter + string[i+2:length01]
	return string
