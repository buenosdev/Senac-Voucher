# Tratamento de Erro em Conversão de Tipos:

# Converta uma string para um tipo numérico (por exemplo, int ou float) e trate exceções caso a conversão falhe.

numero_str = input("Digite a string: ")
try:
    numero_int = int(numero_str)
except  ValueError:
    print("| Impossivel converter |")
try:
    print(numero_int)  
except NameError:
    print("| Nome errado |")
.