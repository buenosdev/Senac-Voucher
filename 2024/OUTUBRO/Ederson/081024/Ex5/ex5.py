#Selecione um dataset no Kaggle e trate com o pandas, e apresente cinco tipos de BI (Business Inteligence), posteriormente gere 5 gráficos do Matplotlib.
#Apresentar o Dataset e os resultados.
#https://www.kaggle.com/datasets/ahmedwaelnasef/cars-dataset/data

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Ex5\mazonia.csv")
print(df.info())
# Engine capacidade acima de 1000

#preco = (df.query('engine_capacity > 1000'))

# # # Carros do Egito?
# egito = (df.query('car name & country == egypt'))

# # # Carros com 4 cilindros?
# cilindro = df.query('cylinder == 4')

# # # Carros com 5 assentos?
# assentos = df.query('seats == 5')

# # # Carros da marca Toyota?
# toyota = df.query('brand == "Toyota"')

# # # # Importações

# # preco.to_csv('preco.csv', sep=';', index=False, encoding='utf-8-sig')
# # egito.to_csv('egito.csv', sep=';', index=False, encoding='utf-8-sig')
# # cilindro.to_csv('cilindro.csv', sep=';', index=False, encoding='utf-8-sig')
# # assentos.to_csv('assentos.csv', sep=';', index=False, encoding='utf-8-sig')

