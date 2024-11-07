import json
import os

from dotenv import find_dotenv
from dotenv import load_dotenv


if not load_dotenv(find_dotenv("/work/config/env.file")):
    load_dotenv(find_dotenv())


class Config:
    ENV = "production"
    PROJECT_NAME = "fastapi-best-practices"
    APP_PORT = int(os.getenv("APP_PORT", 8080))
    APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
    APP_WORKERS = int(os.getenv("APP_WORKERS", 1))
    SEND_LOGS_TO_GRAYLOG: bool = os.getenv("SEND_LOGS_TO_GRAYLOG", "False").lower() in (
        "true",
        "1",
    )
    GRAYLOG_HOST = os.getenv("GRAYLOG_HOST", "ml-dev1.dohod.local")
    GRAYLOG_PORT = int(os.getenv("GRAYLOG_PORT", 12201))

    #DATABASE

    POSTGRESQL_DSN = os.getenv("POSTGRESQL_DSN", "postgresql+psycopg2://lil_antoha_big_smoke:lil_antoha_big_smoke@db:5432/PDP")

    #AUTH

    SECRET_KEY=os.getenv("SECRET_KEY", "gV64m9aIzFG4qpgVphvQbPQrtAO0nM-7YwwOvu0XPt5KJOjAy4AfgLkqJXYEt")
    ALGORITHM=os.getenv("ALGORITHM", "HS256")

    #MAIL

    SMTP_SERVER = os.getenv("SMTP_HOST",  "smtp.yandex.ru")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "465"))
    SMTP_USER = os.getenv("SMTP_USER", "a.pdp@yandex.ru")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "curteicktvsbkgga")
    CODES = {}




class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True


class TestingConfig(Config):
    ENV = "testing"


class StagingConfig(Config):
    ENV = "staging"


class ProductionConfig(Config):
    ENV = "production"
    IS_PRODUCTION = True


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "staging": StagingConfig,
    "default": DevelopmentConfig,
}

env = os.getenv("ENV", "production")

CONFIG: Config = config[env]()

def get_auth_data():
    return {"secret_key": CONFIG.SECRET_KEY, "algorithm": CONFIG.ALGORITHM}
