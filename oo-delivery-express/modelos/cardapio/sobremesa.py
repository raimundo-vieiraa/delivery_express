from modelos.cardapio.item_cardapio import ItemCardapio
class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, descricao_sobremesa):
        super().__init__(nome, preco)
        self.descricao_sobremesa=descricao_sobremesa
    
    def aplicar_desconto(self):
        self._preco-=(self._preco*0.07)