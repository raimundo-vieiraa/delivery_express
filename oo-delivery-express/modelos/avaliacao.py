"""
A classe Avaliação vai representar as notas dos clientes, com:
-Nome
-Nota do cliente
"""
class Avaliacao:
    def __init__(self,cliente,nota):
        self._cliente=cliente
        self._nota=nota