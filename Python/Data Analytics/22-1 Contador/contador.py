# A little program for counting the str inputs of the datasheet
import pandas as pd
import os
def process(filepath):
    def printstats(gen, br, non_br, gen_c, br_c, non_br_c):
        global output_file
        ''' CONSOLE PRINTING
        print("General: (%i respostas)"%(gen_c))
        for key in gen:
            print("{:>20}: {:05.2f}%".format(key, (gen[key]/gen_c)*100).replace('.',','))

        print("Brasileiros: ({:05.2f}%)".format(br_c/gen_c*100))
        for key in br:
            print("{:>20}: {:05.2f}%".format(key, (gen[key]/gen_c)*100).replace('.',','))

        print("Estrangeiros: ({:05.2f}%)".format(non_br_c/gen_c*100))
        for key in non_br:
            print("{:>20}: {:05.2f}%".format(key, (gen[key]/gen_c)*100).replace('.',','))
        '''
        output_file.write("General:;(%i respostas)\n"%(gen_c))
        for key in gen:
            output_file.write("{};{:05.2f}%\n".format(key, (gen[key]/gen_c)*100).replace('.',','))

        output_file.write("\nBrasileiros:;({:05.2f}%)\n".format(br_c/gen_c*100))
        for key in br:
            output_file.write("{};{:05.2f}%\n".format(key, (br[key]/br_c)*100).replace('.',','))

        output_file.write("\nEstrangeiros:;({:05.2f}%)\n".format(non_br_c/gen_c*100))
        for key in non_br:
            output_file.write("{};{:05.2f}%\n".format(key, (non_br[key]/non_br_c)*100).replace('.',','))
        output_file.close()

    def add(t, title):
        global general_stats, brazillian_stats, non_brazillian_stats
        try:
            if(t == 0):                     # general
                general_stats[title] += 1
            elif(t == 1):                   # brazillian
                brazillian_stats[title] += 1
            else:                           # non_brazillian
                non_brazillian_stats[title] += 1
        except:
            if(t == 0): # general
                general_stats[title] = 1
            elif(t == 1): # br
                brazillian_stats[title] = 1
            else: # non_br
                non_brazillian_stats[title] = 1

    def getNumbers(value, t): # This function makes the statistics of a column float64
        global data
        global general_stats, brazillian_stats, non_brazillian_stats
        if(value == 0):
            add(t, '0')
        elif(value > 0 and value <= 100):
            add(t, '0 até 100')
        elif(value > 100 and value <= 200):
            add(t, '100 até 200')
        elif(value > 200 and value <= 300):
            add(t, '200 até 300')
        elif(value > 300 and value <= 400):
            add(t, '300 até 400')
        elif(value > 400 and value <= 500):
            add(t, '400 até 500')
        elif(value > 500 and value <= 600):
            add(t, '500 até 600')
        elif(value > 600 and value <= 700):
            add(t, '600 até 700')
        elif(value > 700 and value <= 800):
            add(t, '700 até 800')
        elif(value > 800 and value <= 900):
            add(t, '800 até 900')
        elif(value > 900 and value <= 1000):
            add(t, '900 até 1000')
        elif(value > 1000):
            add(t, '1000+')

    def getNumbers_2(value, t): # second parameter of the same function
        global data
        global general_stats, brazillian_stats, non_brazillian_stats
        if(value == 0):
            add(t, '0')
        elif(value > 0 and value <= 500):
            add(t, '0 até 500')
        elif(value > 500 and value <= 1000):
            add(t, '500 até 1000')
        elif(value > 1000 and value <= 1500):
            add(t, '1000 até 1500')
        elif(value > 1500 and value <= 2000):
            add(t, '1500 até 2000')
        elif(value > 2000 and value <= 2500):
            add(t, '2000 até 2500')
        elif(value > 2500 and value <= 3000):
            add(t, '2500 até 3000')
        elif(value > 3000):
            add(t, '3000+')

    def getNumbers_3(value, t): # second parameter of the same function
        global data
        global general_stats, brazillian_stats, non_brazillian_stats
        if(value == 0):
            add(t, '0')
        elif(value > 0 and value <= 100):
            add(t, '0 até 100')
        elif(value > 100 and value <= 200):
            add(t, '100 até 200')
        elif(value > 200 and value <= 300):
            add(t, '200 até 300')
        elif(value > 300 and value <= 400):
            add(t, '300 até 400')
        elif(value > 400 and value <= 500):
            add(t, '400 até 500')
        elif(value > 500 and value <= 1000):
            add(t, '500 até 1000')
        elif(value > 1000):
            add(t, '1000+')

    def workOn(column, cat):
        global data, nation_column
        global total_counter, brazillian_counter, non_brazillian_counter
        global general_stats, brazillian_stats, non_brazillian_stats
        # General
        if(cat == 1):
            for row, nation in zip(data[column], data[nation_column]):
                if (pd.isnull(row) == False): # With this, the program will function only on valid row's (non-NaNs)
                    total_counter += 1
                    getNumbers(row, 0)
                    # Brazillian
                    if(nation == 'AUTOMATIC'): # 'AUTOMATIC' mean's it's a brazillian
                        brazillian_counter += 1
                        getNumbers(row, 1)

                    else: # Non-Brazillian
                        non_brazillian_counter += 1
                        getNumbers(row, 2)

            print("Total: %i" %(total_counter))
            return total_counter, brazillian_counter, non_brazillian_counter
        elif(cat == 2):
            for row, nation in zip(data[column], data[nation_column]):
                if (pd.isnull(row) == False): # With this, the program will function only on valid row's (non-NaNs)
                    total_counter += 1
                    getNumbers_2(row, 0)
                    # Brazillian
                    if(nation == 'AUTOMATIC'): # 'AUTOMATIC' mean's it's a brazillian
                        brazillian_counter += 1
                        getNumbers_2(row, 1)

                    else: # Non-Brazillian
                        non_brazillian_counter += 1
                        getNumbers_2(row, 2)

            print("Total: %i" %(total_counter))
            return total_counter, brazillian_counter, non_brazillian_counter
        elif(cat == 3):
            for row, nation in zip(data[column], data[nation_column]):
                if (pd.isnull(row) == False): # With this, the program will function only on valid row's (non-NaNs)
                    total_counter += 1
                    getNumbers_3(row, 0)
                    # Brazillian
                    if(nation == 'AUTOMATIC'): # 'AUTOMATIC' mean's it's a brazillian
                        brazillian_counter += 1
                        getNumbers_3(row, 1)

                    else: # Non-Brazillian
                        non_brazillian_counter += 1
                        getNumbers_3(row, 2)

            print("Total: %i" %(total_counter))
            return total_counter, brazillian_counter, non_brazillian_counter

    # data = pd.read_excel('analyser/natal-novembro.xlsx', sheetname='uncleaned_data')
    # nation_column = 'onde_o_sr_a_reside_mora_' # self-explanatory
    ''' process(filepath)'''
    ''' NEW FUNC '''
    city = filepath.split('/')[1][:-5]
    print('## Processamento de '+city+' iniciado.\n\n')
        # read of the excel file (.xlsx)
    global data, nation_column, general_stats, brazillian_stats, non_brazillian_stats, total_counter, brazillian_counter, non_brazillian_counter, output_file
    data = pd.read_excel(filepath, sheetname='uncleaned_data')
    nation_column = 'onde_o_sr_a_reside_mora_' # self explanatory
    d_p = 'group_mf3ez33/'
    work_columns = {'Hospedagem':2,
                    'Alimenta_o':1,
                    'Transporte':3,
                    'Passeios_e_lazer':3,
                    'Compras':3,
                    'Outros':3} # These are the columns that we'll be working on
    for label in work_columns:
        # reset variables
        general_stats, brazillian_stats, non_brazillian_stats = {}, {}, {}
        total_counter, brazillian_counter, non_brazillian_counter = 0, 0, 0
        try:
            output_file = open('resultados-'+city+'/'+label+'-output.csv','w')
        except:
            os.system('mkdir resultados-'+city)#-city
            output_file = open('resultados-'+city+'/'+label+'-output.csv','w')
        # when real work is done
        print("Processando coluna {}...".format(label))
        total, br, non_br = workOn(d_p+label, work_columns[label]) # generate the statistics
        printstats(general_stats, brazillian_stats, non_brazillian_stats, total, br, non_br) # print the statistics
        print("Processado.\n")
''' root scope '''
data, nation_column = 0, 0
general_stats, brazillian_stats, non_brazillian_stats = {}, {}, {}
total_counter, brazillian_counter, non_brazillian_counter = 0, 0, 0
output_file = 0

files = os.listdir('analyser')
# print(files)
for filename in files:
    # print(filename[:-5])
    if(filename[-5:] == '.xlsx'):
        process('analyser/'+filename)
# out = open('statistics.txt', 'w')
# try:
#     work_column = input("Please, type the column you wanna work:\n> ")
#     # work_column = 'group_mf3ez33/Alimenta_o'
#     total, br, non_br = workOn(work_column)
#     printstats(general_stats, brazillian_stats, non_brazillian_stats, total, br, non_br)
# except FileNotFoundError:
#     print("Arquivo não localizado, tente novamente.")

'''
group_mf3ez33/Hospedagem
group_mf3ez33/Alimenta_o
group_mf3ez33/Transporte
group_mf3ez33/Passeios_e_lazer
group_mf3ez33/Compras
group_mf3ez33/Outros
'''
