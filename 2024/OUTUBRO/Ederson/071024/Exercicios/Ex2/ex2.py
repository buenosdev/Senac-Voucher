import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("Exercicios/Ex2/all_seasons.csv")

df1 = df.loc[0:11145, ["player_height"]]
df2 = df.loc[0:11145, ["player_weight"]]

print(df.loc[0:11145, ["player_weight"]])

