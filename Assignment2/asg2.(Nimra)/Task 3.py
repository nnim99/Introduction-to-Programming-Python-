print('''The Program can only diagnose these diseases!
1. Headache \t 2. Cough \t 3. vomitting 
4.Fever. \t 5.chest pain ''')
def based(symptom):
	if (symptom == "1"):
		print("Take Panadol.")
	elif (symptom == "2"):
		print("Take Vicks cough syrup")
	elif (symptom == "3"):
		print("Take Dramamine")
	elif (symptom == "4"):
		print("Take Brufen")
	elif (symptom == "5"):
		print("Take Aspirin")
	else:
		print("Invalid no. enter.")

def basedOn(symptomList):
	for index in range(len(symptomList)):
		symptom01= symptomList[index]
		if symptom01=="1":
			sym2 = input("Are you experiencing blurred vision and are your eyes getting sensitive to light? Yes or No?").lower()
			if (sym2 == "yes"):
			  print("You are experiencing Migraine.")
			  print("Take ibuprofen.")
			  break
			elif sym2 == "no":
					var03 = input("Are you experiencing lose of memory? Yes or No? ").lower()
					if var03 == "yes":
			
						print("You have brain tumour!")
						print("Go for radio therapy and doctor for further tests!")
					else:
						print("You're suffering from a simple headache.")
						print("You should take Aspirin.")
						break
			break	
		elif symptom01=="2":
			sym2 = input("Do blood come up with coughing? Yes or No?").lower()
			if (sym2 == "yes"):
			  print("You might be suffering from lungs cancer!.")
			  var05 = input("Are you experiencing weight lose or appetite lose? Yes or No?").lower()
			  if var05 == "yes":
			  	var06 = input("Are you experiencing Shortness of breath? Yes or No?").lower()
			  	if var06 == "yes":
			  		print("You are probably having lungs cancer!.")
			  		print("You should go for further tests and go for chemotherapy!.")
			  	else:
			  		print("Normal cough! do gargles!")

			  break
			else:
				var07 = input("Are you having fever? Yes or No?").lower()
				if var07 == "yes":
					print("You are suffering from viral!")
					print("Take augmenton")
				else:
					print("Do gargles!")
				break
		elif symptom01 == "3":
			sym2 = input("Did the vomiting occur instantly after a meal? Yes or No?").lower()
			if (sym2 == "yes"):
			  print("You are suffering from food poison!.")
			  print("Avoid solid foods until vomiting ends.")
			elif sym2=="no":	
				var08 = input("Are you experiencing stomach ache? Yes or No?").lower()
				if var08 == "yes":
					print("You might be struggling with gastric trouble.")
					print("Drink some peppermint tea.")
				else:
					print("Your problem is not recognized!")
			break
		elif symptom01=="4":
			sym2 = input("Are you Experiencing nausea? Yes or No? ").lower()
			if (sym2 == "yes"):
			  	print("You are maybe experiencing diarrhea.")
			  	var09 = input("Are you Experiencing Abdominal cramps? Yes or No?").lower()
			  	if var09 =="yes":
			  		print("You are experiencing diarrhea.")
			  		print("bismuth subsalicylate")
			  	else:
			  		print("Take Panadol!")
			  	break
			else:
			  print("You should take Panadol.")
			  break
		elif symptom01=="5":
			sym2 = input("Are you experiencing heartburn ? Yes or No? ").lower()
			if (sym2 == "yes"):
			  print("You may have Heart Disease. ")
			  var10 = input("Do you sweat more than often? Yes or No?").lower()
			  if var10 == "yes":
			  	print("You have heart disease!")
			  	print("Take Angiotensin II.")
			  break
			else:
			  	var11 = input("Are you experiencing pain in your tummy or shoulder? Yes or No?").lower()
			  	if (var11 == "yes"):
			  		print("You have a broken rib.")
			  		print("Take paractamol to reduce pain.")
			  	else:
			  		print("Disease not identified!")
			  		break
	
def main():
  oneOrMore = input("Do you want to enter more than one symptom?Yes or No?").lower()
  if (oneOrMore == "yes"):
    symptomList = input("Enter the number for symptoms using spaces in between: ").split()
    basedOn(symptomList)
  else:
    symptom = input("Enter the number of the symptom from the above list: ")
    based(symptom)
main()