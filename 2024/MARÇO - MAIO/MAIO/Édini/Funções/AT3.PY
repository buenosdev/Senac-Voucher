# Quadrado de Hashtags:
# Faça um programa que peça um número inteiro positivo ‘n’ ao usuário e imprima um 
# quadrado de lado ‘n’ preenchido com hashtags. Por exemplo, para n=4, o resultado seria:
# ####
# ####
# ####
# ####

def quadrado(num):
    for i in range(num):
        print('#' * num)

num = int(input("Digite um número inteiro positivo: "))
quadrado(num)
