class Restaurante:
    nome=''
    categoria=''
    ativo=False

restaurante_praca=Restaurante()
restaurante_praca.nome='Praça'
restaurante_praca.categoria='Italiana'
restaurante_pizza=Restaurante()
restaurante_pizza.nome='Pizza Place'
restaurante_pizza.categoria='Fast Food'
restaurante_pizza.ativo=True
restaurantes=[restaurante_praca]
print(f'Nome: {restaurante_praca.nome} | Categoria: {restaurante_praca.categoria} | Status: {restaurante_praca.ativo}')
if restaurante_praca.ativo==True:
    print(f'O restaurante {restaurante_praca.nome} está ativo.')
else:
    print(f'O restaurante {restaurante_praca.nome} está inativo.')