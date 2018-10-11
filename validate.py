import pandas as pd
import numpy as np

df_ant = pd.read_csv('data/csv/ant.csv')
df_stdif = pd.read_csv('data/csv/stdif.csv')
df_st = pd.read_csv('data/csv/st.csv')

item_gtin = df_stdif['item.gtin_trib'].tolist()


def validate_gtin(i):
    vec_mult = np.array([1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3])
    if len(i) == 13:
        vec_gtin = np.array([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]])
        produto_escalar = np.sum(vec_mult * vec_gtin.astype(int))
        prox_decimal = int(produto_escalar / 10) * 10 + 10
        resultado = prox_decimal - produto_escalar
        resultado = resultado % 10
        # print("Resultado: " + str(resultado) + "  Digito real: " + str(i[12]))
        print("Valido?")
        if str(resultado) == i[12]:
            return True
    return False


def transform_gtin_14(i):
    vec_mult = np.array([1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3])
    if len(i) == 14:
        gtin_13 = np.array([i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12]])
        produto_escalar = np.sum(vec_mult * gtin_13.astype(int))
        prox_decimal = int(produto_escalar / 10) * 10 + 10
        resultado = prox_decimal - produto_escalar
        resultado = resultado % 10
        gtin_13 = np.append(gtin_13, resultado)
        return True, ''.join(gtin_13)
    else:
        return False, ''


for item in item_gtin:
    i = str(item).replace(".", "")
    if pd.notnull(item) and len(i) == 14:
        transform_gtin_14(item)






