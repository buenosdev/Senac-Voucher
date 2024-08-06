# Número Perfeito:
# Um número é dito ser perfeito quando ele é igual à soma de seus divisores. Por exemplo, o 
# seis é perfeito, pois: 6=1+2+3
# Crie um programa que pede um número ao usuário e diga se ele é perfeito ou não.


def perfeito(num):
    soma = 0
    for i in range(1, num):
        if num % i == 0:
            soma += i
    if num == soma:
        print("Número perfeito.")
    else:
        print("Seu número não é perfeito.")

num = int(input("Digite um número: "))
perfeito(num)


# def perfeito(num):

#     np = sum(num%2 == 0)
#     if num == np:
#         print("Número perfeito.")
#     else:
#         print("Seu número não é perfeito")

# num = int(input("Digite um número: "))
# perfeito(num)












