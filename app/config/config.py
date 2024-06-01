import os

class Settings():
    OPENAI_KEY: str
    MILVUS_HOST: str
    MILVUS_PORT: str

    class Config:
        env_file = ".env"

env = os.getenv("ENV", "dev")
if env == "prod":
    Settings.Config.env_file = ".env.prod"
else:
    Settings.Config.env_file = ".env.dev"

settings = Settings()
