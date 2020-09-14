#Yasoob Ali
#Section 8
#500953533
#2019.10.01
#A function that will take the user's inputted % grade and
#convert to a letter grade

letter = 'F'

def ryerson_grade_calculator(i):
    if (i < 50 and i >= 40):
        letter = 'F'
    elif (i >= 50 and i <= 52):
        letter = 'D-'
    elif (i >= 53 and i <= 56):
        letter = 'D'
    elif (i >= 57 and i <= 59):
        letter = 'D+'
    elif (i >= 60 and i <= 62):
        letter = 'C-'
    elif (i >= 63 and i <= 66):
        letter = 'C'
    elif (i >= 67 and i <= 69):
        letter = 'C+'
    elif (i >= 70 and i <= 72):
        letter = 'B-'
    elif (i >= 73 and i <= 76):
        letter = 'B'
    elif (i >= 77 and i <= 79):
        letter = 'B+'
    elif (i >= 80 and i <= 84):
        letter = 'A-'
    elif (i >= 85 and i <= 89):
        letter = 'A'
    elif (i >= 90 and i <= 100):
        letter = 'A+'
    else :
        letter = 'N/A'
    return letter

for n in range (40, 101, 1):
    print('grade for', n, 'is', ryerson_grade_calculator(n))
    
