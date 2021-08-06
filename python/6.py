## kstrikis' solution for project euler problem 6
## released under The Unlicense
## Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
squares = 0
sumssquared = 0
for x in range(1,101):
    squares = squares + x*x
    sumssquared = sumssquared + x
sumssquared = sumssquared * sumssquared
print(sumssquared-squares)
