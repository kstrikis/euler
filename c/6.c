// kstrikis' solution for project euler problem 6
// released under The Unlicense
// Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
// compile with gcc 6.c -o 6
#include<stdio.h>

int main(){
	int a = 0;
	int b = 0;
	for(int x=1; x<101; x++) {
		a += x*x;
		b += x;
	}
	b = b*b;
	printf("%d\n",b-a);
}
