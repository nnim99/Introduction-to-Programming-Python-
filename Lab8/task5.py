def prime(value):
	for number in range(2,value-1):
		if(value%number==0):
			return
	print(value)
def main():
	print("Following is the list of prime numbers from 1 to 10,000")
	for var in range(1,10001):
		if(var==1):
			print(var)
		else:	
			prime(var)
main()		