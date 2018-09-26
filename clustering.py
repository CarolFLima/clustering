from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# # Lendo do excel e gerando csv
# df_ant = pd.read_excel('data/ant.xlsx')
# df_stdif = pd.read_excel('data/stdif.xlsx')
# df_st = pd.read_excel('data/st.xlsx')
#
# VARIABLES = ['item.ncm', 'item.cfop', 'item.cst']
# df_stdif['item.cst'].fillna(0, inplace=True)
# df_ant[VARIABLES].to_csv('data/csv/ant.csv')
# df_stdif[VARIABLES].to_csv('data/csv/stdif.csv')
# df_st[VARIABLES].to_csv('data/csv/st.csv')

# Lendo do csv
df_ant = pd.read_csv('data/csv/ant.csv')
df_stdif = pd.read_csv('data/csv/stdif.csv')
df_st = pd.read_csv('data/csv/st.csv')

# Salvando o tamanho de cada dataframe
tam_ant = df_ant.shape[0]
tam_stdif = df_stdif.shape[0]
tam_st = df_st.shape[0]

# Juntando todos os dataframes em um só
frames = [df_ant, df_stdif, df_st]
df_temp = pd.concat(frames)

item_ncm = df_temp['item.ncm'].tolist()
ncm1 = []
ncm2 = []
ncm3 = []

# Quebrando o ncm em partes
for item in item_ncm:
    a1 = str(item)[0:2]
    a2 = str(item)[2:4]
    a3 = str(item)[4:8]

    if a1 == "":
        a1 = "00"
    if a2 == "":
        a2 = "00"
    if a3 == "":
        a3 = "0000"

    ncm1.append(a1)
    ncm2.append(a2)
    ncm3.append(a3)

# Classificando os clusters

d = {'ncm1': ncm1, 'ncm2': ncm2, 'ncm3': ncm3, 'cfop': df_temp['item.cfop'], 'cest': df_temp['item.cst']}
df = pd.DataFrame(data=d)
df['cest'].fillna(0, inplace=True)

print(df.head(10))
print(df_ant.head(10))

# initial_centers = []
# initial_centers.append(df.iloc[4615].tolist())
# initial_centers.append(df.iloc[442183].tolist())
# initial_centers.append(df.iloc[613207].tolist())
# print(initial_centers)

model = KMeans(n_clusters=3)#, init=np.asarray(initial_centers))

labels = model.fit_predict(df[['ncm1', 'ncm2', 'cfop']].values)

# Gerando a crosstab
varieties = []
for i in range(tam_ant):
    varieties.append("ANT")
for i in range(tam_stdif):
    varieties.append("STDIF")
for i in range(tam_st):
    varieties.append("ST")

result = pd.DataFrame({'labels': labels, 'varieties': varieties, 'ncm1': ncm1,
                       'ncm2': ncm2, 'cfop': df['cfop'], 'cest': df['cest']})

ct = pd.crosstab(result['labels'], result['varieties'])
print(ct)

# plt.scatter(result['ncm2'], result['cfop'], c=labels)
# plt.show()

