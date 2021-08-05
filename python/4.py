## kstrikis' solution for project euler problem 4
## released under The Unlicense
## Find the largest palindrome made from the product of two 3-digit numbers.
prod = 0
lgpal = 0
for x in range(100,1000):
    for y in range(100,1000):
        prod = x*y
        if(prod<lgpal):
            continue
        s = str(prod)
        if(s[0] != s[-1]):
            continue
        if(s[1] != s[-2]):
            continue
        if(s[2] != s[-3]):
            continue
        lgpal = prod
print(lgpal)
