#CTI-110
#P3HW1 - Age Classifier
#Jessica Washington
#June 24, 2018

#Get the user's age
age = int(input("Enter the age:"))

#Discover age group

if age <= 1:
    print('Person is an infant')
    
if age != 1 and age <= 12:
    print('Person is a child')

if age >= 12 and age <= 19:
    print('Person is a teenager')

if age >= 20:
    print('Person is an adult')
    




        
    
