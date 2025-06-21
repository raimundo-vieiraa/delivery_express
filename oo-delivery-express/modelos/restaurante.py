class Restaurante:
    restaurantes=[]
    def __init__(self, nome, categoria):
        self._nome=nome.title() #   .title() A primeira letra fica maiuscula.
        self._categoria=categoria.upper() #   .upper A palavra toda fica maiuscula.
        self._ativo=False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'| Nome: {self._nome.ljust(15)} | Categoria: {self._categoria.ljust(15)} | Status: {self.ativo}|'
    @classmethod
    def listar_restaurantes(cls):
        print(f'| {'Nome do Restaurante'.ljust(25)} | {'Categoria do Restaurante'.ljust(25)} | {'Status do Restaurante'.ljust(25)} |')
        for restaurante in cls.restaurantes:
            print(f'| {restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} |{restaurante.ativo.ljust(25)} |')
    @property
    def ativo(self):
        return '✅'if self._ativo else '❎'

    def alternar_estado(self):
        self._ativo= not self._ativo

restaurante_praca=Restaurante('Praça','Italiana')
restaurante_praca.alternar_estado()
restaurante_pizza=Restaurante('Pizza Express','Italiana')
Restaurante.listar_restaurantes()
