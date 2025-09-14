import mysql.connector

print("Test de connexion avec l'utilisateur 'dbuser'...")

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="dbuser",
        password="",
        database="cinephoria2"
    )
    print("✅ Connexion réussie avec l'utilisateur 'dbuser'!")
    
    # Test supplémentaire : vérifier les tables
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    print(f"Tables trouvées: {[table[0] for table in tables]}")
    
    conn.close()
except mysql.connector.Error as err:
    print(f"❌ Échec de connexion: {err}")