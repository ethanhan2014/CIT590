#Student Name: Ziyi Han
#Course ID: CIT 590
#Due: Jan. 30th,2015
#Homework #2
#GOAL: In this assignment we will use several number theoretic denitions and learn
#to write functions to check whether a number from 1 to 10000 satises those
#properties. The main goal of this assignment is to write modular code -
#code with a lot of small functions and a high amount of code reuse.

import math

def isPrime(x):
    '''This function returns whether or not the given number x is prime.'''
    if x == 1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

def isComposite(x):
    '''This function returns whether or not the given number x is composite.'''
    if x == 1:
        return False
    
    return not isPrime(x)

def isPerfect(x):
    '''This function returns whether or not the given number x is perfect.'''
    if isComposite(x):
        sum = 1;
        for i in range(2,int(x/2)+1):
            if x%i == 0:
                sum +=i
        return sum == x

    else:
        return False

def isAbundant(x):
    '''This function returns whether or not the given number x is abundant.'''
    if isComposite(x):
        sum = 1;
        for i in range(2,int(x/2)+1):
            if x%i == 0:
                sum += i
        return sum > x

    else:
        return False

def isTriangular(x):
    '''This function returns whether or not the given number x is triangular.'''
    return (math.sqrt(8*x+1)-1)%2==0
    

def isPentagonal(x):
    '''This function returns whether or not the given number x is pentagonal.'''
    return (1+math.sqrt(1+24*x))%6 ==0
    
def isHexagonal(x):
    '''This function returns whether or not the given number x is Hexagonal.'''
    return (1+math.sqrt(1+8*x))%4== 0

def isInt(x):
    '''This function returns whether or not the given number x is an integer number'''
    return x == int(x)

def result(boolean,nameString):
    '''This function returns result as a string'''
    if boolean:
        return "is "+nameString
    else:
        return "is not "+nameString

def main():
    '''This is main function with different functions'''

    x = input("----Please enter an integer number from 1 to 10000 or enter -1 to exit----: "); #input a value

    while not (x == -1):   #determine whether or not exit the game

        if x>1 and x<=10001 and isInt(x):   #determine whether or not the input number is legal

            # get the results 
            ans1 = result(isPrime(x),"prime")
            ans2 = result(isComposite(x),"composite")
            ans3 = result(isPerfect(x),"perfect")
            ans4 = result(isAbundant(x),"abundant")
            ans5 = result(isTriangular(x),"triangular")
            ans6 = result(isPentagonal(x),"pentagonal")
            ans7 = result(isHexagonal(x),"hexagonal")

            print "\n",x,ans1,",",ans2,",",ans3,",",ans4,",",ans5,",",ans6,",",ans7,".\n"  #print the results
            
        else:
            print "\n----Error! Please re-enter your number!----\n" #Error message
        
        x = input("----Please enter an integer number from 1 to 10000 or enter -1 to quit----: ");

    print "\n----THANK YOU----\n" #End
    

if __name__== "__main__":
    main();
