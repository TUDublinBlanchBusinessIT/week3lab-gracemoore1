#grace moore
#7th feb 2024
#divisors.py
#week 3 notes for programming
#if you use number 20 it should return [1,2,4,5,10] -> number needs to be a perfect number ie. all factors of number add up to initial number

#define function header called divisors expecting one arguement
def divisors(num):
    #set up an empty list to hold result
    myList = []
    #loop from 1 to the number you are checking (take care not to include itself ie if num is 20 dont include 20 in factors}
    for i in range(1,num):
        if num % i == 0:#if 20%3 answer is 2 because remainder is 2, if you do 20%5 answer is 0 because there is no remainder-thats how we identify if it is perfect number, 0 = perf number
            myList.append(i) 
            
    return myList

print(divisors(6))
    
