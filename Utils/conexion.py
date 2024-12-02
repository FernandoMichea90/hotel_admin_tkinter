import mysql.connector

def conectar_db():
    """Conectar a la base de datos."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123",
        database="hotel_ecomusic"
    )   