import os

DB_NAME = os.environ.get("DB_NAME", None)
DB_USER = os.environ.get("DB_USER", None)
DB_HOST = os.environ.get("DB_HOST", None)
DB_PORT = os.environ.get("DB_PORT", 5432)
DB_PASSWORD = os.environ.get("DB_PASSWORD", None)
