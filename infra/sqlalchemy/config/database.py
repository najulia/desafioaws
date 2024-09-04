from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql:///./alunos.db"
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:banco123@localhost:3306/alunos"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_connection():
    try:
        with engine.connect() as connection:
            print("Conexão bem-sucedida!")
    except Exception as e:
        print(f"Erro na conexão: {e}")

test_connection()