import pandas as pd 

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# # Quantas crianças abaixo de 10 anos sobreviveram?
# crianca1 = (df.query('Age < 10 & Survived == 1'))

# # Quantas mulheres sobreviveram?
# female = (df.query('Sex== "female"'))

# # Quantos homens sobreviveram?
# male = (df.query('Sex == "male"'))

# # Quantos idosos acima de 50 anos sobreviveram?
# idoso = (df.query('Survived == 1 & Age > 50'))

# # Quantas crianças abaixo de 12 anos do sexo feminino sobreviveram?
# crianca2 = df.query('Survived == 1 & Age < 12')


# # Importações

# crianca1.to_csv('crianca1.csv', sep=';', index=False, encoding='utf-8-sig')
# crianca2.to_csv('crianca2.csv', sep=';', index=False, encoding='utf-8-sig')
# female.to_csv('female.csv', sep=';', index=False, encoding='utf-8-sig')
# male.to_csv('male.csv', sep=';', index=False, encoding='utf-8-sig')
# idoso.to_csv('idoso.csv', sep=';', index=False, encoding='utf-8-sig')

print(df.info())