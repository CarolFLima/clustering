import pandas as pd
import numpy as np

df_stdif = pd.read_csv('data/csv/stdif.csv')

item_gtin = df_stdif['item.gtin_trib'].tolist()

vec_mult = np.array([1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3])

for item in item_gtin:
    i = str(item)
    if pd.notnull(item) and len(i) == 13:
        vec_gtin = np.array([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]])
        produto_escalar = np.sum(vec_mult*vec_gtin.astype(int))
        prox_decimal = int(produto_escalar/10)*10 + 10
        resultado = prox_decimal - produto_escalar
        resultado = resultado % 10
        # print("Resultado: " + str(resultado) + "  Digito real: " + str(i[12]))

def validate_gtin():
    return True