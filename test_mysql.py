import mysql.connector

print("Test de connexion MySQL...")

# Essai 1: sans mot de passe
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cinephoria2"
    )
    print("✅ Connexion réussie avec mot de passe vide!")
    conn.close()
except mysql.connector.Error as err:
    print(f"❌ Échec avec mot de passe vide: {err}")

# Essai 2: avec mot de passe "root"
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="cinephoria2"
    )
    print("✅ Connexion réussie avec mot de passe 'root'!")
    conn.close()
except mysql.connector.Error as err:
    print(f"❌ Échec avec mot de passe 'root': {err}")