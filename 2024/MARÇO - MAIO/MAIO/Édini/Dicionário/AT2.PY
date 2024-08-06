# Média de Notas:
# ○ Crie um dicionário com nomes de alunos e suas notas. Calcule a média das
# notas e exiba o resultado.

alunos = {
    'fulano1': (4, 10),
    'fulano2': (6, 4),
    'fulano3': (10, 8)
}

for aluno, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"A média das notas de {aluno} é {media}")
