import os
# from pydantic_settings import BaseSettings

class Settings():
    OPENAI_KEY: str

    class Config:
        env_file = ".env"

env = os.getenv("ENV", "dev")
if env == "prod":
    Settings.Config.env_file = ".env.prod"
else:
    Settings.Config.env_file = ".env.dev"

settings = Settings()
