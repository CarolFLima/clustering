from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

##### Teste dropando linhas
# Lendo do csv
df_ant = pd.read_csv('data/csv/ant.csv')
df_stdif = pd.read_csv('data/csv/stdif.csv')
df_st = pd.read_csv('data/csv/st.csv')

# Salvando o tamanho de cada dataframe
tam_ant = df_ant.shape[0]
tam_stdif = df_stdif.shape[0]
tam_st = df_st.shape[0]

frames = [df_ant, df_stdif, df_st]
df_temp = pd.concat(frames)

print(len(df_temp['codificacao']))
for i, row in df_temp.iterrows():
    if math.isnan(row['item.cst']):
        df_temp.drop(i, axis=0, inplace=True)

df_temp.to_csv('data/cest/data.csv')
print(len(df_temp['codificacao']))

# col = ['string.mva_valor', 'string.mva_tipo', 'string.aliquota_icms',
#        'string.aliquota_fecoep', 'string.aliq_ie', 'string.tipo_imposto']
#
# ################################ PREP STDIF
# df_stdif = pd.read_excel('data/stdif.xlsx')
# stdif = []
# for index, row in df_stdif.iterrows():
#     a = row['string.aliquota_icms']
#     b = row['string.aliquota_fecoep']
#     c = (a + b/10)*1000
#     str_aliq_icms_fecoep = str(round(c))
#
#     aliq_ie = row['string.aliq_ie']
#     str_aliq_ie = str(round(aliq_ie*100)).zfill(2)
#
#     # mva_valor = row['string.mva_valor']
#     # str_mva = str(('%.4f' % (mva_valor,))).replace(".", "")
#     # str_mva_tipo = row['string.mva_tipo'][0]
#     # string_cod = str(row['string.tipo_imposto']) + ' MVA ' + str_mva + ' ' + str_aliq_icms_fecoep \
#     #              + ' ' + str_mva_tipo + ' ' + str_aliq_ie
#     string_cod = str(row['string.tipo_imposto']) + ' ' + str_aliq_icms_fecoep \
#                  + ' ' + str_aliq_ie
#     stdif.append(string_cod)
#
# df_stdif['codificacao'] = stdif
# print(df_stdif['codificacao'].unique())
# df_stdif.to_csv('data/csv/stdif.csv')
#
# ################################ PREP ST
# df_st = pd.read_excel('data/st.xlsx')
# st = []
# for index, row in df_st.iterrows():
#     a = row['string.aliquota_icms']
#     b = row['string.aliquota_fecoep']
#     c = (a + b/10)*1000
#     str_aliq_icms_fecoep = str(round(c))
#
#     aliq_ie = row['string.aliq_ie']
#     str_aliq_ie = str(round(aliq_ie*100)).zfill(2)
#
#     # mva_valor = row['string.mva_valor']
#     # str_mva = str(('%.4f' % (mva_valor,))).replace(".", "")
#     # str_mva_tipo = row['string.mva_tipo'][0]
#     # string_cod = str(row['string.tipo_imposto']) + ' MVA ' + str_mva + ' ' + str_aliq_icms_fecoep \
#     #              + ' ' + str_mva_tipo + ' ' + str_aliq_ie
#     string_cod = str(row['string.tipo_imposto']) + ' ' + str_aliq_icms_fecoep \
#                  + ' ' + str_aliq_ie
#     st.append(string_cod)
#
# df_st['codificacao'] = st
# print(df_st['codificacao'].unique())
# df_st.to_csv('data/csv/st.csv')
#
# ################################ PREP DO AT
# df_ant = pd.read_excel('data/ant.xlsx')
# ant = []
# for index, row in df_ant.iterrows():
#     a = row['string.aliquota_icms']
#     b = row['string.aliquota_fecoep']
#     c = (a + b/10)*1000
#     str_aliq_icms_fecoep = str(round(c))
#
#     aliq_ie = row['string.aliq_ie']
#     str_aliq_ie = str(round(aliq_ie*100)).zfill(2)
#
#     string_cod = str(row['string.tipo_imposto']) + ' ' + str_aliq_icms_fecoep \
#                  + ' ' + str_aliq_ie
#     ant.append(string_cod)
#
# df_ant['codificacao'] = ant
# print(df_ant['codificacao'].unique())
# df_ant.to_csv('data/csv/ant.csv')

