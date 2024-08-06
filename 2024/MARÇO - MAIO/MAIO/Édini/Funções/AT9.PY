# Jogo de Par ou Ímpar:
# Escolha 0 para par ou 1 para ímpar. Em seguida, forneça um número. Crie um programa que 
# determine se a soma do número escolhido com um número aleatório é par ou ímpar.


# import random

# def soma(impar,par):
# num = int(input("Escolha "))
# par = num%2 == 0
# impar = num%2 !=0


# if num + random.num(par,impar) == par:
#     print("Seu número é par.")

# else:
#     print("Seu número é ímpar.")

# soma(impar,par)





import random

def soma(par):
    num = int(input("Escolha um número: "))
    par = num % 2 == 0

    if random.choice([True, False]) == par:
        print("A soma é par.")
    else:
        print("A soma é ímpar.")

soma(par)
