import psycopg2 as pg
from psycopg2 import Error
import os
from dotenv import load_dotenv

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")

def start_conn():
    try:
        conect = pg.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT,
            database="servidor_do_becario_database")

        print("Conectado com sucesso!")
    except Error as e:
        print(f"Não foi possível conectar ao banco de dados: {e}")

    return conect

def finish_conn(conect):
    if conect:
        conect.close()