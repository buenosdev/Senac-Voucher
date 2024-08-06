# Hipotenusa de um Triângulo Retângulo:
# Crie um programa que recebe os dois lados menores de um triângulo retângulo e uma 
# função retorna o valor da hipotenusa.

def func(lado1,lado2):
    soma = lado1**2 + lado2**2
    hipotenusa = (soma) ** 0.5
    print(hipotenusa)

func(int(input("Digite os lados: ")),int(input("Digite os lados: ")))