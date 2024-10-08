# Selecione um dataset no Kaggle e trate com o pandas, e apresente cinco tipos de BI (Business Inteligence), posteriormente gere 5 gráficos do Matplotlib.
# Apresentar o Dataset e os resultados.

# https://www.kaggle.com/datasets/ahmedwaelnasef/cars-dataset/data

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Ex5\cars.csv")
print(df.info())
# Carros com preço abaixo de 5000?
# preco = (df.query('price < EGP 5000'))

# # Carros do Egito?
# brasil = (df.query('car name & country == egypt'))

# # Carros com 4 cilindros?
# cilindro = df.query('cylinder == 4')

# # Carros com 5 assentos?
# assentos = df.query('seats == 5')

# # Carros da marca Toyota?
# toyota = df.query('brand == "Toyota"')

# # # Importações

# preco.to_csv('preco.csv', sep=';', index=False, encoding='utf-8-sig')
# brasil.to_csv('brasil.csv', sep=';', index=False, encoding='utf-8-sig')
# cilindro.to_csv('cilindro.csv', sep=';', index=False, encoding='utf-8-sig')
# assentos.to_csv('assentos.csv', sep=';', index=False, encoding='utf-8-sig')

# print(df.info())


#  #   Column           Non-Null Count  Dtype
# ---  ------           --------------  -----
#  0   car name         6308 non-null   object
#  1   price            6308 non-null   object
#  2   engine_capacity  6308 non-null   object
#  3   cylinder         5684 non-null   object
#  4   horse_power      6308 non-null   object
#  5   top_speed        6308 non-null   object
#  6   seats            6308 non-null   object
#  7   brand            6308 non-null   object
#  8   country          6308 non-null   object