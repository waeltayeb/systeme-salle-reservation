import os

MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "rootpassword")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_DB = os.getenv("MYSQL_DB", "salle_db")

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
