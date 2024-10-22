# 1 - Reino
class Animal:
    def __init__(self, nome, nome_cientifico, nutricao, habitat):
        self.nome = nome
        self.nome_cientifico = nome_cientifico
        self.nutricao = nutricao
        self.habitat = habitat
        
    def alimentar(self):
        print("Comer...")

    def movimentar(self):
        print("Andou/Nadou/Voou...")

# 2 Filo
class Chordata(Animal):
    def __init__(self, nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto):
        super().__init__(nome, nome_cientifico, nutricao, habitat)
        self.nervoso_dorsal = nervoso_dorsal
        self.endoesqueleto = endoesqueleto

    def caracteristicas_filo(self):
        print("O filo Chordata é caracterizado pela presença de um nervoso dorsal,\n um endoesqueleto e estruturas relacionadas ao sistema nervoso,\n fundamentais para a classificação dos organismos desse grupo.")


# 3 Classe
class Mamiferos(Chordata):
    def __init__(self, nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas):
        super().__init__(nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto)
        self.mamarias = mamarias
        self.endotermicos = endotermicos
        self.orelhas = orelhas

    def amamentar(self):
        print("A mamífera está amamentando os filhotes.")

# 4 Ordem
class Carnivora(Mamiferos):
    def __init__(self, nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas, caninos_molares, pelagem_peltada):
        super().__init__(nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas)
        self.caninos_molares = caninos_molares
        self.pelagem_peltada = pelagem_peltada

    def habilidade_caca(self):
        print("O carnívoro usa suas habilidades de caça para pegar presas.")



# 5 Familia
class Canideos(Carnivora):
    def __init__(self, nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas, caninos_molares, pelagem_peltada, territorialidade, org_jacobson):
        super().__init__(nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas, caninos_molares, pelagem_peltada)
        self.territorialidade = territorialidade
        self.org_jacobson = org_jacobson
    
    def marcar_territorio(self):
        print("O canídeo está marcando seu território.")


# 6 Gênero
class Vulpes(Canideos):
    def __init__(self, nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas, caninos_molares, pelagem_peltada, territorialidade, org_jacobson, cauda_espessa, onivoro):
        super().__init__(nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas, caninos_molares, pelagem_peltada, territorialidade, org_jacobson)
        self.cauda_espessa = cauda_espessa
        self.onivoro = onivoro

    def adaptabilidade(self):
        print(f"A raposa do gênero Vulpes é altamente adaptável,\n conseguindo viver em diversos habitats, como:\n florestas, desertos e áreas urbanas.")

# 7 Espécie
class Raposa_Vermelha(Vulpes):
    def __init__(self, nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas, caninos_molares, pelagem_peltada, territorialidade, org_jacobson, cauda_espessa, onivoro, adaptabilidade, laranja_avermelhada):
        super().__init__(nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas, caninos_molares, pelagem_peltada, territorialidade, org_jacobson, cauda_espessa, onivoro)
        self.adaptabilidade = adaptabilidade
        self.laranja_avermelhada = laranja_avermelhada

    def adaptabilidade(self):
        print("A raposa-vermelha é altamente adaptável a diversos habitats.")



raposa = Raposa_Vermelha(
    nome="Raposa-vermelha",
    nome_cientifico="Vulpes vulpes",
    nutricao="Onívoro",
    habitat="Diversos",
    nervoso_dorsal="Sim",
    endoesqueleto="Sim",
    mamarias="Sim",
    endotermicos="Sim",
    orelhas="Sim",
    caninos_molares="Sim",
    pelagem_peltada="Sim",
    territorialidade="Espessa",
    org_jacobson="Sim",
    cauda_espessa="Sim",
    onivoro="Sim",
    adaptabilidade="Alta",
    laranja_avermelhada="Laranja-avermelhada"
)

Raposa_Vermelha.alimentar(raposa)
print()
Raposa_Vermelha.movimentar(raposa)
print()
Raposa_Vermelha.caracteristicas_filo(raposa)
print()
Raposa_Vermelha.amamentar(raposa)
print()
Raposa_Vermelha.habilidade_caca(raposa)
print()
Raposa_Vermelha.marcar_territorio(raposa)
print()
Raposa_Vermelha.adaptabilidade(raposa)

print(f"""\n\n
    Nome: {raposa.nome}
    Nome Científico: {raposa.nome_cientifico}
    Nutrição: {raposa.nutricao}
    Habitat: {raposa.habitat}
    Nervoso Dorsal: {raposa.nervoso_dorsal}
    Endoesqueleto: {raposa.endoesqueleto}
    Mamárias: {raposa.mamarias}
    Endotérmicos: {raposa.endotermicos}
    Orelhas: {raposa.orelhas}
    Caninos/Molares: {raposa.caninos_molares}
    Pelagem Peltada: {raposa.pelagem_peltada}
    Territorialidade: {raposa.territorialidade}
    Órgão de Jacobson: {raposa.org_jacobson}
    Cauda Espessa: {raposa.cauda_espessa}
    Adaptabilidade: {raposa.adaptabilidade}
    Cor: {raposa.laranja_avermelhada}
""")