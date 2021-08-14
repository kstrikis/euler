// kstrikis' solution for project euler problem 8
// released under The Unlicense
// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.
#include<stdio.h>
#include<stdbool.h>

int main(){
	for(int a=1; a<1000; a++){
		int b = 1;
		int c = 1000-(a+b);
		while(b<(1000-a)){
			if(a*a + b*b == c*c){
				printf("%d\n",a*b*c);
				return 0;
			}
		b++;
		c--;
		}	
	}
}
