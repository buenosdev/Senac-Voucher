# 3. Faça um programa que leia e valide as seguintes informações: 
# a. Nome: maior que 3 caracteres; 
# b. Idade: entre 0 e 150; 
# c. Salário: maior que zero; 
# d. Sexo: 'f' ou 'm'; 
# e. Estado Civil: 's', 'c', 'v', 'd'; 
# Use a função len(string) para saber o tamanho de um texto (número de 
# caracteres). 
# Solução: Validação de dados em Python
while True:
    nome = input("Digite seu nome (maior que 3 caracteres): ")
    idade = int(input("Digite sua idade (entre 0 e 150): "))
    salario = float(input("Digite seu salário (maior que zero): "))
    sexo = input("Digite seu sexo ('f' ou 'm'): ")
    estado_civil = input("Digite seu estado civil ('s', 'c', 'v', 'd'): ")

    if len(nome) > 3 and 0 <= idade <= 150 and salario > 0 and sexo in ['f', 'm'] and estado_civil in ['s', 'c', 'v', 'd']:
        print("Informações válidas:")
        print("Nome:", nome)
        print("Idade:", idade)
        print("Salário:", salario)
        print("Sexo:", sexo)
        print("Estado Civil:", estado_civil)
        break
    else:
        print("Erro: Alguma informação digitada é inválida. Por favor, corrija.")
