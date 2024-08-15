# Tratamento de Erro em Acesso a Listas:

# Acesse uma posição inválida em uma lista e trate a exceção IndexError. ​
lista = [1,2,3,4,5]
try:
    num = int(input("Digite um número: "))
    elemento = lista[num]
    print("Número encontrado.")
        
except IndexError:
    print("Número não encontrado.")

except ValueError:
    print("Entrada inválida.")