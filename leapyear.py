"""
This program inputs a year and determines whether the input is a leap year or not.
The program uses the following logic:
A leap year is divisible by four, but not by one hundred,
unless it is divisible by four hundred.
"""
def leapyear(year):
    a = year % 4            #Determines whether the year is divisible by 4.
    if a != 0:   
        print ("False")     #If no, returns false.
    if a == 0:              #If yes, check if the year is divisible by 100.
        b = year % 100
        if b != 0:          #If the year is not divisible by 100,
            print("True")   #then the year is a leap year.
        if b == 0:          #If the year is divisible by 100,
            c = year % 400  #then the program will check if the year is divisible by 400.
            if c == 0:      #If 400 is a factor then it is a leapyear,
                print ("True")
            if c != 0:      #otherwise it is not.
                print ("False")
