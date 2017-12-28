#include "util.h"

int gdc(int x, int y){
	if (y == 0)	return(x);
	else return(gdc(y, x % y));
}

int phi(int x, int y){
	return((x-1)*(y-1));
}

int isPrime(int x){
	if(x == 1 || x == 2) return 1;
	if(x % (int) sqrt(x) == 0){
		return 0;
	}
	for(int i = 2; i < sqrt(x); i++){
		if(x % i == 0) return 0; 
	}
	return 1;
}