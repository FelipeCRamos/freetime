# A little program for counting the str inputs of the datasheet
import pandas as pd

def printstats(gen, br, non_br, gen_c, br_c, non_br_c):
    print("General: (%i respostas)"%(total))
    for key in gen:
        print("{:>20}: {:05.2f}%".format(key, (gen[key]/gen_c)*100).replace('.',','))

    print("Brasileiros: ({:05.2f}%)".format(br_c/gen_c*100))
    for key in br:
        print("{:>20}: {:05.2f}%".format(key, (gen[key]/gen_c)*100).replace('.',','))

    print("Estrangeiros: ({:05.2f}%)".format(non_br_c/gen_c*100))
    for key in non_br:
        print("{:>20}: {:05.2f}%".format(key, (gen[key]/gen_c)*100).replace('.',','))

    global out
    out.write("General: (%i respostas)\n"%(total))
    for key in gen:
        out.write("{:>20}: {:05.2f}%\n".format(key, (gen[key]/gen_c)*100).replace('.',','))

    out.write("\nBrasileiros: ({:05.2f}%)\n".format(br_c/gen_c*100))
    for key in br:
        out.write("{:>20}: {:05.2f}%\n".format(key, (gen[key]/gen_c)*100).replace('.',','))

    out.write("\nEstrangeiros: ({:05.2f}%)\n".format(non_br_c/gen_c*100))
    for key in non_br:
        out.write("{:>20}: {:05.2f}%\n".format(key, (gen[key]/gen_c)*100).replace('.',','))
    out.close()

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

def workOn(column):
    global data, nation_column
    global total_counter, brazillian_counter, non_brazillian_counter
    global general_stats, brazillian_stats, non_brazillian_stats
    # General
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
# read of the excel file (.xlsx)
data = pd.read_excel('analyser/natal-novembro.xlsx', sheetname='uncleaned_data')
nation_column = 'onde_o_sr_a_reside_mora_' # self-explanatory

general_stats = {'0':0, '0 até 100':0, '100 até 200':0, '200 até 300':0, '300 até 400':0, '400 até 500':0, '500 até 600':0, '600 até 700':0, '700 até 800':0, '800 até 900':0, '900 até 1000':0, '1000+':0}
brazillian_stats = {'0':0, '0 até 100':0, '100 até 200':0, '200 até 300':0, '300 até 400':0, '400 até 500':0, '500 até 600':0, '600 até 700':0, '700 até 800':0, '800 até 900':0, '900 até 1000':0, '1000+':0}
non_brazillian_stats = {'0':0, '0 até 100':0, '100 até 200':0, '200 até 300':0, '300 até 400':0, '400 até 500':0, '500 até 600':0, '600 até 700':0, '700 até 800':0, '800 até 900':0, '900 até 1000':0, '1000+':0}
total_counter, brazillian_counter, non_brazillian_counter = 0, 0, 0
out = open('statistics.txt', 'w')

# work_column = input("Please, type the column you wanna work:\n> ")
work_column = 'group_mf3ez33/Alimenta_o'

total, br, non_br = workOn(work_column)

printstats(general_stats, brazillian_stats, non_brazillian_stats, total, br, non_br)
