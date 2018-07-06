#P5T1 - Kilometer Converter
#CTI 110
#Jessica Washington
#July 5th, 2018

#This program will convert distance from km to mi

#Assign a constant
conversion_factor = 0.6214

def main():
    #Enter distance in kilometers
    km = float(input('Enter the number of kilometers:'))

    #Display the distance converted to miles
    show_miles(km)    
        

def show_miles(km):
    #Convert kilometers to miles
    miles = km * conversion_factor

    #Display miles
    print(km, 'converts to', miles, 'miles.')

main()
