# Escreva um programa que faça um cadastro de clientes. Seu programa deve:
# [Entrada]: receber os seguintes dados do usuário:
# 1) o nome completo; 2) o RG do cliente; 3) o CPF e; 4) o telefone do cliente.

# [Processamento]: Seu programa deve armazenar todos os dados em uma ÚNICA LISTA. [Saída]: AO FINAL, SOMENTE AO FINAL, Seu programa deve mostrar (um cliente por linha):
# a) o nome completo do paciente, b) O RG; c) o CPF e; d) o telefone do cliente.
# Obs: o usuário deve fazer esse procedimento para quantos clientes ELE QUISER.

# Exemplo de Entrada:
# Digite o nome completo do cliente (ou digite 'sair' para encerrar): Enilda Caceres
# Digite o RG do cliente: 5478
# Digite o CPF do cliente: 5588
# Digite o telefone do cliente: 5877
# Digite o nome completo do cliente (ou digite 'sair' para encerrar): sair
# Exemplo de Saída:
# Cadastro de Clientes:
# ====================
# Nome: Enilda Caceres, RG: 5478, CPF: 5588, Telefone: 5877


cadastro = []


while True:

    nome = str(input("Digite o nome do cliente:")).upper()

    rg = int(input("Digite o RG do cliente: "))

    cpf = int(input("Digite o CPF do cliente: "))

    tell = int(input("Digite o telefone do cliente: "))

    cliente =  {"nome":nome,
                "rg":rg,
                "cpf":cpf,
                "tell":tell}
    
    cadastro.append(cliente)

    print("")
    print("Cliente cadastrado com sucesso. Digite 1 para sair e 0 para continuar")
    cod = int(input("Digite: "))

    if cod !=0:
        break
    else:
        continue

print("\nClientes cadastrados: ")
for cliente in cadastro:
    print(f'Nome: {nome}, RG: {rg}, CPF {cpf}, Telefone{tell}')

