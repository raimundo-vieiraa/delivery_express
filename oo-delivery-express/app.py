from modelos.restaurante import Restaurante
restaurante_praca=Restaurante('Praça','Goumert')
restaurante_mexicano=Restaurante('Mexican Food','Mexicana')
restaurante_japones=Restaurante('Japa','Japonesa')
restaurante_praca.receber_avaliacao('Rai',10)
restaurante_praca.receber_avaliacao('Matheus',7)
restaurante_praca.receber_avaliacao('Thigas',10)
restaurante_praca.receber_avaliacao('Marcelo',8)
restaurante_mexicano.alternar_estado()
def main():
    Restaurante.listar_restaurantes()



if __name__ == '__main__':
    main()