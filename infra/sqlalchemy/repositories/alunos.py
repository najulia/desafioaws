from sqlalchemy.orm import Session, session
from schema import schemas
from infra.sqlalchemy.models import models
from sqlalchemy import update

class RepositorioAluno():

    def __init__(self, db:Session):
        self.db = db

    def create(self, aluno:schemas.Aluno):
        db_aluno = models.Aluno(
            nome=aluno.nome,
            idade=aluno.idade, 
            nota_primeiro_semestre = aluno.nota_primeiro_semestre, 
            nota_segundo_semestre = aluno.nota_segundo_semestre, 
            nome_professor = aluno.nome_professor,
            numero_sala = aluno.numero_sala, 
        )
        self.db.add(db_aluno)
        self.db.commit()
        self.db.refresh(db_aluno)
        return db_aluno

    def read(self):
        return self.db.query(models.Aluno).all()

    def read_by_id(self, id_aluno:int):
        return self.db.query(models.Aluno).filter(models.Aluno.id==id_aluno).first()

    def update(self, id_aluno:int, novos_dados:dict):
        aluno_atualizado = self.db.query(models.Aluno).filter(models.Aluno.id == id_aluno).first()
        for chave, valor in novos_dados.items():
            setattr(aluno_atualizado, chave, valor)
        self.db.commit()
        return aluno_atualizado
    
    def delete(self, id_aluno: int):
        aluno = self.db.query(models.Aluno).filter(models.Aluno.id == id_aluno).first()
        if aluno:
            self.db.delete(aluno)
            self.db.commit()
            return aluno
        else:
            return None