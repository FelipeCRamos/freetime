#include "util.h"
#include "generate_key.h"


int main(int argc, char const *argv[])
{
	system("clear");
	printf("\nWelcome to the RSA Enc/Dec Tool\n");
	printf("\nThis program has been created by Felipe Ramos\n\n");

	Key private_key = *generateKeys();


	return 0;
}