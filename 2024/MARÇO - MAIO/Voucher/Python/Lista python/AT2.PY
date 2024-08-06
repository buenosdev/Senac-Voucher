# 2. Faça um programa que leia um nome de usuário e a sua senha e 
# não aceite a senha igual ao nome do usuário, mostrando uma mensagem 
# de erro e voltando a pedir as informações. 
# Solução: Validação de dados em Python
while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    if senha != usuario:
        print("Usuário e senha aceitos.")
        break
    else:
        print("Erro: A senha não pode ser igual ao nome de usuário. Por favor, tente novamente.")
