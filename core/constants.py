# настройка send_mail
from datetime import timedelta

from decouple import config

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", "False") == "True"

POSTGRES_DB = config("POSTGRES_DB", "django")
POSTGRES_USER = config("POSTGRES_USER", "django")
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", "")
DB_HOST = config("DB_HOST", "")
DB_PORT = config("DB_PORT", 5432)
