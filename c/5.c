// kstrikis' solution for project euler problem 5
// released under The Unlicense
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
// compile with gcc 5.c -lm -o 5
// answer will be product of primes < 20 times repeated factors (16=2*2*2*2, 9=3*3)
#include<stdio.h>
#include<math.h>
#include<stdbool.h>

bool isprime(int n, int i) {
	if (n==2) return true;
	if (i*i>n) return true;
	if (n%i==0) return false;
	return isprime(n,i+1);
}
int main(){
	int prod = 1;
	for(int x=1; x<20; x++) {
		if(isprime(x,2)) prod *= x;
	}
	printf("%d\n",prod*8*3);
}
