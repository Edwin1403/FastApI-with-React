from pydantic import BaseSettings

class Settings (BaseSettings):
    db_name : str
    db_password : str
    db_host : str
    db_username : str

    class Cofig : 
        env_file = ".env"
    
settings = Settings()