from sklearn.cluster import MiniBatchKMeans
from sklearn.cluster import KMeans
from validate import validate_gtin
from validate import transform_gtin_14
import pandas as pd
import numpy as np
import math

##### Teste dropando linhas
df_ant = pd.read_csv('data/csv/ant.csv')
df_stdif = pd.read_csv('data/csv/stdif.csv')
df_st = pd.read_csv('data/csv/st.csv')

# Salvando o tamanho de cada dataframe
tam_ant = df_ant.shape[0]
tam_stdif = df_stdif.shape[0]
tam_st = df_st.shape[0]


frames = [df_ant, df_stdif, df_st]
df_temp = pd.concat(frames)

print(df_temp.info())

############### Gerar novos dataframes
# idx = []
# for index, row in df_temp.iterrows():
#     item_gtin = row['item.gtin_trib']
#     i = str(item_gtin).replace(".", "")
#     # if validate_gtin(i):
#     #     print("Entrou aqui")
#     #     idx.append(index)
#     # else:
#     if len(i) == 14:
#         res, gtin_13 = transform_gtin_14(i)
#         if res:
#             df_temp.loc[index, 'item.gtin_trib'] = float(gtin_13)
#             idx.append(index)
#
# print(len(df_temp.loc[idx]))

# ############# Contagem do GTIN
# com8 = 0
# com12 = 0
# com13  = 0
# com14 = 0
# outros = 0
# valoresNulos = 0
# valores_gtin = df_stdif['item.gtin_trib'].value_counts()
# for valor, qtd in valores_gtin.items():
#     print(valor)
#     if not pd.isnull(valor):
#         if len(str(valor)) == 8:
#             com8 = com8 + 1
#         elif len(str(valor)) == 12:
#             com12 = com12 + 1
#         elif len(str(valor)) == 13:
#             com13 = com13 + 1
#         elif len(str(valor)) == 14:
#             com14 = com14 + 1
#         else:
#             outros = outros + 1
#     else:
#         valoresNulos = valoresNulos+1
#
# print("Com 8: " + str(com8))
# print("Com 12: " + str(com12))
# print("Com 13: " + str(com13))
# print("Com 14: " + str(com14))
# print("Outros: " + str(outros))
# print("Valores nulos: " + str(valoresNulos))

############# Contagem do CEST
# notnull = 0
# null = 0
# for index, item in df_ant['item.cst'].items():
#
#     if not pd.isnull(item):
#         notnull = notnull + 1
#     else :
#         null = null + 1
# print("Valor não-nulo: "+str(notnull))
# print("Valor nulo: "+str(null))

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

