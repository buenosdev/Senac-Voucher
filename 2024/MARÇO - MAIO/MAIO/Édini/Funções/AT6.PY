# Número Invertido:
# Crie um software que recebe um número do usuário, passa esse valor para uma função e ela 
# retorna o número escrito ao inverso. Por exemplo, se o usuário der o valor 1234, a função 
# deve retornar 4321. Dica: primeiro, crie uma função que conta quantos dígitos tem um 
# número.

# def invertido(num):
#     num = int(input("Digite um número: "))
#     lista = {num}
#     lista_invertida = lista[::-1]
#     print(lista_invertida)

# invertido(0)


retorne = input("Digite seu número: ") 

def InverterNum():
    reverter =[]
    reverter.extend(retorne)
    reverter.reverse()
    revertido = ''.join(reverter)

    return revertido

ver = print("Seu número invertido: " + InverterNum())