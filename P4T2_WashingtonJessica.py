#P4T2
#CTI 110
#Jessica Washington
#July 2nd, 2018


#Initialize the accumulator.
total = 0

#Get the bugs collected for each day.
for day in range(1,8):
    #Collect info from user.
    print('Enter the bugs collected on day', day, ':')

    #Input number of bugs
    bugs = int(input())

    #Add bugs to total
    total += bugs

#Display the total bugs.
    print('You collected a total of', total, 'bugs.')
    
