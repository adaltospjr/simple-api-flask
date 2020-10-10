from dotenv import load_dotenv
import psycopg2 as psycopg
from os import getenv

load_dotenv("/home/adalto/Documentos/github/simple-api-flask/.env")


def connect():
    # Connect to your postgres DB
    conn = psycopg.connect(
        database=getenv("DB_DATABASE"),
        user=getenv("DB_USER"),
        password=getenv("DB_PASSWORD"),
        host=getenv("DB_HOST"),
        port=getenv("DB_PORT"),
    )

    return conn


def select():
    # Execute a query
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    for row in records:
        print(f"id:{row[0]}")
        print(f"nome:{row[1]}")
        print(f"sobrenome:{row[2]}")
        print(f"data de nascimento:{row[3]}")
        print(f"altura:{row[4]}")


def insert(values):
    conn = connect()
    cursor = conn.cursor()

    query = f"""
        INSERT INTO usuarios(
            nome,
            sobrenome,
            data_nasc,
            altura
        )
        VALUES(
            '{values[0]}',
            '{values[1]}',
            '{values[2]}',
            '{values[3]}'
        )
        """
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()


def update(nome):
    conn = connect()
    cursor = conn.cursor()

    query = f"""
        UPDATE
        usuarios
        SET
        nome = '{nome}'
        WHERE
        id =11;
    """
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()


def delete(id):
    conn = connect()
    cursor = conn.cursor()
    query = f"""
    delete
    from
    usuarios
    where
    id = {id}
    """
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()


data = ["George", "Rufino", "1996-01-01", 1.75]

# delete(id=12)
# update(nome="Ades")
# select()
