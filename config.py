from pydantic import BaseSettings

class Setting (BaseSettings):
    db_url: str
    
    class Config : 
        env_file = ".env"
    
settings = Setting()