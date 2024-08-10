# Tratamento de Exceção Genérico:

# Escreva um método genérico que possa capturar qualquer tipo de exceção.

while True:
    try:
        a=int(input("Entre com um valor:\n"))
        break
    except ValueError:
        print("Opss!!!\nAlgo deu errado!!Entre com um valor por favor!!") 
print(a)