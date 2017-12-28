#ifndef UTIL_H
#define UTIL_H

#include <stdio.h>
#include <stdlib.h>
#include <math.h>


typedef struct Key_t{
	int e, n;
	int d;
} Key;


int gdc(int x, int y);

int phi(int x, int y);

int isPrime(int x);



#endif