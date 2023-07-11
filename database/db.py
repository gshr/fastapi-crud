from sqlmodel import SQLModel,Field,create_engine,Session
from typing import Optional

class User(SQLModel,table=True):
    id: int = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
    
    

sqlite_file_name = "database1.db"  # 
sqlite_url = f"sqlite:///{sqlite_file_name}"  

engine = create_engine(sqlite_url)  


def create_db_and_tables():  # 
    SQLModel.metadata.create_all(engine)
    
    
    
def db_session():
    try:
        db = Session(engine)
        yield db
    finally:
        db.close()
    

    