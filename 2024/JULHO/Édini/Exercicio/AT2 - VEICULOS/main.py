from recomendacao import * 
from veiculos import *


# Função principal
def main():
    # Inicialização da habilitação (simulação de dados para exemplo)
    habilitacao = Habilitacao(categoriaA=True, categoriaB=True, categoriaC=True, categoriaD=True, categoriaE=True)

    while True:
        print("\nMenu de Busca de Veículos:")
        print("0. Sair")
        print("1. Buscar Veículos")

        opcao = input("Digite a opção desejada: ")

        if opcao == "0":
            print("Saindo do programa...")
            break
        elif opcao == "1":
            tracao = input("Digite o tipo de tração desejada (ou deixe em branco para qualquer): ").strip()
            especie = input("Digite a espécie de veículo desejada (ou deixe em branco para qualquer): ").strip()
            categoria = input("Digite a categoria de veículo desejada (A, B, C, D, E) (ou deixe em branco para qualquer): ").strip().upper()
            quant_passageiros = int(input("Digite a quantidade de passageiros desejada: "))
            quant_carga = int(input("Digite a capacidade de carga desejada (em kg): "))
            velocidade = int(input("Digite a velocidade máxima desejada (em km/h): "))

            recomendacoes = buscar_veiculos(habilitacao, tracao, especie, categoria, quant_passageiros, quant_carga, velocidade)

            if recomendacoes:
                print("\nVeículos recomendados:")
                for veiculo in recomendacoes:
                    print(veiculo)
            else:
                print("\nNenhum veículo encontrado que atenda aos critérios.")

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()