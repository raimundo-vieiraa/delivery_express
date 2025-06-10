class Restaurante:
    restaurantes=[]
    def __init__(self, nome, categoria):
        self.nome=nome.title() #   .title() A primeira letra fica maiuscula.
        self.categoria=categoria.upper() #   .upper A palavra toda fica maiuscula.
        self._ativo=False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'| Nome: {self.nome.ljust(15)} | Categoria: {self.categoria.ljust(15)} | Status: {self.ativo}|'
    
    def listar_restaurantes():
        print(f'| {'Nome do Restaurante'.ljust(25)} | {'Categoria do Restaurante'.ljust(25)} | {'Status do Restaurante'.ljust(25)} |')
        for restaurante in Restaurante.restaurantes:
            print(f'| {restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} |{restaurante.ativo.ljust(25)} |')
    @property
    def ativo(self):
        return '✅'if self._ativo else '❎'



restaurante_praca=Restaurante('Praça','Italiana')
restaurante_pizza=Restaurante('Pizza Express','Italiana')
Restaurante.listar_restaurantes()
