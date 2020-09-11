import random
def main():
    print("Try Out this Game!")
    print("Guess The Number!")
    print("You have Five Tries!")
    print("Best Of Luck!")
    number01 = random.randint(1,100) #This will take a random unknown value starting from 1 to 100 
    number02 = input("Enter a number between 1 and 100: ", )
    try:
        number02 = int(number02)
        if (number02 < 1) and (number > 100): 
            raise Exception ("The value entered is not in given range!")
    except Exception as e:
        print(e)
    else:
        number = number02
    result = number - number01 #The difference between number entered and number chosen by python
    if result == 0:
        print("Your Guess is Right! You won!")
    else:
        if (result >= -15) and (result < 0) : #The number entered by user is less than the number by python and range the of difference is 15
            print("Your Guess was less than the actual value, Try Again!")
        elif (result < -15) and (result > -99) : #The number entered by the user is far less than the number by python and the range of difference continues from 15 to 99 
            print("Your Guess was far less than the actual value, Try Again!")
        elif (result < 15) and (result > 0): #The number entered by user is greater than the number by python and range the of difference is 15
            print("Your value was greater than the actual value, Try Again!")
        elif (result > 15) and (result < 99): #The number entered by the user is far greater than the number by python and the range of difference continues from 15 to 99
            print("Your value was far greater than the actual value, Try Again!")
        number03 = input("Enter a number between 1 and 100: ")
        try:
            number03 = int(number03)
            if (number03 < 1) and (number03 > 100):
                raise Exception ("The value entered is not in given range!")
        except Exception as e:
            print(e)
        else:
            number = number03
        result = number - number01  
        if result == 0:
            print("Your Guess is Right! You won!")
        else:
            if (result >= -15) and (result < 0 ):
                print("Your Guess was less than the actual value, Try Again!")
            elif (result < -15) and (result > -99) :
                print("Your Guess was far less than the actual value, Try Again!")
            elif (result < 15) and (result > 0):
                print("Your value was greater than the actual value, Try Again!")
            elif (result > 15) and (result < 99):
                print("Your value was far greater than the actual value, Try Again!")
            number04 = input("Enter a number between 1 and 100: ")
            try:
                number04 = int(number04)
                if (number04 < 1) and (number04 > 100):
                    raise Exception ("The value entered is not in given range!")
            except Exception as e:
                print(e)
            else:
                number = number04
            result = number - number01
            if result == 0:
                print("Your Guess is Right! You won!")
            else:
                if (result >= -15) and (result < 0) :
                    print("Your Guess was less than the actual value, Try Again!")
                elif (result < -15) and (result > -99) :
                    print("Your Guess was far less than the actual value, Try Again!")
                elif (result < 15) and (result > 0):
                    print("Your value was greater than the actual value, Try Again!")
                elif (result > 15) and (result < 99):
                    print("Your value was far greater than the actual value, Try Again!")
                number05 = input("Enter a number between 1 and 100: ")
                try:
                    number05 = int(number05)
                    if (number05 < 1) and (number05 > 100):
                        raise Exception ("The value entered is not in given range!")
                except Exception as e:
                    print(e)
                else:
                    number = number05
                result = number - number01
                if result == 0:
                    print("Your Guess is Right! You won!")
                else:
                    if (result >= -15) and (result < 0 ):
                        print("Your Guess was less than the actual value, Try Again!")
                    elif (result < -15) and (result > -99) :
                        print("Your Guess was far less than the actual value, Try Again!")
                    elif (result < 15) and (result > 0):
                        print("Your value was greater than the actual value, Try Again!")
                    elif (result > 15) and (result < 99):
                        print("Your value was far greater than the actual value, Try Again!")
                    number06 = input("Enter a number between 1 and 100: ")
                    try:
                        number06 = int(number06)
                        if (number06 < 1) and (number06 > 100):
                            raise Exception ("The value entered is not in given range!")
                    except Exception as e:
                        print(e)
                    else:
                        number = number06
                    result = number - number01
                    if result == 0:
                        print("Your Guess is Right! You won!")
                    else:
                        if (result >= -15) and (result < 0 ):
                            print("Your Guess was less than the actual value, Try Again!")
                        elif (result < -15) and (result > -99) :
                            print("Your Guess was far less than the actual value, Try Again!")
                        elif (result < 15) and (result > 0):
                            print("Your value was greater than the actual value, Try Again!")
                        elif (result > 15) and (result < 99):
                            print("Your value was far greater than the actual value, You lose")
    print("The right value was: ",number01)
main()
    
        
    
