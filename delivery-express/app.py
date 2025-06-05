import os

restaurantes=[]

def exibir_nome_do_programa():
    """
    Essa função tem o objetivo de mostrar o nome da aplicação.

    OutPuts:
    - Retorna o nome da aplicação.
    """
    print("""
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─████████████───██████████████─██████─────────██████████─██████──██████─██████████████─████████████████───████████──████████─
─██░░░░░░░░████─██░░░░░░░░░░██─██░░██─────────██░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░██──██░░░░██─
─██░░████░░░░██─██░░██████████─██░░██─────────████░░████─██░░██──██░░██─██░░██████████─██░░████████░░██───████░░██──██░░████─
─██░░██──██░░██─██░░██─────────██░░██───────────██░░██───██░░██──██░░██─██░░██─────────██░░██────██░░██─────██░░░░██░░░░██───
─██░░██──██░░██─██░░██████████─██░░██───────────██░░██───██░░██──██░░██─██░░██████████─██░░████████░░██─────████░░░░░░████───
─██░░██──██░░██─██░░░░░░░░░░██─██░░██───────────██░░██───██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───────████░░████─────
─██░░██──██░░██─██░░██████████─██░░██───────────██░░██───██░░██──██░░██─██░░██████████─██░░██████░░████─────────██░░██───────
─██░░██──██░░██─██░░██─────────██░░██───────────██░░██───██░░░░██░░░░██─██░░██─────────██░░██──██░░██───────────██░░██───────
─██░░████░░░░██─██░░██████████─██░░██████████─████░░████─████░░░░░░████─██░░██████████─██░░██──██░░██████───────██░░██───────
─██░░░░░░░░████─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░██───████░░████───██░░░░░░░░░░██─██░░██──██░░░░░░██───────██░░██───────
─████████████───██████████████─██████████████─██████████─────██████─────██████████████─██████──██████████───────██████───────
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─████████──████████─██████████████─████████████████───██████████████─██████████████─██████████████─
─██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████─████░░██──██░░████─██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
─██░░██───────────██░░░░██░░░░██───██░░██──██░░██─██░░██────██░░██───██░░██─────────██░░██─────────██░░██─────────
─██░░██████████───████░░░░░░████───██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
─██░░░░░░░░░░██─────██░░░░░░██─────██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████───████░░░░░░████───██░░██████████─██░░██████░░████───██░░██████████─██████████░░██─██████████░░██─
─██░░██───────────██░░░░██░░░░██───██░░██─────────██░░██──██░░██─────██░░██─────────────────██░░██─────────██░░██─
─██░░██████████─████░░██──██░░████─██░░██─────────██░░██──██░░██████─██░░██████████─██████████░░██─██████████░░██─
─██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░██─────────██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████████████─████████──████████─██████─────────██████──██████████─██████████████─██████████████─██████████████─
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────
      """)

def exibir_opçoes_do_programa():
    """
    Essa função tem o objetivo de exibir as opções da aplicação.
    
    OutPuts:
    - Retorna as opções da aplicação.
    """
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar ou desativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    """
    Essa função tem o objetivo de finalizar a aplicação.

    OutPuts:
    - Retorna exibir_subtitulo()
    """
    exibir_subtitulo('Finalizando operação')

def opcao_invalida():
    """
    Essa função tem o objetivo de retorna ao menu principal, caso algo de errado na aplicação.

    OutPuts:
    - Retorna retorne_ao_menu_principal()
    """
    print('Opção invalida!\n')
    retorne_ao_menu_principal()

def exibir_subtitulo(texto):
    """Essa função tem o objetivo de exibir o subtitulo de cada função.
    
    OutPuts:
    - Retorna o subtitulo de maneira mais organizada.
    """
    os.system('cls')
    linha='-'*(len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    """
    Essa função tem o objetivo de casdastrar um novo restaurante.

    Inputs: 
    - Nome do restaurante.
    - Categoria do restaurante.    

    OutPuts:
    - Adiciona um novo restaurante a lista restaurantes.
    """
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante=input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante=input('Digite a categoria do seu restaurante: ')
    dados_do_restaurante={'nome':nome_do_restaurante,'categoria':categoria_do_restaurante, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso!!\n')
    retorne_ao_menu_principal()

def lista_de_restaurantes():
    """
    Essa função tem o objetivo de mostrar os restaurantes cadastrados.

    OutPuts:
    - Retorna o nome do restaurante / categoria / status do restaurante.
    """
    exibir_subtitulo('Restaurantes Cadastrados')
    print(f'{'Nome: '.ljust(22)} | {'Categoria: '.ljust(21)}| Atividade:')
    for dados_do_restaurante in restaurantes:
        nome=dados_do_restaurante['nome']
        categoria=dados_do_restaurante['categoria']
        ativo='Ativado' if dados_do_restaurante['ativo'] else 'Desativado'
        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    retorne_ao_menu_principal()

def alterna_atividade_restaurante():
    """
    Essa função tem o objetivo de alterar o status de atividade do restaurante.
    
    Inputs:
    - Alterar o status do restaurante.
    
    OutPuts:
    - Retorna a mudança de status do restaurante.
    """
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante_ativar=input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado=False
    for restaurante in restaurantes:
        if nome_restaurante_ativar==restaurante['nome']:
            restaurante_encontrado=True
            restaurante['ativo']=not restaurante['ativo']
            mensagem=f'O restaurante {nome_restaurante_ativar} foi ativado com sucesso.' if restaurante['ativo'] else f'O restaurante {nome_restaurante_ativar} foi desativado com sucesso.'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
    retorne_ao_menu_principal()
    
def retorne_ao_menu_principal():
    """
    Essa função tem o objetivo de voltar ao menu principal.

    Inputs:
    - Digita qualquer tecla para voltar ao menu.

    OutPuts:
    - Retorna o main()
    """
    input('\nDigite qualquer tecla para voltar ao menu principal: ')
    main()

def escolher_opcao():
    """
    Essa função tem o objetivo de escolher uma opção para continuar.

    Inputs:
    - Escolher uma opção.

    OutPuts:
    - Opções que podem ser acessadas: Cadastrar novo restaurante | Mostra lista de restaurantes cadastrados | Ativar ou desativar um restaurante cadastrado | Finalizar a operação.
    """
    try:
        opcao_escolhida=int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                lista_de_restaurantes()
            case 3:
                alterna_atividade_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    """
    Essa função tem o objetivo de retorna a main principal.
    """
    os.system ('cls')
    exibir_nome_do_programa()
    exibir_opçoes_do_programa()
    escolher_opcao()
if __name__ == '__main__':
    main()