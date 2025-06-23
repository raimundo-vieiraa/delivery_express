"""
Arquivo principal que instancia objetos da classe Restaurante,
executa algumas operações básicas (como receber avaliações e alterar estado)
e chama a listagem dos restaurantes.

Serve como ponto de entrada para demonstrar o funcionamento do módulo modelos.restaurante.
"""

from modelos.restaurante import Restaurante
restaurante_praca=Restaurante('Praça','Goumert')
restaurante_mexicano=Restaurante('Mexican Food','Mexicana')
restaurante_japones=Restaurante('Japa','Japonesa')
restaurante_praca.receber_avaliacao('Rai',10)
restaurante_praca.receber_avaliacao('Matheus',2)
restaurante_praca.receber_avaliacao('Thigas',7.5)
restaurante_praca.receber_avaliacao('Marcelo',10)
restaurante_mexicano.alternar_estado()
def main():
    Restaurante.listar_restaurantes()



if __name__ == '__main__':
    main()