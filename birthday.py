#!/usr/bin/python

print "This will simulate the 'Birthday Problem' by generating XX random numbers between 1 and 365 (inclusively).\n"
people = int(raw_input("Please enter how many random 'people' you'd like to simulate: "))

trials = int(raw_input("Please enter how many trials you'd like to complete: "))

import random, math, decimal

matches = 0
nomatches = 0
total_trials = trials

while trials > 0:
    trials -= 1
    # Seed random with the current time, creates more "randomness" on each iteration
    random.seed()

    numbers = [random.randrange(1,366) for i in range(people)]

    #print "Here is the list of numbers: "

    #for number in numbers:
        #print number
        
    def findmatches( numbers ):
        s = set()
        ans = False
        for number in numbers:
            if numbers.count(number) > 1:
                s.add(number)
                ans = True
        return ans, s

    a,b = findmatches(numbers)
    
    if a == True:
        matches += 1

print "\nNumber of successful trials: ", matches
result = float (matches) / total_trials * 100
print "Percent of successful trials: ",result


expected =  (1 - decimal.Decimal(math.factorial(365)) / ( 365**people * math.factorial(365-people)))*100

print "Expected percent of number of successful trials:",expected

pe = abs( (expected - decimal.Decimal(result)) / decimal.Decimal(result * 100))

print "Percent of error:",pe

