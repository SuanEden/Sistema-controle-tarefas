from funcoes import coletaDadosDemanda, autenticacaoUsuario

def main():
    nome = autenticacaoUsuario()
    coletaDadosDemanda()
    print(nome)
    
if __name__ == "__main__":
    main()