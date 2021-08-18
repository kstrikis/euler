## kstrikis' solution for project euler problem 10
## released under The Unlicense
## Find the sum of all the primes below two million.
#def isprime(n,i): #stack overflow when approaching 1 million
#    if(n==2):
#        return 1
#    if(n%i==0):
#        return 0
#    if(i**2>n):
#        return 1
#    return isprime(n,i+1)
import math
def isprime(n):
    if n==2:
        return 1
    if n%2==0:
        return 0
    sqrtn = math.ceil(math.sqrt(n))
    for a in range(3,sqrtn+1,2):
        if n%a==0:
            return 0
    return 1
count = 0
check = 1
while(check<2000000):
    check = check + 1
    if(isprime(check)):
        count = count + check
print(count)
