#Consultar estoque,atualizar estoque, adicionar novos produtos
#Adicionar novos produtos: Nome, descrição (Higiene, alimento, produtos para casa etc) e um subtipo (Alimento: frios, carne, legumes, massas, etc) preço e código do produto.
#Preço alteravel 

#Exibir um menu logo quando entrar no sistema.

#Dentro das sessões escolhidas devem ter uma sub-sessão
#Escolhe os produtos que vai colcar dentro do carrinho de compras e se mudar de ideia, pode remove-los

produtos = {
    '1': {'nome': 'Jato', 'descricao': 'Jatinho legal', 'subtipo': 'Aéreo', 'preco': 299999.99, 'quantidade': 50},
    '2': {'nome': 'Banana', 'descricao': 'Banana maça legal', 'subtipo': 'Fruta', 'preco': 0.99, 'quantidade': 30},
    '3': {'nome': 'Relógio', 'descricao': 'Relógio Legal', 'subtipo': 'Acessório', 'preco': 99.99, 'quantidade': 20}
}

carrinho = []
total = 0.0

usuario = input("Você é um (1) Cliente ou (2) Funcionário? ")
if usuario == '1':
    cpf = input("Digite seu CPF: ")
    nome = input("Digite seu nome: ")
elif usuario == '2':
    cpf = input("Digite seu CPF: ")
    nome = input("Digite seu nome: ")
    matricula = input("Digite sua matrícula: ")
    data_nascimento = input("Digite sua data de nascimento: ")

opcao = ''
while opcao != '0':
    print("____________________")
    print("\n1. Adicionar novos produto")
    print("2. Atualizar estoque")
    print("3. Consultar estoque")
    print("4. Adicionar ao carrinho")
    print("5. Remover do carrinho")
    print("6. Ver carrinho e finalizar compra")
    print("0. Sair")
    print("____________________")
    opcao = input("\nEscolha uma opção: ")

    if opcao == '1' and usuario == '2':
        codigo = input("Digite o código do produto: ")
        if codigo not in produtos:
            nome = input("Digite o nome do produto: ")
            descricao = input("Digite a descrição do produto: ")
            subtipo = input("Digite o sub-tipo do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade do produto: "))
            produtos[codigo] = {'nome': nome, 'descricao': descricao, 'subtipo': subtipo, 'preco': preco, 'quantidade': quantidade}
            print("Produto cadastrado com sucesso.")
        else:
            print("Produto já existe.")

    elif opcao == '2' and usuario == '2':
        codigo = input("Digite o código do produto: ")
        if codigo in produtos:
            preco = float(input(f"Digite o novo preço para {produtos[codigo]['nome']}: "))
            quantidade = int(input(f"Digite a nova quantidade para {produtos[codigo]['nome']}: "))
            produtos[codigo]['preco'] = preco
            produtos[codigo]['quantidade'] = quantidade
            print("Produto atualizado com sucesso.")
        else:
            print("Produto não encontrado.")

    elif opcao == '3':
        if produtos:
            print("Produtos cadastrados:")
            for codigo in produtos:
                produto = produtos[codigo]
                print(f"Código: {codigo}, Nome: {produto['nome']}, Descrição: {produto['descricao']}, Subtipo: {produto['subtipo']}, Preço: R${produto['preco']}, Quantidade: {produto['quantidade']}")
        else:
            print("Nenhum produto cadastrado.")

    elif opcao == '4':
        codigo = input("Digite o código do produto: ")
        if codigo in produtos:
            quantidade = int(input("Digite a quantidade a ser adicionada: "))
            if produtos[codigo]['quantidade'] >= quantidade:
                carrinho.append((codigo, quantidade))
                produtos[codigo]['quantidade'] -= quantidade
                print("Produto adicionado ao carrinho.")
            else:
                print("Estoque insuficiente.")
        else:
            print("Produto não encontrado.")

    elif opcao == '5':
        codigo = input("Digite o código do produto a ser removido: ")
        for item in carrinho:
            if item[0] == codigo:
                carrinho.remove(item)
                produtos[codigo]['quantidade'] += item[1]
                print("Produto removido do carrinho.")
                break
        else:
            print("Produto não encontrado no carrinho.")

    elif opcao == '6':
        if not carrinho:
            print("Carrinho vazio.")
        else:
            total = 0.0
            print("Resumo da compra:")
            for item in carrinho:
                codigo, quantidade = item
                produto = produtos[codigo]
                print(f"{produto['nome']} - {quantidade} x R${produto['preco']} = R${produto['preco'] * quantidade}")
                total += produto['preco'] * quantidade

            impostos_nacional = total * 0.05
            impostos_estadual = total * 0.08
            impostos_municipal = total * 0.12
            total_impostos = impostos_nacional + impostos_estadual + impostos_municipal
            total_com_impostos = total + total_impostos

            print(f"Total: R${total}")
            print(f"Impostos Nacionais: R${impostos_nacional}")
            print(f"Impostos Estaduais: R${impostos_estadual}")
            print(f"Impostos Municipais: R${impostos_municipal}")
            print(f"Total com impostos: R${total_com_impostos}")

            while True:
                print("\nFormas de pagamento:")
                print("1. Dinheiro")
                print("2. Pix")
                print("3. Cartão")
                forma = input("Escolha a forma de pagamento: ")

                if forma == '1':
                    valor_entregue = float(input("Digite o valor entregue: "))
                    if valor_entregue < total_com_impostos:
                        print("Valor insuficiente.")
                    else:
                        troco = valor_entregue - total_com_impostos
                        print(f"Compra aprovada. Troco: R${troco}")
                        carrinho = []
                        total = 0.0
                        break
                elif forma == '2' or forma == '3':
                    saldo = float(input("Digite o saldo disponível: "))
                    if saldo >= total_com_impostos:
                        print("Compra aprovada.")
                        carrinho = []
                        total = 0.0
                        break
                    else:
                        print("Saldo insuficiente.")
                else:
                    print("Forma de pagamento inválida.")

    elif opcao == '0':
        break

    else:
        print("Opção inválida.")
