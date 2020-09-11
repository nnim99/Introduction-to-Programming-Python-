def main():
	for i in range(0,8):
		string=""
		if(i%2!=0):
			for j in range(i):
				string+="*"
				space=""
				for k in range((9-i)//2):
					space+=" "				
			print(space+string)
	for l in range(9,0,-1):
		string=""
		if(l%2!=0):
			for m in range(l):
				string+="*"
				space=""
				for n in range((9-l)//2):
					space+=" "				
			print(space+string)


main()
