# kstrikis' solution for project euler problem 3
# released under The Unlicense
# What is the largest prime factor of the number 600851475143 ?
import math
composite = 600851475143
factor = 1.0 # need decimal remainders
lgfactor = 1
while(1):
    factor = factor + 2
    remainder = composite/factor - math.floor(composite/factor)
    if remainder == 0:
        if factor > lgfactor:
            lgfactor = factor
        composite = composite/factor
    if factor > composite:
        break
print(lgfactor)
