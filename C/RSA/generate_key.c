#include "util.h"
#include "generate_key.h"


Key *generateKeys(){
	Key *newKey = (Key *) calloc (1, sizeof(Key));

	int x, y, p, q;
	printf("Please, select 2 prime numbers:\n");
	scanf("%i %i", &x, &y);
	// Check if both numbers are primes
	if(isPrime(x) != 1 || isPrime(y) != 1){
		printf("Error: You should pick two prime numbers!\n");
		return generateKeys();
	}

	if(x == y){
		printf("Error: You should pick two different prime numbers!\n");
		return generateKeys();	
	}


	// certifies that p > q and both are coprimes 
	if(x < y){
		p = x, q = y;
	} else {
		p = y, q = x;
	}

	if(gdc(p, q) != 1){
		printf("Error: You should pick coprime numbers!\n");
		return generateKeys();
	}

	// IF the program runs till here, it's everything okay with the inputs.
	newKey->n = p*q;
	int phi_n = phi(p, q);
	// printf("phi: %i\n", phi(p, q));

	// Now, let's choose $e
	printf("Eligible numbers to be $e:\n");
	for(int i = 2; i < phi_n; i++){
		if(gdc(newKey->n, i) == 1 && gdc(phi_n, i) == 1){
			printf("- %i ", i);
		}
	}
	printf("\n\nChoose a number:\n"); // this needs to be automatic and random *

	// int e;
	scanf("%i", &newKey->e);
	newKey->d = newKey->e * phi_n * + 1; 
	printf("Key generated: (%i, %i)\n", newKey->e, newKey->n);
	// printf("Decrypt Key: (%i, %i)\n", newKey->d, newKey->n);
	// printf("")
	return(newKey);
}
