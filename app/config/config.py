import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    OPENAI_KEY: str
    PINECONE_API_KEY: str
    PINECONE_INDEX_NAME: str

    class Config:
        env_file = ".env.dev"

env = os.getenv("ENV", "dev")
if env == "prod":
    Settings.Config.env_file = ".env.prod"
else:
    Settings.Config.env_file = ".env.dev"

settings = Settings()
