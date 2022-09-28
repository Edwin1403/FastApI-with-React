from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

try:
    dbURL="postgresql://Cyril:Edwin123@localhost/formapi" 
    engine=create_engine(dbURL)
    local=sessionmaker(autoflush=False,autocommit=False,bind=engine)
    print("success")
except Exception as error:
    print('db error',error)    

base=declarative_base()

def get_db():
    db=local()
    try:
        yield db
    finally:
        db.close()    
