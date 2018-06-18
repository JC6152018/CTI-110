# CTI-110
# P2HW2 - Tip Tax Total
# Jessica Washington
# June 17th, 2018

#Get the total food charge

foodCost = float(input( 'What is the total food cost? '))

#Calculate the tip
tipAmount = foodCost * .18
print ('The total tip will be: $',(format(tipAmount,'.2f')))

#Calculate the total tax

salesTax = foodCost * .07
print ('The total tax will be: $',(format(salesTax,'.2f')))

#Calculate the total bill

totalCost = foodCost + tipAmount + salesTax
print ('The total bill will be: $',(format(totalCost,'.2f')))




