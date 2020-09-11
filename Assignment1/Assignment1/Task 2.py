import math
def main():
	print("What do you want to perform? ")
	print("1. Simple multiplication, addition, subtraction or division.")
	print("2. Power based calculations.")
	print("3. Trignometric Calculations ")
	print("4. Hyperbolic Function calculations ") 
	print("5. Logrithmic with base 10 ")
	print("6. Natural Logrithmic with base e")
	print("7. Logrithm with respect to any base except e and 10")
	print("8. Calculation based on quadratic equations")
	choice = input("Select a Number for which purpose you want to use calculator? ")
        #Selecting the option
	if choice == "1":
		value1  = input("Enter value one: ")
		operator = input("Enter an operator? (+/-///x ): ")
		value2  = input("Enter a value two: ")

		#exception handling
		try:
			value1 = float(value1) or int(value1)
			value2 = float(value2) or int(value2)
		except Exception as e:
			print(e)
			value1 = 0
			value2 = 0
			print("The values taken are 0")
		else:
			value01 = value1
			value02 = value2

		if operator == "+":
			result = value01+value02
		elif operator == "-":
			result = value01-value02
		elif operator == "/":
			result == value01/value02
		elif operator == "x":
			result == value01*value02
		else:
			print("Invalid Operator! ")
		print("The answer is:",value01,operator,value02,"=" , result)

	if choice == "2":
		value1  = input("Enter value: ")
		power   = input("Enter power for that value (enter 0.5 for square root: ")
		try:
			value1 = float(value1) or int(value1)
			power  = float(power) or int(power)
		except Exception as e:
			print(e)
			value1 = 0 
			power  = 0
			print("The value taken for value is and for power is:", value1)
		else:
			value01 = value1
			power01 = power
		result = math.pow(value01,power01)
		print("The answer is:", value1, "^",power,"=", result)
	
	if choice == "3":
		angle = input("Angle is in degrees or radians?: ")
		angle = angle.lower()
		angle01 = input("Enter angle= ")

		try:
			angle01 = float(angle01) or int(angle01)
		except Exception as e:
			print(e)
			print("The value for the angle taken is: ", 0)
			angle1 = 0
		else:
			angle1 = angle01


		if angle == "degrees" or angle == "degree":
			angle02 = math.radians(angle1)
		if angle == "radians" or angle == "radian":
			angle02 = angle1

		print("Select your Operation")
		print("1. Sine ")
		print("2. Cosine")
		print("3. tangent")
		print("4. arcSine")
		print("5. arcCosine")
		print("6. arctangent")

		selection = input("Enter your choice (1/2/3/4/5/6): ")
		if selection == "1":
			result = math.sin(angle02)
			print("The sin(",angle02,")=",result )
		if selection == "2":
			result = math.cos(angle02)
			print("The cos(",angle02,")=",result )
		if selection == "3":
			result = math.tan(angle02)
			print("The tan(",angle02,")=",result )
		if selection == "4":
			result = math.asin(angle02)
			print("The arcsin(",angle02,")=",result )

		if selection == "5":
			result = math.acos(angle02)
			print("The arccos(",angle02,")=",result )
		if selection == "6":
			result = math.atan(angle02)
			print("The tan(",angle02,")=",result )

	if choice == "4":
		angle = input("Angle is in degrees or radians?: ")
		angle = angle.lower()
		angle01 = input("Enter angle= ")

		try:
			angle01 = float(angle01) or int(angle01)
		except Exception as e:
			print(e)
			print("The value for the angle taken is: 0 ")
			angle1 = 0
		else:
			angle1 = angle01


		if angle == "degrees" or angle == "degree":
			angle02 = math.radians(angle1)
		if angle == "radians" or angle == "radian":
			angle02 = angle1

		print("Select your Operation")
		print("1. Sinh ")
		print("2. Cosh")
		print("3. tanh")
		print("4. arcSinh")
		print("5. arcCosh")
		print("6. arctanh")

		selection = input("Enter your choice (1/2/3/4/5/6): ")
		if selection == "1":
			result = math.sinh(angle02)
			print("The sinh(",angle02,")=",result )
		if selection == "2":
			result = math.cosh(angle02)
			print("The cosh(",angle02,")=",result )
		if selection == "3":
			result = math.tanh(angle02)
			print("The tanh(",angle02,")=",result )
		if selection == "4":
			result = math.asinh(angle02)
			print("The arcsinh(",angle02,")=",result )

		if selection == "5":
			result = math.acosh(angle02)
			print("The arccosh(",angle02,")=",result )
		if selection == "6":
			result = math.atanh(angle02)
			print("The arctanh(",angle02,")=",result )

	if choice == "5":
		value1 = input("Enter the value you want to take log with base 10: ")
		try:
			value1 = float(value1) or int(value1)
			if value < 0 : 
				raise Exception ("The value entered is invalid")
		except Exception as e:
			print(e)
			value1 = 10
			print("The value is taken as: 10 ")
		else:
			value01 = value1
		result = math.log10(value01)
		print("The log(",value1, ")=",result)

	if choice == "6":
		value1 = input("Enter the value you want to take log with base e: ")
		try:
			value1 = float(value1) or int(value1)
			if value < 0 : 
				raise Exception ("The value entered is invalid")
		except Exception as e:
			print(e)
			value1 = math.e
			print("The value is taken as: e ")
		else:
			value01 = value1
		result = math.log(value01)
		print("The ln(",value1, ")=",result)
	if choice == "7":
		value1 = input("Enter the value you want to take log with any base except 10 and e: ")
		base = input("Enter a base number= ")

		try:
			value1 = float(value1) or int(value1)
			base = float(base) or int(base)

			if value < 0 : 
				raise Exception ("The value entered is invalid")
		except Exception as e:
			print(e)
			value1 = 10
			print("The value of number and base are taken as: 10 ")
		else:
			value01 = value1
			base01 = base
		result = math.log(base01,value01)
		print("The log(",value1, ") wrt.", base01,"=",result)
	if choice == "8":
		print("Do not take value of a=0!")
		print("")
		var1 = input("Enter the value for a= ")
		var2 = input("Enter the value for b= ")
		var3 = input("Enter the value for c= ")
		try:
			var1 = float(var1) or int(var1)
			var2 = float(var2) or int(var2)
			var3 = float(var3) or int(var3)
			if var1 == "0":
				raise Exception ("The value for a cannot be 0!")
		except Exception as e:
			print(e)
			var1 = 1
			var2 = 1
			var3 = 1
			print("The entered values were wrong! so value taken for a b and c is 1")
		else:
			var01 = var1
			var02 = var2
			var03 = var3
		discriminant= (var02**2) -4*var01*var03
		if discriminant < 0 :
			print("The roots are imaginary and unequal.")
			result01 = ((-var02) + (discriminant*-1)**0.5)/(2*var01)
			result02 = ((-var02) - (discriminant*-1)**0.5)/(2*var01)
			result03 = str(result01)
			result04 = str(result02)
			print("Roots are= ", result03+"i"+ ",", result04+"i" )
		elif discriminant == 0 :
			print("Roots are Real and equal.")
			result = (-var02) / (2*var01)
			print("The roots are:", result, result)
		else:
			print("The roots are real and unequal")
			result01 = ((-var02) + (discriminant)**0.5)/(2*var01)
			result02 = ((-var02) - (discriminant)**0.5)/(2*var01)
			print("The roots are: ", result01,result02)




main()
