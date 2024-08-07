```
import json

  

# Nome do arquivo onde os dados serão salvos

DATA_FILE = 'vendas.json'

  

def carregar_dados():

    """Carrega os dados do arquivo JSON ou retorna um dicionário padrão se o arquivo não existir ou estiver corrompido."""

    try:

        with open(DATA_FILE, 'r') as file:

            dados = json.load(file)

            garantir_estrutura_correta(dados)

            return dados

    except (FileNotFoundError, json.JSONDecodeError):

        return inicializar_dados()

  

def salvar_dados(dados):

    """Salva os dados no arquivo JSON."""

    with open(DATA_FILE, 'w') as file:

        json.dump(dados, file, indent=4)

  

def formatar_nome(nome):

    """Formata o nome com a primeira letra maiúscula."""

    return nome.strip().title()

  

def garantir_estrutura_correta(dados):

    """Garante que a estrutura dos dados esteja no formato esperado."""

    if not isinstance(dados.get("curso_manha"), dict):

        dados["curso_manha"] = {}

    if not isinstance(dados.get("curso_noite"), dict):

        dados["curso_noite"] = {}

    if not isinstance(dados.get("no_papel"), (int, float)):

        dados["no_papel"] = 0

    if not isinstance(dados.get("igreja"), dict):

        dados["igreja"] = {}

    if not isinstance(dados.get("total_atual"), (int, float)):

        dados["total_atual"] = 0

    if not isinstance(dados.get("pessoas_pendentes"), dict):

        dados["pessoas_pendentes"] = {}

  

def inicializar_dados():

    """Inicializa o dicionário de dados com a estrutura padrão."""

    return {

        "curso_manha": {},

        "curso_noite": {},

        "no_papel": 0,

        "igreja": {},

        "total_atual": 0,

        "pessoas_pendentes": {}

    }

  

def adicionar_venda(dados):

    """Adiciona uma venda aos dados."""

    print("\nEscolha o período ou tipo de venda:")

    print("1. Curso - Manhã")

    print("2. Curso - Noite")

    print("3. No papel")

    print("4. Igreja")

  

    escolha = input("Escolha uma opção: ").strip()

  

    if escolha in ['1', '2']:

        pessoa = formatar_nome(input("Informe o nome da pessoa: ").strip())

        valor = float(input("Informe o valor da venda: R$").strip())

        chave = "curso_manha" if escolha == '1' else "curso_noite"

        if chave not in dados:

            dados[chave] = {}

        dados[chave][pessoa] = dados[chave].get(pessoa, 0) + valor

    elif escolha == '3':

        valor = float(input("Informe o valor registrado no papel: R$").strip())

        dados["no_papel"] += valor

    elif escolha == '4':

        pessoa = formatar_nome(input("Informe o nome da pessoa (Igreja): ").strip())

        valor = float(input("Informe o valor da venda para a Igreja: R$").strip())

        if "igreja" not in dados:

            dados["igreja"] = {}

        dados["igreja"][pessoa] = dados["igreja"].get(pessoa, 0) + valor

    else:

        print("Opção inválida. Tente novamente.")

        return

  

    dados["total_atual"] += valor

    salvar_dados(dados)

    print("Venda adicionada com sucesso!")

  

def remover_venda(dados):

    """Remove uma venda dos dados."""

    print("\nEscolha o período ou tipo de venda para remover:")

    print("1. Curso - Manhã")

    print("2. Curso - Noite")

    print("3. No papel")

    print("4. Igreja")

  

    escolha = input("Escolha uma opção: ").strip()

  

    if escolha in ['1', '2']:

        pessoa = formatar_nome(input("Informe o nome da pessoa: ").strip())

        valor = float(input("Informe o valor da venda a ser removido: R$").strip())

        chave = "curso_manha" if escolha == '1' else "curso_noite"

        if chave in dados and pessoa in dados[chave]:

            if dados[chave][pessoa] >= valor:

                dados[chave][pessoa] -= valor

                if dados[chave][pessoa] == 0:

                    del dados[chave][pessoa]

            else:

                print("O valor a ser removido é maior que o valor registrado.")

        else:

            print("Pessoa não encontrada.")

    elif escolha == '3':

        valor = float(input("Informe o valor registrado no papel a ser removido: R$").strip())

        if dados.get("no_papel", 0) >= valor:

            dados["no_papel"] -= valor

        else:

            print("O valor a ser removido é maior que o valor registrado.")

    elif escolha == '4':

        pessoa = formatar_nome(input("Informe o nome da pessoa (Igreja): ").strip())

        valor = float(input("Informe o valor da venda para a Igreja a ser removido: R$").strip())

        if "igreja" in dados and pessoa in dados["igreja"]:

            if dados["igreja"][pessoa] >= valor:

                dados["igreja"][pessoa] -= valor

                if dados["igreja"][pessoa] == 0:

                    del dados["igreja"][pessoa]

            else:

                print("O valor a ser removido é maior que o valor registrado.")

        else:

            print("Pessoa não encontrada.")

    else:

        print("Opção inválida. Tente novamente.")

        return

  

    dados["total_atual"] -= valor

    salvar_dados(dados)

    print("Venda removida com sucesso!")

  

def adicionar_pessoa_pendente(dados):

    """Adiciona uma pessoa e seu valor pendente aos dados."""

    pessoa = formatar_nome(input("Informe o nome da pessoa pendente: ").strip())

    valor = float(input("Informe o valor pendente: R$").strip())

    if not isinstance(dados.get("pessoas_pendentes"), dict):

        dados["pessoas_pendentes"] = {}

    dados["pessoas_pendentes"][pessoa] = dados["pessoas_pendentes"].get(pessoa, 0) + valor

    salvar_dados(dados)

    print("Pessoa pendente e valor adicionados com sucesso!")

  

def remover_pessoa_pendente(dados):

    """Remove uma pessoa e seu valor pendente dos dados."""

    pessoa = formatar_nome(input("Informe o nome da pessoa pendente a ser removida: ").strip())

    if isinstance(dados.get("pessoas_pendentes"), dict) and pessoa in dados["pessoas_pendentes"]:

        del dados["pessoas_pendentes"][pessoa]

        salvar_dados(dados)

        print("Pessoa pendente removida com sucesso!")

    else:

        print("Pessoa não encontrada ou dados corrompidos.")

  

def remover_todos_dados(dados):

    """Remove todos os dados com confirmação de dupla camada."""

    confirmacao1 = input("Digite 'CONFIRMAR' para confirmar a remoção de todos os dados: ").strip().upper()

    if confirmacao1 == 'CONFIRMAR':

        confirmacao2 = input("Digite 'DELETAR' para confirmar a remoção completa: ").strip().upper()

        if confirmacao2 == 'DELETAR':

            dados.clear()

            dados.update(inicializar_dados())  # Re-inicializa a estrutura de dados

            salvar_dados(dados)

            print("Todos os dados foram removidos com sucesso!")

        else:

            print("Confirmação incorreta. A remoção foi cancelada.")

    else:

        print("Confirmação incorreta. A remoção foi cancelada.")

  

def exibir_dados(dados):

    """Exibe todos os dados armazenados."""

    for chave in ["curso_manha", "curso_noite", "igreja"]:

        if isinstance(dados.get(chave), dict):  # Verifica se o valor é um dicionário

            print(f"\n{chave.replace('_', ' ').title()}:")

            for pessoa, valor in dados[chave].items():

                print(f"{pessoa} - R${valor:.2f}")

        else:

            print(f"\n{chave.replace('_', ' ').title()}: Dados corrompidos ou não encontrados.")

  

    print(f"\nNo papel - R${dados.get('no_papel', 0):.2f}")

  

    print(f"\nTotal atual: R${dados.get('total_atual', 0):.2f}")

  

    if isinstance(dados.get("pessoas_pendentes"), dict):

        print("\nPessoas pendentes:")

        if dados["pessoas_pendentes"]:

            for pessoa, valor in dados["pessoas_pendentes"].items():

                print(f"{pessoa} - R${valor:.2f}")

        else:

            print("Nenhuma")

    else:

        print("\nPessoas pendentes: Dados corrompidos ou não encontrados.")

  

def main():

    dados = carregar_dados()

  

    while True:

        print("\nMenu:")

        print("1. Adicionar venda")

        print("2. Remover venda")

        print("3. Adicionar pessoa pendente")

        print("4. Remover pessoa pendente")

        print("5. Remover todos os dados")

        print("6. Exibir dados")

        print("7. Sair")

  

        escolha = input("Escolha uma opção: ").strip()

  

        if escolha == '1':

            adicionar_venda(dados)

        elif escolha == '2':

            remover_venda(dados)

        elif escolha == '3':

            adicionar_pessoa_pendente(dados)

        elif escolha == '4':

            remover_pessoa_pendente(dados)

        elif escolha == '5':

            remover_todos_dados(dados)

        elif escolha == '6':

            exibir_dados(dados)

        elif escolha == '7':

            break

        else:

            print("Opção inválida. Tente novamente.")

  

if __name__ == "__main__":

    main()
```