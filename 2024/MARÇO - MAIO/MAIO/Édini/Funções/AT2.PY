# Existência de um Triângulo:
# Crie um programa que recebe os três lados de um triângulo e passa esses valores para uma 
# função que verifica se esse triângulo existe ou não. Para que um triângulo exista, cada lado 
# deve ser maior que o módulo da subtração dos outros dois lados e menor que a soma dos 
# outros dois lados.

def verifica_triangulo(lado1, lado2, lado3):
    # Verifica se cada lado é menor que a soma e maior que a diferença dos outros dois
    if lado1 < (lado2 + lado3) and lado1 > abs(lado2 - lado3):
        if lado2 < (lado1 + lado3) and lado2 > abs(lado1 - lado3):
            if lado3 < (lado1 + lado2) and lado3 > abs(lado1 - lado2):
                return True
    return False

def func():
    lado1 = int(input("Digite o primeiro lado: "))
    lado2 = int(input("Digite o segundo lado: "))
    lado3 = int(input("Digite o terceiro lado: "))
    
    if verifica_triangulo(lado1, lado2, lado3):
        print("Esse triângulo existe.")
    else:
        print("Esse triângulo é inexistente.")

func()




# def sub(lado1,lado2,lado3):
#     sub1 = lado1 - lado2
#     sub2 = lado2 - lado3
#     sub3 = lado1 - lado3
#     if sub1<0:
#         sub1 = sub1*-1
#     if sub2<0:
#         sub2 = sub2*-1
#     if sub3<0:
#         sub3 = sub3*-1
#     return False

# def adicao(lado1,lado2,lado3):
#     ad1 = lado1 + lado2
#     ad2 = lado2 + lado3
#     ad3 = lado1 + lado3


# def func(lado1,lado2,lado3):
#     lado1 = int(input("Digite o primeiro lado: "))
#     lado2 = int(input("Digite o segundo lado: "))
#     lado3 = int(input("Digite o terceiro lado: "))
    
#     if sub and adicao(lado1, lado2, lado3):
#         print("Esse triângulo existe.")
#         return True
#     else:
#         print("Esse triângulo é inexistente.")



# func(1,1,1)