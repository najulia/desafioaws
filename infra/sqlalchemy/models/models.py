from sqlalchemy import Column, Integer, Float, String
from infra.sqlalchemy.config.database import Base

class Aluno(Base):
    
    __tablename__ = 'alunos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(200),  nullable=False)
    idade = Column(Integer)
    nota_primeiro_semestre = Column(Float) 
    nota_segundo_semestre =  Column(Float) 
    nome_professor = Column(String(200),  nullable=False)
    numero_sala = Column(Integer)