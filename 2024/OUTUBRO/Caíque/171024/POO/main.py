# carro = {
#     "marca":"VolksWagen",
#     "modelo":"Fusca",
#     "cor":"Azul",
#     "ano":"1945"
# }

# print(carro.get("marca"))

class Car:
    def __init__(self, marca: str, modelo: str, ano: int):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano

    @property
    def marca(self):
        """Propriedade Marca"""
        return self._marca

    @marca.setter
    def marca(self, value):
        if(type(value) != str):
            raise TypeError('Tipo incorreto! Precisa ser uma String')
        if(len(value) <= 3):
            raise ValueError('Comprimento do Marca é muito curto')

        self._marca = value

    @marca.deleter
    def marca(self):
        self._marca = 'Carro'

    @property
    def modelo(self):
        """Propriedade modelo"""
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        if(type(value) != str):
            raise TypeError('Tipo incorreto! Precisa ser uma String')
        if(len(value) <= 3):
            raise ValueError('Comprimento do Modelo é muito curto')
        
        self._modelo = value

    @modelo.deleter
    def modelo(self):
        self._modelo = None
    
    @property
    def ano(self):
        """Propriedade ano"""
        return self._ano

    @ano.setter
    def ano(self, value):
        if(type(value) != int):
            raise TypeError('Tipo incorreto! Precisa ser uma Int')
        if(value <= 0):
            raise ValueError('Ano não pode ser menor que Zero')
        if(value > 2025):
            raise ValueError('Ano não pode ser maior que 2025')

        self._ano = value

    @ano.deleter
    def ano(self):
        self._ano = None
    
    def __str__(self) -> str:
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}'

cusca = Car('volkis', 'Fusção', 1945)
cusca.ano = 3000
print(cusca)

