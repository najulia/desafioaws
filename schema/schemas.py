from pydantic import BaseModel

class Aluno(BaseModel):
    nome: str
    idade: int
    nota_primeiro_semestre: float 
    nota_segundo_semestre: float
    nome_professor: str
    numero_sala: int 

    class Config:
        orm_mode = True