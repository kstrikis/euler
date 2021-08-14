## kstrikis' solution for project euler problem 9
## released under The Unlicense
## There exists exactly one Pythagorean triplet for which a + b + c = 1000.
## Find the product abc.
a = 0
while(a < 998):
    a += 1
    b = 1
    c = 1000 - (a+b)
    while(b < (1000-a)):
        if(a*a + b*b == c*c):
            ##print(a,b,c)
            ##print(a*a,b*b,c*c)
            print(a*b*c)
            a=998 ##could refactor to use return for this nested loop
            break
        b += 1
        c -= 1
