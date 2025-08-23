"""
id = int (Chave primarea, Criada pelo sistema)
user = string (Max = 10, min 5)
senha = int (Max = 10, min 5)
"""
from sqlmodel import SQLModel, Field

class User(SQLModel, table = True):
    id: int = Field(primary_key = True, defalte = None)
    username: str = Field(..., max_length = 10, min_length = 5, description = "Nome do Usuario")
    senha: str = Field(..., max_length = 10, min_length = 5, description = "Senha do Usuario")