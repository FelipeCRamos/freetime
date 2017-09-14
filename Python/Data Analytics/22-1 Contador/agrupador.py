# By Felipe Ramos
import pandas as pd # PANDAS LIB
import re as r # REGULAR EXPRESSIONS

path = 'analyser/uncleaned/'
path = path + input("Selecione o nome do arquivo xlsx: (dentro da pasta uncleaned)\n> ")

def converter(cidade):
    if cidade in ['Pirangi', 'Cotovelo', 'Pium']:
        return 'Parnamirim'
    elif cidade in ['Buzios','Camurupim','Tabatinga','lagoa_do_bofim','arituba_e_carcara']:
        return 'Nisia Floresta'
    elif cidade in ['Sibaúma','Pipa','praia_do_amor','lagoa_dos_guarairas','tibau_do_sul']:
        return 'Tibau do Sul'
    elif cidade in ['barra_do_cunhau']:
        return 'Canguaretama'
    elif cidade in ['Jacumã','lagoa_de_jacuma','Muriú','porto_mirim/jacuma']:
        return 'Ceará Mirim'
    elif cidade in ['barra_do_rio','genipabu','Pirangui']:
        return 'Extremoz'
    elif cidade in ['Maracajau','Maxaranguape','cabo_de_sao_roque']:
        return 'Maxaranguape'
    elif cidade in ['Zumbi','punaú','rio_do_fogo','Punau']:
        return 'Rio do Fogo'
    elif cidade in ['baia_formosa','Sagi']:
        return 'Baía Formosa'
    else:
        return cidade+' *- Não listado *'


def percorrer_data(ncol):
    global uc_data
    uc_data[ncol].dropna(axis=0, inplace=True)
    cities, qnt_total = [], 0
    for resp in uc_data[ncol]:
        qnt_total += 1
        temp = []
        for cid in resp.split(' '):
            temp.append(converter(cid))
        for c in set(temp):
            cities.append(c)
    s_cit = set(cities)
    contagem = {}
    for cidade in cities:
        try:
            contagem[cidade] += 1
        except:
            contagem[cidade] = 1
    for cidade in contagem:
        print("\nCidade: *%s*\n%.2f%% - %i Pessoas"%(cidade, (contagem[cidade]/qnt_total)*100, contagem[cidade]))
    print("Quantidade total: %i"%(qnt_total))


# MAIN
try:
    uc_data = pd.read_excel(path)
    print("Status: File Loaded")
    percorrer_data(input("\nAgora, insira o nome da coluna a ser analisada:\n> "))

except FileNotFoundError:
    print("Não foi possivel achar o arquivo!")
