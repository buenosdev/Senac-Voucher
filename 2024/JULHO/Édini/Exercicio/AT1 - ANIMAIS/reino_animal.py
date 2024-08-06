# Reino: 
# Filo: 
# Classe:
# Ordem: 
# Família: 
# Gênero: 
# Espécie: 
# Característica: 

class Reino:
    def __init__(self, nomeReino):
        self.nome = nomeReino
    # def __str__(self):
    #     return f"{self.nome}"

class Filo(Reino):
    def __init__(self,nomeReino, nomeFilo):        
        super().__init__(nomeFilo)
        self.nomeFilo = nomeFilo
        self.nomeReino = nomeReino

class Classe(Filo):
    def __init__(self,nomeReino, nomeFilo, nomeClasse):
        super().__init__(nomeClasse, nomeFilo)
        self.nomeReino = nomeReino
        self.nomeReino = nomeFilo
        self.nomeClasse = nomeClasse

class Ordem(Classe):
    def __init__(self,nomeReino, nomeFilo, nomeClasse, nomeOrdem):
        super().__init__(nomeOrdem, nomeFilo, nomeClasse)
        self.nomeReino = nomeReino
        self.nomeReino = nomeFilo
        self.nomeClasse = nomeClasse
        self.nomeOrdem = nomeOrdem


class Familia(Ordem):
    def __init__(self,nomeReino, nomeFilo, nomeClasse, nomeOrdem,nomeFamilia):
        super().__init__(nomeFamilia, nomeFilo, nomeClasse, nomeOrdem)
        self.nomeReino = nomeReino
        self.nomeReino = nomeFilo
        self.nomeClasse = nomeClasse
        self.nomeOrdem = nomeOrdem
        self.nomeFamilia = nomeFamilia

class Genero(Familia):
    def __init__(self,nomeReino, nomeFilo, nomeClasse, nomeOrdem,nomeFamilia, nomeGenero,):
        super().__init__(nomeGenero, nomeFilo, nomeClasse, nomeOrdem,nomeFamilia)
        self.nomeReino = nomeReino
        self.nomeReino = nomeFilo
        self.nomeClasse = nomeClasse
        self.nomeOrdem = nomeOrdem
        self.nomeFamilia = nomeFamilia
        self.nomeGenero = nomeGenero

    # def __str__(self):
    #     return f"{self.nome}, {self.especies}"

class Especie(Genero):
    def __init__(self,nomeReino, nomeFilo, nomeClasse, nomeOrdem, nomeEspecie, nomeFamilia, nomeGenero,  caracteristicas):
        super().__init__(nomeEspecie,nomeFilo, nomeClasse, nomeOrdem, nomeFamilia,nomeGenero)
        self.nomeReino = nomeReino
        self.nomeReino = nomeFilo
        self.nomeClasse = nomeClasse
        self.nomeOrdem = nomeOrdem
        self.nomeFamilia = nomeFamilia
        self.nomeGenero = nomeGenero
        self.nomeEspecie = nomeEspecie
        self.caracteristicas = caracteristicas

    def __str__(self):
        return f"{self.nomeEspecie}, {self.caracteristicas}, {self.nomeReino},{self.nome},{self.nomeFilo},{self.nomeFilo},{self.nomeClasse},{self.nomeClasse},{self.nomeOrdem},{self.nomeOrdem},{self.nomeEspecie},{self.nomeEspecie},{self.nomeFamilia},{self.nomeFamilia},{self.nomeGenero},{self.nomeGenero}"
