from sklearn.cluster import MiniBatchKMeans
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


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


# initial_centers = []
# initial_centers.append(df.iloc[4615].tolist())
# initial_centers.append(df.iloc[442183].tolist())
# initial_centers.append(df.iloc[613207].tolist())
# print(initial_centers)

mbkmeans = MiniBatchKMeans(n_clusters=3)

labels = mbkmeans.fit_predict(df[['ncm1', 'ncm2', 'cest', 'cfop']].values)

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






