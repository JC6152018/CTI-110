# CTI-110
# P3LAB Debugging
# Jessica Washington
# June 25th, 2018

def main():
    # This program takes a number grade and outputs a letter grade.
    # Define scores using 10-point grading scale
    A_score = float(90) 
    B_score = float(80)
    C_score = float(70)
    D_score = float(60)
    F_score = float(50)
    
    #Find letter grade
    
    
    score = float(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    else:
        if score > B_score and score != A_score:
            print('Your grade is: B')
        else:
            if score > C_score and score != B_score:
                print('Your grade is: C')
            else:
                if score > D_score and score != C_score:
                    print('Your grade is: D')
                else:
                    if score > F_score:
                        print('Your grade is: F')

# program start
main()

