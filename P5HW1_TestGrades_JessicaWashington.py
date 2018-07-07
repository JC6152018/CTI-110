#To gather 5 test grades,
#display letter grades for each test,
#and display the average test score.
#July 6th, 2018
#CTI-110 P5HW1 - Test Average and Grade
#Jessica Washington

#Calls the next 2 functions into play
#holds the input commands for grade collection
def main():
    g1 = int(input('Enter grade 1:'))
    g2 = int(input('Enter grade 2:'))
    g3 = int(input('Enter grade 3:'))
    g4 = int(input('Enter grade 4:'))
    g5 = int(input('Enter grade 5:'))
    determine_grade(g1)
    determine_grade(g2)
    determine_grade(g3)
    determine_grade(g5)
    determine_grade(g4)
    print()
    print('Your average score is:', calc_average(g1, g2, g3, g4, g5))

#accepts test score as an argument
#returns letter grade for score
#uses a 10 point grading scale
#letter grade string should be a,b,c,d,f
def determine_grade(n):
    if n >= 90:
        print('Your', n, 'grade is an: A')
    elif n > 80 and n != 90:
        print('Your', n, 'grade is a: B')
    elif n > 70 and n != 80:
        print('Your', n, 'grade is a: C')
    elif n > 60 and n != 70:
        print('Your', n,'grade is a: D')
    else:
        print('Your', n, 'grade is a: F')
    

#accepts five test scores as arguments
#returns the average of the scores
#calculate avg by dividing total of grades with number of grades collected
def calc_average(g1, g2, g3, g4, g5):
    #Complete formula - sum of all grades divided by number of grades
    average = (g1 + g2 + g3 + g4 + g5) / 5    
    return average  

#Start program
main()    

