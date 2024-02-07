#run this program when you have completed the first two parts of the exercise
#if you have completed the first two parts correctly this will find the first four perfect nubmers

from perfectNumber import perfectNumber

totalPFs = 0
testNumber = 1
while (totalPFs <= 4):
    if (perfectNumber(testNumber)):
        print(testNumber," is a perfect number")
        totalPFs = totalPFs + 1
        testNumber = testNumber + 1
