def reverse(word):
	wordIsReversed = word[::-1]
	return wordIsReversed
def main():	
	sentence = input("Enter a sentence containing 5 words:",)
	index01  = sentence.find(" " , 0)
	word01   = sentence[0:index01]
	index02  = sentence.find(" ", index01+1)
	word02   = sentence[index01:index02]
	index03  = sentence.find(" ", index02+1)
	word03   = sentence[index02:index03]
	index04  = sentence.find(" ", index03+1)
	word04   = sentence[index03:index04]
	index05  = sentence.find(" ", index04+1)
	word05   = sentence[index04: ]
	print (reverse(word01) + " " + reverse(word02) + reverse(word03) + reverse(word04) + reverse(word05))

main()