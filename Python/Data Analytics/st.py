import csv


''' Contador Geral '''
def counter(element, list_of_elements): # counter(elemento, lista_geral)
    counter = 0
    for el in list_of_elements:
        if element == el:
            counter += 1
    return counter

''' Fuckin Logic bitch '''
def cont_geral(i_cont, special=0, special2=0, qnt_cont={}, s_cont=None):
    '''
    Função para chamar contador geral
    '''
    global arq

    qnt_cont, s_cont, cont, n_r = {}, None, [], 0

    global arquivo

    for pessoa in arquivo[1:]:
        if pessoa[6] == '':
            pass
        else:
            if (i_cont >= special) and (i_cont <= special2):
                if pessoa[i_cont] == '':
                    pessoa[i_cont] = '?'
            if pessoa[i_cont] != '' and pessoa[i_cont] != 'n/a':
                cont.append(pessoa[i_cont])
                s_cont = set(cont)
            else:
                n_r += 1
    try:
        for pessoa in s_cont:
            qnt_cont[pessoa] = counter(pessoa, cont)
    except TypeError:
        pass # ignore the TypeError

    print('-'*50 + '\n' + "{:^25}".format(arquivo[0][i_cont]) + '\n' + '-'*50)
    arq.write('"' + str(arquivo[0][i_cont]) + '","PERCENTUAL"\n')

    for data in qnt_cont:
        # print(str(data) + ':' + str(qnt_cont[data]) + '{:>.2f}% ({}/{})'.format((qnt_cont[data]/len(cont))*100, qnt_cont[data], len(cont)))
        print('{:>18.17s}:{:.>4}{:.>10.2f}%  ({}/{})'.format(data, qnt_cont[data], (qnt_cont[data]/len(cont))*100, qnt_cont[data], len(cont)))
        arq.write('"{}"'.format(data) + ',"%.2f"\n'%((qnt_cont[data]/len(cont))*100))

    if n_r == 0 or len(cont) == 0:
        arq.write('\n\n')
    elif n_r/len(cont) < 1:
        print('{:>18.17s}:{:.>4}{:.>10.2f}%  ({}/{})'.format('Não responderam', n_r, (n_r/len(cont))*100, n_r, len(cont)))
        arq.write('"Não Respondidos", "%.2f","%i"\n\n'%((n_r/len(cont))*100, n_r))
    else:
        arq.write('"",""\n\n')
    print('-'*50 +  '\n{:->19} {:-<30}\n'.format("Total:",len(cont))+'-'*50)




''' Main Func '''
print("Digite o nome do arquivo que deseja abrir: ")
filename = input()
# print("Agora, digite o nome do arquivo que deseja salvar: ")
salvepath = filename[:-4] + '_processado.csv'
print("Save path:", salvepath)

# filename = 'qts12-07.csv'
# from graphics import *
arq = open(salvepath, 'w')
with open(filename, newline='') as file:
    delim = input("Insira o delimitador:\n>> ")

    arquivo = list(csv.reader(file, delimiter=delim))
    cabecario = arquivo[0]
    for x, nome in enumerate(arquivo[0]):
        print('{}: {}'.format(x, nome))

    print('Total:', len(arquivo[0]))
    inicio, fim = map(int, input("Digite o primeiro elemento e depois o final:\n>> ").split())
    special, special2 = map(int, input("Digite o inicio e fim do periodo especial: (Caso não tenha, digite '0 0')\n>> ").split())
    # cont_nacio()
    # print('\nBrasileiros: {} | Estrangeiros: {}\n'.format(br, est))
    # print('### Estrangeiros: ')
    # cont_pais_est()
    # for pais in s_op:
    #     print("~ {}: {}" .format(pais, qnt_pais[str(pais)]))
    print('\n')
    # cont_estado()
    # cont_sexo()
    # cont_fe()
    # win = GraphWin('My Window', 700, 700)

    # inicio, fim = 3, 127
    for i in range(inicio, fim):
        cont_geral(i,special, special2)
        print()
    arq.close()
    # win.getMouse()
    # win.close()
