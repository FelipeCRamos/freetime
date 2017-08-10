# Made by FelipeCRamos
# V1.0

import csv
file = csv.reader(open('legislators.csv'))
legislators = list(file)
genders_all = [legislator[3] for legislator in legislators] # [3] is the position of the gender information
set_genders = list(set(genders_all))
dic_genders = {}
for gender_c in set_genders:
    dic_genders[gender_c] = 0
for gender in genders_all:
    dic_genders[gender] += 1
dic_genders['Undefined'] = dic_genders['']
del(dic_genders[''], dic_genders['gender'])
print(dic_genders)
