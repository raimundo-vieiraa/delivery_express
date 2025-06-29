"""
Arquivo principal que instancia objetos da classe Restaurante,
executa algumas operações básicas (como receber avaliações e alterar estado)
e chama a listagem dos restaurantes.

Serve como ponto de entrada para demonstrar o funcionamento do módulo modelos.restaurante.
"""

from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa
restaurante_praca=Restaurante('Praça','Goumert')
restaurante_mexicano=Restaurante('Mexican Food','Mexicana')
restaurante_japones=Restaurante('Japa','Japonesa')

bebida_suco=Bebida('Suco de Melancia',9.0,'Grande')
bebida_suco.aplicar_desconto()
prato_paozinho=Prato('Pãozinho',2.0,'O melhor da região!')
prato_paozinho.aplicar_desconto()
sobremesa_pudim=Sobremesa('Pudim',10.0,'O mais cremoso!')
sobremesa_pudim.aplicar_desconto()
restaurante_praca.add_no_cardapio(bebida_suco)
restaurante_praca.add_no_cardapio(prato_paozinho)
restaurante_praca.add_no_cardapio(sobremesa_pudim)
restaurante_mexicano.alternar_estado()
def main():
    restaurante_praca.exibir_cardapio



if __name__ == '__main__':
    main()