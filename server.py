from fastapi import FastAPI, Depends, HTTPException
import uvicorn
from sqlalchemy.orm import Session
from schema.schemas import Aluno
from infra.sqlalchemy.repositories.alunos import RepositorioAluno
from infra.sqlalchemy.config.database import get_db, create_db

create_db()
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/alunos")
def criar_aluno(aluno:Aluno, db: Session = Depends(get_db)):
    aluno_criado = RepositorioAluno(db).create(aluno)
    return{"message":"aluno ok"}

@app.get("/alunos")
def listar_alunos(db: Session = Depends(get_db)): 
    alunos = RepositorioAluno(db).read()
    return alunos

@app.get('/alunos/{id_aluno}', response_model=Aluno)
def busca_por_id(id_aluno:int, db:Session = Depends(get_db)):
    aluno_localizado = RepositorioAluno(db).read_by_id(id_aluno=id_aluno)
    if not aluno_localizado:
        raise HTTPException(status_code=404, detail=f"aluno com o id {id_aluno} não existe")
    return aluno_localizado

@app.put("/alunos/{id_aluno}")
def atualizar_aluno(id_aluno: int, aluno: Aluno, db: Session = Depends(get_db)):
    novos_dados = {
        "nome": aluno.nome,
        "idade": aluno.idade,
        "nota_primeiro_semestre": aluno.nota_primeiro_semestre,
        "nota_segundo_semestre": aluno.nota_segundo_semestre,
        "nome_professor": aluno.nome_professor,
        "numero_sala": aluno.numero_sala
    }
    aluno_atualizado = RepositorioAluno(db).update(id_aluno, novos_dados)
    if aluno_atualizado:
        return {"message":"aluno atualizado com sucesso"}
    else:
        raise HTTPException(status_code=404, detail=f"Aluno com id {id_aluno} não encontrado")

@app.delete("/alunos/{id_aluno}")
def remover_aluno(id_aluno: int, db: Session = Depends(get_db)):
    aluno_removido = RepositorioAluno(db).delete(id_aluno)
    if aluno_removido:
        return {"message": f"Estudante de ID {id_aluno} foi excluído com sucesso"}
    else:
        raise HTTPException(status_code=404, detail=f"Estudante com id {id_aluno} não encontrado")
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))