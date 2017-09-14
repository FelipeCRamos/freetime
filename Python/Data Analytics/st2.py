import pandas as pd
# import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np

# Implemented with Pandas and matplotlib!

quest = pd.read_excel('qts12.xlsx')

columns = quest.columns.tolist()

for index,item in enumerate(columns):
    print("{:>3} -> {:.40}..".format(index, item))

# print(quest.columns.tolist())

select_col = int(input("\nDigite a coluna desejada: "))
select_col = columns[select_col]
print("Your selected column was: {}".format(select_col))

print("Let's show now the counter.")
graphic = quest[select_col].value_counts(normalize=True)
array = np.array(graphic)
graphic.plot(kind='bar', antialiased=True)
plt.show()



# columns_names = quest.columns.tolist()
# rows = quest.shape[0]
# cont_gringo = 0
# quest.count()

# p.plot(range(10), range(10))
# p.show()
