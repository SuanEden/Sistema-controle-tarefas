import sys
def coleta_dados_demanda():
    """
    Coleta as informações da demanda
    """
    usuario =  input('Qual o criador da demanda:')
    titulo = input('Qual a demanda? ')
    data_vencimento = input('Qual a data de vencimento da demanda? ')
    descricao = input('Descrição da Demanda: ')

    return usuario, titulo, data_vencimento, descricao


def autenticacao_usuario():
    """
    Altentica Usuario e senha
    """
    usuario_resistrado = 'Suan'
    senha_resistrada = '1831'
    limite_tentativas = 2
    tentativa = 0
    usuario = input('Qual o nome do Usuario:')
    while(usuario_resistrado != usuario):
        usuario = input('Usuario incorreto, tente novamente \nnome do Usuario:')
        tentativa+=1
        
        if(tentativa>=limite_tentativas):
            print('Você exedeu o limete de tentativas')
            sys.exit(f'O sistema se encerrou por exeder o limite de tentativas')

    senha = input(f'Olá {usuario}, qual a sua senha: ')
    while(senha_resistrada != senha):
        senha = input('Senha incorreta, tente novamente \nQual a sua Senha:')
        tentativa+=1
        
        if(tentativa>=limite_tentativas):
            print('Você exedeu o limete de tentativas')
            sys.exit(f'O sistema se encerrou por exeder o limite de tentativas')
    print(f'Seja bem vindo {usuario}, como está?')
    return usuario, senha

