# Desenvolva um algoritmo com os candidatos a eleição no município de Campo Grande.
# Os mais votados Vereadores
# Gráfico em pizza

import pandas as pd
import matplotlib.pyplot as plt

# Candidatos eleitos a vereador 
data = {
    'Candidato': [
        'Marquinhos Trad – PDT', 'Rafael Tavares – PL', 'Carlão Comunitário Mesmo – PSB', 
        'Silvio Pitu – PSDB', 'Veterinário Francisco – UNIÃO', 'Fabio Rocha – UNIÃO', 
        'Professor Riverton – PP', 'Junior Coringa – MDB', 'Dr Victor Rocha – PSDB', 
        'Professor Juari – PSDB', 'Flavio Cabo Almi – PSDB', 'Luiza Ribeiro – PT', 
        'André Salineiro Agente Federal – PL', 'Papy – PSDB', 'Ana Portela – PL', 
        'Neto Santos – Republicanos', 'Maicon Nogueira – PP', 'Delei Pinheiro – PP', 
        'Wilson Lands – Avante', 'Herculano Borges – Republicanos', 'Beto Avelar – PP', 
        'Dr Jamal – MDB', 'Landmark – PT', 'Clodoilson Pires – Podemos', 
        'Jean Ferreira – PT', 'Dr Lívio – UNIÃO', 'Ronilço Guerreiro – Podemos', 
        'Leinha – Avante', 'Otávio Trad – PSD'
    ],
    'Votos': [
        8567, 8128, 6912, 6409, 6371, 6314, 6271, 6131, 5355, 5050, 5003, 4982, 
        4782, 4641, 4577, 4576, 4236, 4179, 4148, 4119, 4063, 4030, 4022, 3859, 
        3768, 3636, 3244, 3167, 2426
    ]
}

df = pd.DataFrame(data)

# Plotar o gráfico em pizza
plt.figure(figsize=(10, 10))
plt.pie(df['Votos'], labels=df['Candidato'], autopct='%1.1f%%', startangle=140)
plt.title('Distribuição de Votos dos Candidatos Eleitos a Vereador em Campo Grande')
plt.show()








# Candidatos eleitos a prefeitos

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Candidato": ["Marquinhos Trad", "Rafael Tavares", "Carlão", "Silvio Pitu", "Veterinário Francisco", "Fábio Rocha", 
                  "Professor Riverton", "Junior Coringa", "Dr Victor Rocha", "Professor Juari", "Flavio Cabo Almi", 
                  "Luiza Ribeiro", "André Salineiro", "Papy", "Ana Portela", "Neto Santos", "Maicon Nogueira", 
                  "Delei Pinheiro", "Wilson Lands", "Herculano Borges", "Beto Avelar", "Doutor Jamal", "Landmark", 
                  "Dr Sandro", "Betinho", "Clodoilson Pires", "Jean Ferreira", "Professor João Rocha", 
                  "Valdir Gomes", "Dr Lívio"],
    "Partido": ["PDT", "PL", "PSB", "PSDB", "União", "União", "PP", "MDB", "PSDB", "PSDB", 
                "PSDB", "PT", "PL", "PSDB", "PL", "Republicanos", "PP", "PP", 
                "Avante", "Republicanos", "PP", "MDB", "PT", 
                "PP", "Republicanos", "Pode", 
                "PT","PP","PP","União"],
    "Votos": [8567, 8128, 6912, 6409, 6371, 6314, 6271, 6131, 5355, 5050, 5003, 4982, 4782, 4641, 4577, 4576, 4236, 4179, 4148, 4119, 4063, 4030, 4022, 3922, 3877, 3859, 3768, 3693, 3648, 3636]
}

df = pd.DataFrame(data)

# Criar gráfico de barras
plt.figure(figsize=(10,8))
plt.barh(df['Candidato'], df['Votos'], color='skyblue')
plt.xlabel('Votos')
plt.ylabel('Candidato')
plt.title('Votos por Candidato')
plt.gca().invert_yaxis() 
plt.show()

