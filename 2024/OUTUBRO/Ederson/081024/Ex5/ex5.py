#Selecione um dataset no Kaggle e trate com o pandas, e apresente cinco tipos de BI (Business Inteligence), posteriormente gere 5 gráficos do Matplotlib.
#Apresentar o Dataset e os resultados.
#https://www.kaggle.com/datasets/gustavomodelli/forest-fires-in-brazil

import pandas as pd
import matplotlib.pyplot as plt

df =pd.read_csv("Ex5/amazonia.csv")
print(df.info())

# ----------------   ----------------   ----------------   ----------------   ----------------  

# Incêndios ocorridos após os anos 2000:
pos_2000 = df.query('year > 2000')

# Dados das queimadas ocorridas no estado do Amazonas:
amazonas = df.query('state == "Amazonas"')

# Queimadas específicas do dia 10 de setembro de 2000:
queimadas_10_set = df.query('date == "2000-09-10"')

# Queimadas entre os anos de 2015 e 2017:
entre_anos = df.query('2015 <= year <= 2017')

# Queimadas ocorridas no mês de agosto:
agosto = df.query('month == "Agosto"')

# Queimadas que ocorreram no estado do Acre no ano de 2012:
acre_2012 = df.query('state == "Acre" and year == 2012')

# ----------------   ----------------   ----------------   ----------------   ----------------  

# # Importações
# pos_2000.to_csv('pos_2000.csv', sep=';', index=False, encoding='utf-8-sig')

# amazonas.to_csv('amazonas.csv', sep=';', index=False, encoding='utf-8-sig')

# queimadas_10_set.to_csv('queimadas_10_set.csv', sep=';', index=False, encoding='utf-8-sig')

# entre_anos.to_csv('entre_anos.csv', sep=';', index=False, encoding='utf-8-sig')

# agosto.to_csv('agosto.csv', sep=';', index=False, encoding='utf-8-sig')

# acre_2012.to_csv('acre_2012.csv', sep=';', index=False, encoding='utf-8-sig')

# ----------------   ----------------   ----------------   ----------------   ----------------  

# Gráfico 1: Incêndios ocorridos após o ano de 2000
queimadas_pos_2020 = pos_2000.groupby('state')['number'].sum().reset_index()

# Gráfico 2: Dados das queimadas ocorridas no estado do Amazonas
queimadas_amazonas = amazonas.groupby('year')['number'].sum().reset_index()

# Gráfico 3: Queimadas específicas do dia 10 de setembro de 2000
queimadas_10_set = queimadas_10_set.groupby('state')['number'].sum().reset_index()

# Gráfico 4: Queimadas entre os anos de 2015 e 2017
queimadas_entre_anos = entre_anos.groupby('year')['number'].sum().reset_index()

# Gráfico 5: Queimadas ocorridas no mês de agosto
queimadas_agosto = agosto.groupby('state')['number'].sum().reset_index()

# Gráfico 6: Queimadas que ocorreram no estado do Acre no ano de 2012
queimadas_acre_2012 = acre_2012.groupby('month')['number'].sum().reset_index()

# Criar subgráficos
fig, axs = plt.subplots(3, 2, figsize=(15, 15))

# Gráfico 1
axs[0, 0].bar(queimadas_pos_2020['state'], queimadas_pos_2020['number'], color='orange')
axs[0, 0].set_title('Queimadas Ocorridas Após o Ano de 2000')
axs[0, 0].set_xlabel('Estado')
axs[0, 0].set_ylabel('Número de Queimadas')
axs[0, 0].tick_params(axis='x', rotation=45)

# Gráfico 2
axs[0, 1].bar(queimadas_amazonas['year'], queimadas_amazonas['number'], color='green')
axs[0, 1].set_title('Queimadas no Estado do Amazonas')
axs[0, 1].set_xlabel('Ano')
axs[0, 1].set_ylabel('Número de Queimadas')
axs[0, 1].tick_params(axis='x', rotation=45)

# Gráfico 3
axs[1, 0].bar(queimadas_10_set['state'], queimadas_10_set['number'], color='red')
axs[1, 0].set_title('Queimadas em 10 de Setembro de 2000')
axs[1, 0].set_xlabel('Estado')
axs[1, 0].set_ylabel('Número de Queimadas')
axs[1, 0].tick_params(axis='x', rotation=45)

# Gráfico 4
axs[1, 1].bar(queimadas_entre_anos['year'], queimadas_entre_anos['number'], color='blue')
axs[1, 1].set_title('Queimadas entre os Anos de 2015 e 2017')
axs[1, 1].set_xlabel('Ano')
axs[1, 1].set_ylabel('Número de Queimadas')
axs[1, 1].tick_params(axis='x', rotation=45)

# Gráfico 5
axs[2, 0].bar(queimadas_agosto['state'], queimadas_agosto['number'], color='purple')
axs[2, 0].set_title('Queimadas Ocorridas no Mês de Agosto')
axs[2, 0].set_xlabel('Estado')
axs[2, 0].set_ylabel('Número de Queimadas')
axs[2, 0].tick_params(axis='x', rotation=45)

# Gráfico 6
axs[2, 1].bar(queimadas_acre_2012['month'], queimadas_acre_2012['number'], color='cyan')
axs[2, 1].set_title('Queimadas no Acre em 2012')
axs[2, 1].set_xlabel('Mês')
axs[2, 1].set_ylabel('Número de Queimadas')
axs[2, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

 #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   year    6454 non-null   int64
#  1   state   6454 non-null   object
#  2   month   6454 non-null   object
#  3   number  6454 non-null   float64
#  4   date    6454 non-null   object