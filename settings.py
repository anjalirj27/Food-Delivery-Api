from pydantic import BaseSettings

class Settings(BaseSettings):
    authjwt_secret_key: str = "wWdk0PzrENmpOGEUIZ_4rNK4xG3dXT1sA0Uyo8vFQfQ"  # generate your own!

    class Config:
        env_file = ".env"

settings = Settings()
