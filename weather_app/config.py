from functools import lru_cache

from pydantic import BaseSettings

class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./weather.db"   

@lru_cache
def get_settings() -> Settings:
    settings = Settings()    
    return settings