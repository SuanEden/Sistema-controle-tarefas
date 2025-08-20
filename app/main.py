from app.routes.tasks import coleta_dados_demanda, autenticacao_usuario
from fastapi import FastAPI

app = FastAPI()

@app.get("/a")
def root():
    teste_1 = autenticacao_usuario()
    teste_2 = coleta_dados_demanda()
    return teste_1, teste_2
