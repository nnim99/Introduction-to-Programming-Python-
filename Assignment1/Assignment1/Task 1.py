def main():
    basicPay01   = input("Enter your basic pay: ")
    age          = int(input("Enter your age: "))
    joiningDay   = input("Enter your joining Date in DD/MM/YYYY format: ")
    retirementDay= input("Enter your Retirement Date in DD/MM/YYYY format: ")
    try:
        basicPay01 = int(basicPay01)
    except Exception as e:
        print(e)
    else:
        basicPay = basicPay01
    incomeTax    = 0.05*basicPay #The income tax is 5% of the basic pay
    proTax       = 0.07*basicPay #The provincial tax is 7% of the basic pay
    payLeft      = basicPay-incomeTax-proTax #The pay left is the basic pay and difference of the sum of income tax and provincial tax
    print("The pay left after excluding taxes: ", payLeft)
   
    year01       = joiningDay[6:10] #Extracting the year from the string
    year02       = retirementDay[6:10] #Extracting the year from the string
    month01      = joiningDay[3:5] #Extrating the month from the string
    month02      = retirementDay[3:5]#Extrating the month from the string
    year01       = int(year01) #So we can use the year extracted as integer
    year02       = int(year02)
    month01      = int(month01)  #So we can use the month extracted as integer
    month02      = int(month02)

    married      = input("Are you married? Yes or No?")
    married      = married.lower()
    year         = (year02-year01)
    monthInService = (year*12)+ (month02-month01)
    print("The month in service are: ", monthInService)
    
    if married == "yes" :  
        marriageDate         = input("Enter your marriage Date in DD/MM/YY format: ")
        month03              = marriageDate[3:5] #Extracting the month from the marriageDate string
        year03               = marriageDate[6:10]#Extracting the year from the marriage Date string
        month03              = int(month03)
        year03               = int(year03) #So integers can be compared in the following program
        if year03<=year01:
            houseRent            = payLeft*0.15
            serviceAfterMarriage = ((year02-year01)*12) + ( month02-month01)
            
            print("The number of months of service after marriage: " , serviceAfterMarriage)
        elif year03>year01:
            serviceAfterMarriage = ((year02-year03)*12) + ( month02-month03)
            houseRent = payLeft*0.15 #15 percent of pay left is given to the married person
        
    else:
        houseRent = 0 #Person is not married so no house rent
        
    if age < 45:
        oldAge = 0
    elif age >= 45 and age <= 55:
        oldAge = payLeft*0.10 #10% of payleft is given if person is from 45 to 55 
    else:
        oldAge = payLeft*0.15 #15% of payleft is given if person if over 55
        
    totalPay = basicPay + oldAge + houseRent #total pay is the sum of basic pay, house ]rent and oldage
    print("Total pay is = ", totalPay)
    #Steps for caculating pension
    step1 = basicPay*2*monthInService
    step2 = houseRent*serviceAfterMarriage
    step3 = oldAge*3
    step4 =(totalPay) * 2
    step5 = step1 + step2 + step3 + step4
    print("The basic pay is doubled and multiplied with the number of months in service= " , step1)
    print("House rent is multiplied with the months in service since marriage= " , step2)
    print("Old age allowance is multiplied with 3= " , step3)
   
    print("Total Pay is multiplied with 2 = ", step4)
    print("Pension is calculated by adding above 4= " , step5)
main()
