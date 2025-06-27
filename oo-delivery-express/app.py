"""
Arquivo principal que instancia objetos da classe Restaurante,
executa algumas operações básicas (como receber avaliações e alterar estado)
e chama a listagem dos restaurantes.

Serve como ponto de entrada para demonstrar o funcionamento do módulo modelos.restaurante.
"""

from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
restaurante_praca=Restaurante('Praça','Goumert')
restaurante_mexicano=Restaurante('Mexican Food','Mexicana')
restaurante_japones=Restaurante('Japa','Japonesa')

bebida_suco=Bebida('Suco de Melancia',9.0,'Grande')
prato_paozinho=Prato('Pãozinho',2.0,'O melhor da região')
restaurante_praca.add_no_cardapio(bebida_suco)
restaurante_praca.add_no_cardapio(prato_paozinho)
restaurante_mexicano.alternar_estado()
def main():
    print(bebida_suco)
    print(prato_paozinho)



if __name__ == '__main__':
    main()