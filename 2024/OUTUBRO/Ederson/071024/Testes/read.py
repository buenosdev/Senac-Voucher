import pandas as pd 
import matplotlib.pyplot as plt

## ATIVIDADE TESTE

# print (pd.__version__)
# df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
# print(df.info())
# df.set_index('PassengerId',inplace=True)
# print(df.loc[1])
# print(df.loc[[1,2],['Name','Sex','Age']])
# print(df.loc[10:20])
# print(df.loc[10:30:2])
# print(df.loc[1:10,['Name','Sex','Age']])
# print(df.query('Age > 20').head())
# print(df.query('Age>20'))
# df.query('Age>20 &Sex=="male"').head()
# df.to_csv('dataset.csv',sep=';',index= False, encoding='utf-8-sig')

## TITULO EIXO X E Y

# a = (1,2,3,4,5)
# b = (1,2,3,4,5)
# plt.plot(a,b)

# plt.ylabel(u'Alguns Números y')

# plt.xlabel(u'Alguns Números x')

# plt.show()


# TITULO DO GRÁFICO

x = (1,2,3,4,5)
y = (1,2,3,4,5)
plt.xlabel('EixoX')
plt.xlabel('Eixo Y')

plt.title('Meu Gráfico')

plt.plot((1,2,3,4), (1,4,9,16), "mD:")
# plt.axis((0,6,50,1))

plt.ylabel(u'Alguns Números y')

plt.xlabel(u'Alguns Números x')

plt.show()

## FORMATAR -  CORES

# COR - CARACTERE
# AZUL - b
# VERDE - g
# VERMELHO - r
# CIANO - c
# MAGENTA - m
# AMARELO - y
# PRETO
# BRANCO - w

## FORMATAÇÃO - LINHA

# Tipo da linha - Caractere
# Linha cheia - '-'
# Linha tracejada - '--'
# Linha traço-ponto - '-.'
# Linha pontilhada - ':'

