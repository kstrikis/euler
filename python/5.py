## kstrikis' solution for project euler problem 4
## released under The Unlicense
## What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
## the answer will be the product of all primes less than 20 times
## any repeated factors (e.g. 16 = 2*2*2*2 and 9 = 3*3)
## for 1 to 20, these repeated factors are 2, 2, 2, and 3
def isprime(n,i):
    if(n==2):
        return 1
    if(n%i==0):
        return 0
    if(i**2>n):
        return 1
    return isprime(n,i+1)
product = 1
for x in range(20):
        if(isprime(x,2)):
            product = product*x
print(product*8*3)
