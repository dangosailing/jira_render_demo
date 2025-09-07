import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

connection_str=os.getenv("EXTERNAL_CONN_STR", "FAILED_IMPORT_STR")

if connection_str == "FAILED_IMPORT_STR":
    print("Failed to import connection string from env")
else: 
    conn = psycopg2.connect(connection_str)
    cursor = conn.cursor()
    cursor.execute("SELECT NOW();")
    print(cursor.fetchone())
    cursor.close()
    conn.close()
