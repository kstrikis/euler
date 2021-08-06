## kstrikis' solution for project euler problem 7
## released under The Unlicense
## What is the 10 001st prime number?
def isprime(n,i):
    if(n==2):
        return 1
    if(n%i==0):
        return 0
    if(i**2>n):
        return 1
    return isprime(n,i+1)
count = 0
check = 1
while(count<10001):
    check = check + 1
    if(isprime(check,2)):
        count = count + 1
print(check)
