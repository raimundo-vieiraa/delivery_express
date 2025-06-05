class Restaurante:
    restaurantes=[]
    def __init__(self, nome, categoria):
        self.nome=nome
        self.categoria=categoria
        self.ativo=False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'|Nome: {self.nome.ljust(15)} | Categoria: {self.categoria.ljust(15)} | Status: {self.ativo}|'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'| Nome: {restaurante.nome.ljust(15)} | Categoria: {restaurante.categoria.ljust(15)} | Status: {restaurante.ativo} |')
restaurante_praca=Restaurante('Praça','Italiana')
restaurante_pizza=Restaurante('Pizza Express','Italiana')
Restaurante.listar_restaurantes()