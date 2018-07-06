#P4T2
#CTI 110
#Jessica Washington
#July 2nd, 2018

#Initialize the accumulator.
runningTotal = 0


#Collect info from user.
while runningTotal >= 0:
    print('Enter a number?')

    #Input numbers.
    n = int(input())
        
    #Add numbers together.
    runningTotal = runningTotal + n
     #Create a stopping point.
    if n < 0:
        #Add numbers together.
        runningTotal = runningTotal + -n

        print('Total:', runningTotal)

    
    

 
    
