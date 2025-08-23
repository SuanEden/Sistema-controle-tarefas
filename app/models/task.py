"""
id_demanda -> int dado pelo banco 
título ->  script, obrigatorio, max 120 chars  
descrição -> string, opcional
due_date -> data, opcional
status -> string, valores possiveis: todo, soing, done
created_at -> datetime, gerado automaticamente
upgrated_at -> datetime, gerado automaticamente
"""
from sqlmodel import SQLModel, Field
from datetime import datetime
from sqlalchemy import ForeignKey
from emun import Enum

class Status(str, Enum):
    todo = "todo"
    doing = "doing"
    done = "done"

class Task(SQLModel, table = True):
    id_demanda: int = Field(primary_key = True, default = None)
    user_id: int = Field(..., foreign_key = "user.id")
    titulo: str = Field(..., max_length = 120, description = "Titulo da tarefa" )
    descricao: str = Field(default = None, nullable = True, description = "Descrição de terefa")
    due_date: datetime = Field(default_factory = datetime.utcnow, description = "Data de vencimentp da tarefa")
    status: Status = Field(..., default = Status.todo, description = "Status da tarefa: todo, doing ou done")
    updated_at: datetime = Field(default_factory  = datetime.utcnow, description = "Ultima atualização")