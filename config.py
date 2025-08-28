import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY" , "wcc@2023")
    SQLALCHEMY_DATABASE_UEL = os.getenv("DATABASE_URL" , "postgresql://postgresa:SECRET_KEY@127.0.0.1:5432/tarefas_3b")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    