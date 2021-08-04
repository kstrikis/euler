#include<stdio.h>
int main() {
	int a = 1;
	int b = 2;
	int x;
	int sum = 0;
	while(b<4000000){
		if(b%2==0) {sum+=b;}
		x = a;
		a = b;
		b = a+x;
	}
	printf("%d\n",sum);
}
