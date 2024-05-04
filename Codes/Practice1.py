#Imani Hollie 01.31.2024
#This program will collect a student's grades

#Input---------------------------------------------------------------------------------------------
test1 = float(input('Enter score for Test 1: '))
test2 = float(input('Enter score for Test 2: '))
test3 = float(input('Enter score for Test 3: '))

#Calculations--------------------------------------------------------------------------------------
average = (test1 + test2 + test3) / 3.0

#Output--------------------------------------------------------------------------------------------
# If the average is 95 or greater (>= 95), congratulate the user
print('The average score is:', average)
if average >= 95:
    print('Congratulations! That\'s a great average!')