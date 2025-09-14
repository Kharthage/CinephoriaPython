# test_connexion.py
import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cinephoria2",
        port=3306
    )
    print("✅ Connexion à la base de données réussie!")
    
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM cinema")
    result = cursor.fetchone()
    print(f"Nombre de cinémas dans la base: {result[0]}")
    
    cursor.close()
    conn.close()
    
except mysql.connector.Error as err:
    print(f"❌ Erreur de connexion: {err}")