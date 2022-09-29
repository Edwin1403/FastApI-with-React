from pydantic import BaseSettings

class Settings (BaseSettings):
    db_name : str
    db_password : str
    db_host : str
    db_username : str
    db_port : int
    database_url: str

    class Cofig : 
        env_file = ".env"
    
settings = Settings()