#This function will convert feet to inches
#July 5th, 2018
#CTI-110 P5T2_FeetToInches
#Jessica Washington


#Assign how many inches are in a foot
inches_per_foot = 12

#main function
def main():
    #Get number of feet
    feet = int(input('Enter number of feet:'))

    #Convert input to inches
    print(feet, 'feet equals', feet_to_inches(feet), 'inches.')




#Feet to inch conversion using feet_to_inches function
def feet_to_inches(feet):
    return feet * inches_per_foot

main()
