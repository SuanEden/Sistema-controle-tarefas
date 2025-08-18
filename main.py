from funcoes import coleta_dados_demanda, autenticacao_usuario

def main():
    nome = autenticacao_usuario()
    coleta_dados_demanda()
    print(nome)
    
if __name__ == "__main__":
    main()