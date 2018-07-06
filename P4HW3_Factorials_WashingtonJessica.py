#P4HW3 Factorial
#CTI 110
#Jessica Washington
#July 3rd, 2018


#This program will display the factorial of a number.

factorial = 1

#Collect info from user.
print ('Enter a nonnegative integer:')

#Input number.
num = int(input())

#Create the loop.
if num == 0 or num == 1:
    print ('The factorial of', num, 'is:', 1)
else:
    for n in range (1, num + 1):
       factorial = factorial * n
    print('The factorial of', num, 'is', factorial)

    


 
    
