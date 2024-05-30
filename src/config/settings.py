from pydantic import Field
from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    host: str = Field(default="localhost", env="POSTGRES_HOST")
    por5t: int = Field(default=5432, env="POSTGRES_PORT")
    user: str = Field(default="postgres", env="POSTGRES_USER")
    password: str = Field(default="postgres", env="POSTGRES_PASSWORD")
    database: str = Field(default="postgres", env="POSTGRES_DB")


class AppSettings(BaseSettings):
    db: DatabaseSettings = DatabaseSettings()
    title: str = "Alter Jira"
    version: str = "0.1.0"
