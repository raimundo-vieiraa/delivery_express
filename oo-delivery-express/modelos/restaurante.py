"""
A classe Restaurante representa um restaurante dentro de um sistema de delivery. Ela foi projetada para armazenar informações como:
Nome
-Categoria
-Status de atividade
-Avaliações

Além disso, implementa comportamentos úteis tanto para a exibição quanto para a manipulação dos dados dos restaurantes.
"""
from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
class Restaurante:
    restaurantes=[]
    def __init__(self, nome, categoria):
        """
        Método construtor do código, com:
        -Nome
        -Categoria
        -Atividade
        -Avaliação
        -Cardapio
        """
        self._nome=nome.title() #   .title() A primeira letra fica maiuscula.
        self._categoria=categoria.upper() #   .upper A palavra toda fica maiuscula.
        self._ativo=False
        self._avaliacao=[]
        self._cardapio=[]
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        """
        Função str criada para retorna uma string para cada restaurante.
        """
        return f'| Nome: {self._nome.ljust(15)} | Categoria: {self._categoria.ljust(15)} | Status: {self.ativo}|'
    @classmethod
    def listar_restaurantes(cls):
        """
        Essa função tem o objetivo de listar todos os restaurantes cadastrados.
        """
        print(f'| {'Nome do Restaurante'.ljust(25)} | {'Categoria do Restaurante'.ljust(25)} | {'Avaliação'.ljust(20)} | {'Status do Restaurante'.ljust(25)} |')
        for restaurante in cls.restaurantes:
            print(f'| {restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(20)} |{restaurante.ativo.ljust(25)} |')
    @property
    def ativo(self):
        """
        Essa função tem o objetivo de mudar o icone dos status do restaurante.
        """
        return '✅'if self._ativo else '❎'

    def alternar_estado(self):
        """
        Essa função tem o objetivo de alterna o estado de atividade do restaurante.
        """
        self._ativo= not self._ativo
    def receber_avaliacao(self,cliente,nota):
        """
        Essa função tem o objetivo de receber a avaliação do clientes
        """
        if 0 < nota < 5:
            avaliacao=Avaliacao(cliente,nota)
            self._avaliacao.append(avaliacao)
    @property
    def media_avaliacao(self):
        """
        Essa função tem o objetivo de fazer o calculo para se obter a de todas as avaliações.
        """
        if not self._avaliacao:
            return '-'
        soma_nota=sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_nota=len(self._avaliacao)
        media=round(soma_nota/quantidade_nota, 1)
        return media
    
    def add_no_cardapio(self,item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)
        
    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}:\n')
        for i,item in enumerate(self._cardapio,start=1):
            if hasattr(item,'descricao_prato'):
                msg_prato=f'| {i}. Nome: {item._nome.ljust(20)} | Preço: R${str(item._preco).ljust(5)} |\n|     -Descrição: {item.descricao_prato.ljust(30)} |\n'
                print(msg_prato)
            elif hasattr(item,'tamanho'):
                msg_bebida=f'| {i}. Nome: {item._nome.ljust(20)} | Preço: R${str(item._preco).ljust(5)} |\n|     -Tamanho: {item.tamanho.ljust(32)} |\n'
                print(msg_bebida)
            else:
                msg_sobremesa=f'| {i}. Nome: {item._nome.ljust(20)} | Preço: R${str(item._preco).ljust(5)} |\n|     -Tamanho: {item.descricao_sobremesa.ljust(32)} |\n'
                print(msg_sobremesa)