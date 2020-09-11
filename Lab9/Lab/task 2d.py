def main():
	for i in range(10,0,-1):
		string=''
		space=''
		for j in range(11-i):
			string+='*'
		for k in range(i-1):
			space+=' '
		print(space+string)
main()