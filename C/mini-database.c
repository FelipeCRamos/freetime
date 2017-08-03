/* MADE BY: FELIPECRAMOS */

#include<stdlib.h>
#include<stdio.h>
#include<string.h>

struct pessoa{
  char nome[50]; // se  nome do meliante tiver mais de 50 caracteres, ta c a porr;
  int idade;
  int sexo;
};

struct pessoa criarPessoa(int contador){
  struct pessoa temp;
  contador += 1; // Só pra não bugar a visualização do usuário com os %i
  printf("Digite o nome da %i° pessoa: ", contador);
  scanf("%s", &temp.nome);
  printf("Digite a idade da %i° pessoa: ", contador);
  scanf("%i", &temp.idade);
  printf("Digite o sexo da %i° pessoa: (0=Masc / 1=Fem) ", contador);
  scanf("%i", &temp.sexo);
  printf("-----------------------------------------------------------\n");
  //printf("\n%i Pessoa: | Nome: %s | Idade: %i | Sexo: %i\n\n", contador, temp.nome, temp.idade, temp.sexo);
  return temp;
};
/* EM DESENVOLVIMENTO! */



int main(void){
  /* DECLARAÇÃO DE FUNÇÕES */
  struct pessoa criarPessoa(int contador); // Declaração da função | Uma função pode retornar struct (?)
  //void procurar(char nome, char *first, char *last);

  printf("Olá, seja bem vindo ao cadastro de pessoas;\n");
  printf("Quantas pessoas deseja cadastrar: ");
  int qnt_cadastro, i;
  scanf("%i", &qnt_cadastro);
  printf("-----------------------------------------------------------\n");
  struct pessoa meliante[qnt_cadastro]; // Declaração de um vetor com 'n' tamanho, para poder usar como argumento da estrutura
  for(i = 0; i < qnt_cadastro; i++){
    //criarPessoa(i);
    meliante[i] = criarPessoa(i);
  }
  // Dar print nas pessoas

  printf("Escolha o que deseja realizar agora: \n");
  printf("\n1 = Imprimir toda a lista;\n2 = Procurar um nome na lista;\nEscolha sua opção: ");
  int op;
  scanf("%i", &op);
  switch (op) {
    case 1:
      for(i=0; i<qnt_cadastro; i++){
        printf("\nInfo %s:\n- %i anos\n", meliante[i].nome, meliante[i].idade);
        if(meliante[i].sexo == 0){
          printf("- Homem\n");
        }else{
          if(meliante[i].sexo == 1){
            printf("- Molier\n");
          }else{
            printf("- Sexo indefinido\n");
          }
        }
      }
      break;
    case 2:
      /* EM DESENVOLVIMENTO! */
      printf("\nDigite um nome que deseja procurar: (exatamente o nome) \n");
      char find[50];
      scanf("%s", &find);
      for(i=0; i < qnt_cadastro; i++){
        if(strcmp(find, meliante[i].nome) == 0){
          printf("-----------------------------------------------------------\n");
          printf("\n\tCadastro puxado com sucesso!\n");
          printf("-----------------------------------------------------------\n");
          printf("Ficha de %s:\n", find);
          printf("\tNome: %s\n", meliante[i].nome);
          printf("\tIdade: %i\n", meliante[i].idade);
          if(meliante[i].sexo == 0){
            printf("\tSexo: Masculino\n");
          }else{
            if(meliante[i].sexo == 1){
              printf("\tSexo: Feminino\n");
            }else{
              printf("\tSexo: Indefinido\n");
            }
          }

          break;
        }
      }
      break;
    default:
      printf("Por favor, escolha uma opção válida.\n");
  };
// system("pause");
return 0;
}
