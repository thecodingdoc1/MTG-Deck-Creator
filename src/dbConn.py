import psycopg2
import os
from dotenv import load_dotenv
from psycopg2 import sql

load_dotenv()

DB_HOST = "localhost"
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_PORT = os.getenv("DB_PORT")

try:
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )
    cursor = conn.cursor()

    print(f"success '{DB_NAME}', ''{DB_USER}'")

    create_table_query = """
        CREATE TABLE IF NOT EXISTS cards
        (
            scryfall_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            mana_cost VARCHAR(255),
            type_line VARCHAR(255),
            oracle_text TEXT,
            colors VARCHAR(20), 
            power VARCHAR(10),
            toughness VARCHAR(10),
            legalities JSONB
        );
        """
    
    cursor.execute(create_table_query)
    conn.commit()
    print("Table created")

    # retrieve data from skryfall

except Exception as error:
    print(f"Error connecting to db, creating table, importing data {error}")
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Conn closed")
    