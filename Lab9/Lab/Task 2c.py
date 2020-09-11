def main():
	for i in range(10):
		string=''
		space=''
		for j in range(10-i):
			string+='*'
		for k in range(i):
			space+=' '
		print(space+string)
main()