import pandas as pd 

'''
Little program created by Felipe Ramos, just to process and agroup some typed data in a research by CEFAT
'''

path = 'analyser/uncleaned/'
path = path + input("Selecione o nome do arquivo xlsx: (dentro da pasta uncleaned)\n> ")

def converter(cidade):
    if cidade in ['Pirangi', 'Cotovelo', 'Pium','pium', 'Parnamirim', 'parnamirim', 'pirangi', 'cotovelo']:
        return 'Parnamirim'
    elif cidade in ['Buzios','b_zios','Búzios','Camurupim','camurupim','Tabatinga','tabatinga','lagoa_do_bofim','arituba_e_carcara', 'nisia_floresta']:
        return 'Nisia Floresta'
    elif cidade in ['Sibaúma','Pipa','praia_do_amor','lagoa_dos_guarairas','tibau_do_sul', 'Tibau']:
        return 'Tibau do Sul'
    elif cidade in ['barra_do_cunhau', 'barra_do_cunha', 'Csnguareta', 'Barra', 'Canguaretama']:
        return 'Canguaretama'
    elif cidade in ['Jacumã','lagoa_de_jacuma','Muriú', 'Muriu', 'muri','porto_mirim/jacuma', 'porto_mirim__j','ceara_mirim']:
        return 'Ceará Mirim'
    elif cidade in ['barra_do_rio','genipabu','Genipabu','Pirangui', 'pirangui', 'pitangui', 'Pitangui', 'Extremoz', 'extremoz']:
        return 'Extremoz'
    elif cidade in ['Maracajau', 'maracajaú','maracajau','Maxaranguape','cabo_de_sao_roque']:
        return 'Maxaranguape'
    elif cidade in ['Zumbi','punaú','rio_do_fogo','Punau', 'puna']:
        return 'Rio do Fogo'
    elif cidade in ['baia_formosa','Sagi', 'sagi', 'ba_a_formosa']:
        return 'Baía Formosa'
    elif cidade in ['galinhos', 'Galinhos']:
        return 'Galinhos'
    elif cidade in ['', 'M']:
        return converter('Outros');
    else:
        return cidade+' *- Não listado *'

def percorrer_data(ncol):
    '''
    This function will run through the dataset on the ~ncol
    '''
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
    contagem = {}
    for cidade in cities:
        try:
            contagem[cidade] += 1
        except:
            contagem[cidade] = 1
    for cidade in contagem:
        print("\nCidade: *%s*\n%.2f%% - %i Pessoas"%(cidade, (contagem[cidade]/qnt_total)*100, contagem[cidade]))
    print("Quantidade total: %i"%(qnt_total))


'''
The main func that calls everything else, starts here
'''
try:
    uc_data = pd.read_excel(path)
    print("Status: File Loaded")
    percorrer_data(input("\nAgora, insira o nome da coluna a ser analisada:\n> "))

except FileNotFoundError:
    print("Não foi possivel achar o arquivo!")