#include <stdio.h>
#define N 3
int main(int argc, char const *argv[]) {
  int numeros[N] = {1768382797, 1699618913, 560034407};
  char* p;
  p = (char*) numeros;
  for (int i = 0; i < N*sizeof(int); ++i){
    printf("%c", *(p++));
  }
  return 0;
}
