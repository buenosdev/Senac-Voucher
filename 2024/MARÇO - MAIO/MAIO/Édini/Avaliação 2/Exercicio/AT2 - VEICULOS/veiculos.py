# Definição da classe de Habilitacao
class Habilitacao:
    def __init__(self, categoriaA=False, categoriaB=False, categoriaC=False, categoriaD=False, categoriaE=False):
        self.categoriaA = categoriaA
        self.categoriaB = categoriaB
        self.categoriaC = categoriaC
        self.categoriaD = categoriaD
        self.categoriaE = categoriaE

# Definição das classes dos tipos de veículos
class Veiculo:
    def __init__(self, modelo, tracao, especie, categoria, capacidade_passageiros, capacidade_carga, velocidade_maxima):
        self.modelo = modelo
        self.tracao = tracao
        self.especie = especie
        self.categoria = categoria
        self.capacidade_passageiros = capacidade_passageiros
        self.capacidade_carga = capacidade_carga
        self.velocidade_maxima = velocidade_maxima

    def __str__(self):
        return f"Modelo: {self.modelo}, Tração: {self.tracao}, Espécie: {self.especie}, Categoria: {self.categoria}, " \
               f"Capacidade de Passageiros: {self.capacidade_passageiros}, Capacidade de Carga: {self.capacidade_carga}, " \
               f"Velocidade Máxima: {self.velocidade_maxima} km/h"