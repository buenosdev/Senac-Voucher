from veiculos import *
from main import *
# Função para remover acentos e converter para minúsculas
import unicodedata

def remover_acentos(texto):
    return ''.join(ch for ch in unicodedata.normalize('NFD', texto)
                   if unicodedata.category(ch) != 'Mn').lower()

# Função para buscar veículos com base nas preferências do usuário
def buscar_veiculos(habilitacao, tracao, especie, categoria, quant_passageiros, quant_carga, velocidade):
    veiculos_disponiveis = [
        Veiculo("Motocicleta","Tração Dianteira", "Motocicleta", "A", 2, 50, 180),
        Veiculo("Sedan", "Tração Traseira", "Carro de Passeio", "B", 5, 400, 220),
        Veiculo("Caminhão", "Tração 6x4", "Caminhão de Carga", "C", 2, 8000, 120),
        Veiculo("Ônibus", "Tração 4x2", "Ônibus de Passageiros", "D", 50, 0, 100),
        Veiculo("Carreta", "Tração 8x4", "Carreta", "E", 2, 20000, 80),
        Veiculo("SUV", "Tração 4x4", "Carro de Passeio", "B", 7, 500, 200),
        Veiculo("Van", "Tração 4x2", "Van de Passageiros", "D", 12, 1000, 140),
        Veiculo("Bicicleta", "Tração Humana", "Bicicleta", "A", 1, 20, 40),
        Veiculo("Furgão", "Tração 4x2", "Furgão de Carga", "C", 3, 1500, 150),
        Veiculo("Micro-ônibus", "Tração 4x2", "Micro-ônibus de Passageiros", "D", 30, 0, 120),
        Veiculo("Pick-up", "Tração 4x4", "Pick-up", "B", 4, 800, 180),
        Veiculo("Caminhonete", "Tração 4x4", "Caminhonete", "B", 5, 1000, 200),
        Veiculo("Trator", "Tração 4x2", "Trator", "C", 1, 5000, 60),
        Veiculo("Limousine", "Tração Traseira", "Carro de Passeio", "B", 8, 600, 240),
        Veiculo("Quadriciclo", "Tração 4x2", "Quadriciclo", "A", 2, 100, 120),
        Veiculo("Caminhão de Bombeiro", "Tração 6x6", "Caminhão de Bombeiro", "C", 3, 10000, 100),
        Veiculo("Carro Esportivo", "Tração Traseira", "Carro de Passeio", "B", 2, 300, 280),
        Veiculo("Lancha", "Tração Aquática", "Lancha", "E", 6, 0, 100),
        Veiculo("Avião Particular", "Tração Aérea", "Avião Particular", "E", 4, 2000, 300),
        Veiculo("Helicóptero", "Tração Aérea", "Helicóptero", "E", 6, 500, 280),
        Veiculo("Empilhadeira", "Tração 4x2", "Empilhadeira", "C", 1, 2000, 20),
        Veiculo("Carro de Corrida", "Tração Traseira", "Carro de Passeio", "B", 1, 200, 320),
        Veiculo("Ônibus Escolar", "Tração 4x2", "Ônibus de Passageiros", "D", 40, 0, 90),
        Veiculo("Carrinho de Golfe", "Tração 4x2", "Carrinho de Golfe", "A", 2, 50, 30),
        Veiculo("Triciclo Elétrico", "Tração Dianteira", "Triciclo Elétrico", "A", 2, 100, 60)
    ]

    recomendacoes = []

    # Limites de tolerância para os critérios
    limite_passageiros = 1  # Aceita veículos que comportem pelo menos quant_passageiros - limite_passageiros
    limite_carga = 1000     # Aceita veículos que suportem pelo menos quant_carga - limite_carga kg
    limite_velocidade = 20  # Aceita veículos que tenham velocidade máxima pelo menos velocidade - limite_velocidade km/h

    for veiculo in veiculos_disponiveis:
        # Verifica se o veículo está na categoria permitida pela habilitação
        if (habilitacao.categoriaA and veiculo.categoria == "A") or \
           (habilitacao.categoriaB and veiculo.categoria == "B") or \
           (habilitacao.categoriaC and veiculo.categoria == "C") or \
           (habilitacao.categoriaD and veiculo.categoria == "D") or \
           (habilitacao.categoriaE and veiculo.categoria == "E"):
            # Verifica se o veículo tem a tração desejada
            if tracao and remover_acentos(veiculo.tracao).lower().find(remover_acentos(tracao).lower()) != -1:
                # Verifica se o veículo tem a espécie desejada
                if especie and remover_acentos(veiculo.especie).lower().find(remover_acentos(especie).lower()) != -1:
                    # Verifica se o veículo atende à capacidade de passageiros, carga e velocidade desejadas com tolerância
                    if (veiculo.capacidade_passageiros >= quant_passageiros - limite_passageiros and
                        veiculo.capacidade_carga >= quant_carga - limite_carga and
                        veiculo.velocidade_maxima >= velocidade - limite_velocidade):
                        recomendacoes.append(veiculo)

    return recomendacoes
