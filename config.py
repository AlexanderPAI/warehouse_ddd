from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Main config"""

    # db
    postgres_user: str = Field(default="", title="Postgres user")
    postgres_password: str = Field(default="", title="Postgres password")
    postgres_host: str = Field(default="", title="Postgres host")
    postgres_port: int = Field(default="", title="Postgres port")
    postgres_db: str = Field(default="", title="Postgres db")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


cfg = Settings()
