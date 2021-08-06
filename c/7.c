// kstrikis' solution for project euler problem 7
// released under The Unlicense
// What is the 10 001st prime number?
// compile with gcc 7.c -o 7
#include<stdio.h>
#include<stdbool.h>

bool isprime(int n, int i) {
	if (n==2) return true;
	if (i*i>n) return true;
	if (n%i==0) return false;
	return isprime(n,i+1);
}
int main(){
	int n = 1; //number checked
	int x=0; //prime count
	while(x<10001) {
		n++;
		if(isprime(n,2)) x++;
	}
	printf("%d\n",n);
}
