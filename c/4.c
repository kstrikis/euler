// kstrikis' solution for project euler problem 4
// released under The Unlicense
// Find the largest palindrome made from the product of two 3-digit numbers.
// compile with gcc 4.c -lm -o 4
#include<stdio.h>
#include<math.h>
int main(){
	int lgpal = 0;
	int prod;
	for(int x=100; x<1000; x++){
		for(int y=100; y<1000; y++){
			//5 or 6 digit products
			prod = x*y;
			if(prod<lgpal) continue;
			int len = snprintf(NULL,0,"%d",prod); //returns length of formatted string
			char str[len];
			sprintf(str,"%d",prod);
			if(!(str[len-1]==str[0])) continue;
			if(!(str[len-2]==str[1])) continue;
			if(!(str[len-3]==str[2])) continue;
			lgpal = prod;
		}
	}
	printf("%d\n",lgpal);
}
				
