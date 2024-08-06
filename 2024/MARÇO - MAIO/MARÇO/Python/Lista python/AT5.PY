# 5. Altere o programa anterior permitindo ao usuário informar as 
# populações e as taxas de crescimento iniciais. Valide a entrada e permita 
# repetir a operação. 
# (4 e 5): Solução: Validação de dados em Python
def calcular_anos(populacao_A, populacao_B, taxa_crescimento_A, taxa_crescimento_B):
    anos = 0
    while populacao_A < populacao_B:
        populacao_A += populacao_A * taxa_crescimento_A
        populacao_B += populacao_B * taxa_crescimento_B
        anos += 1
    return anos

while True:
    try:
        populacao_A = float(input("Digite a população do país A: "))
        populacao_B = float(input("Digite a população do país B: "))
        taxa_crescimento_A = float(input("Digite a taxa de crescimento anual do país A (em decimal): "))
        taxa_crescimento_B = float(input("Digite a taxa de crescimento anual do país B (em decimal): "))

        anos = calcular_anos(populacao_A, populacao_B, taxa_crescimento_A, taxa_crescimento_B)
        print("Serão necessários", anos, "anos para que a população do país A ultrapasse ou iguale a população do país B.")

        repetir = input("Deseja repetir a operação? (s/n): ")
        if repetir.lower() != 's':
            break
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")
