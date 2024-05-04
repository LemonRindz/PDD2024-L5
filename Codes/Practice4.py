#Imani Hollie 01.31.2024
#This program will compare grades

#Input---------------------------------------------------------------------------------------------
test1 = float(input('Enter score for Test 1: '))
test2 = float(input('Enter score for Test 2: '))
test3 = float(input('Enter score for Test 3: '))

#Calculations--------------------------------------------------------------------------------------
testAvg = (test1 + test2 + test3) / 3.0

#Output--------------------------------------------------------------------------------------------
if testAvg <= 69:
    print('F: Failing')
elif testAvg <= 70:
    print('C: Passing')
elif testAvg <= 80:
    print('B: Passing')
elif testAvg <= 90:
    print('A: Passing')
else:
    print('100% Average')