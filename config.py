from pydantic import BaseSettings

class Setting (BaseSettings):
    db_name : str
    db_password : str
    db_host : str
    db_user : str
    db_port : int
    database_url: str
    
    class Config : 
        env_file = ".env"
    
settings = Setting()