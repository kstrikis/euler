// kstrikis' solution for project euler problem 3
// released under The Unlicense
// What is the largest prime factor of the number 600851475143 ?
// compile with gcc 3.c -lm -o 3
#include<stdio.h>
#include<math.h>
int main(){
	double composite = 600851475143;
	double factor = 1.0;
	double lgfactor = 1.0;
	double decimal;
	while(1){
		factor += 2.0;
		decimal = composite/factor - floor(composite/factor);
		while(decimal==0){
			composite = composite/factor;
			decimal = composite/factor - floor(composite/factor);
		}
		if(factor>composite) break;
	}
	printf("%d\n",(int)factor);
}
