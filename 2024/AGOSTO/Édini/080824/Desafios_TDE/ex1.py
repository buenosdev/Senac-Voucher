# Divisão com Tratamento de Exceção:​

# Crie uma classe que aceite a digitação de dois números e realize a divisão entre eles, exibindo o resultado.​

# Trate as seguintes exceções:​

# ArithmeticException quando ocorrer uma divisão por zero.​

# ValueError  quando o valor informado não for numérico​

while True:
    try:
        x=int(input("Digite o primeiro número:\n"))
        y=int(input("Digite o segundo número:\n"))
    except ValueError:
        print("Digite um número!!!")
    try:
            divisao=x/y
            print(divisao)
            break
    except ArithmeticError:#ZeroDivisionError
        print("Número digitado não pode ser zero")