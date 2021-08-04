# kstrikis' solution for project euler problem 3
# released under The Unlicense
# What is the largest prime factor of the number 600851475143 ?
import math
composite = 600851475143
factor = 1.0 # need decimal remainders
while(1):
    factor = factor + 2
    decimal = composite/factor - math.floor(composite/factor)
    while(decimal==0):
        composite = composite/factor
        decimal = composite/factor - math.floor(composite/factor)
    if factor > composite:
        break
print(factor)
