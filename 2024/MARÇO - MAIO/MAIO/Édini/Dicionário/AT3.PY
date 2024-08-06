contatos = {}



while True:

    print("\n===============LISTA TELEFONICA===============")
    print("-Digite (1) para adicionar")
    print("-Digite (2) para buscar")
    print("-Digite (3) para remover")
    print("-Digite (0) para sair")
    print("=============================================")
    opcao = int(input("Esperando sua resposta: "))

    if opcao == 0:
          break
    
    elif opcao == 1:  
        nome = input("\nDigite o nome: ").upper()
        num = int(input("Digite o número: "))
        contatos.update({nome:num})
        print("\n|Numero adicionado a lista!|")
        print(contatos)
   
    elif opcao == 2:       
            nome = input("Nome: ").upper()
            for nome in contatos:
                print(f"\nNome: {nome} | Contato: {num}")

    elif opcao == 3:
            nome = input("Nome: ").upper()
            contatos.pop(nome)
            print(contatos)

    else:
            print("Não encontrado")


