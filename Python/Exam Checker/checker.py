# CODED BY FelipeCRamos
# FOR FREETIME

print("Welcome to the Exam Checker v1.0\n")
print("If you want the program to work perfecly, please provide the following format:\n"
"<QUESTION>-<ANSWER> (i.a.: 01-A)\n"
"* Please tell a question per line")
my_ans_path = input("Please indicate the filename of your answers: (ex: answers.txt)")
ans_path = input("Please indicate the filename of official answers: ")
quantity = int(input("Now, indicate how many questions are: "))
mgab = open(my_ans_path, 'r')
gabo = open(ans_path, 'r')
final = open('results.txt', 'w')
check = 0
errors = 0
cont = 0
mquestao = mgab.readlines()
questao_oficial = gabo.readlines()
arq = []
while cont < quantity:
    if mquestao[cont] == questao_oficial[cont]:
        check += 1
        print(mquestao[cont][:4] + "- You got it!")
        arq.append(mquestao[cont][:4] + " ## Check!\n")
    else:
        print(mquestao[cont][:4] + "- Almost! >", questao_oficial[cont][3])
        arq.append(mquestao[cont][:4] + " ## Wrong! (%s)\n" %(questao_oficial[cont][3]))
        errors += 1
    cont += 1
final.writelines(arq)
final.writelines("\nYou got %i questions and missed %i. Congrats (or no)!" %(check, errors))
final.close()
print("\n\n You got %i questions and missed %i." %(check, errors))
