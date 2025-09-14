import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from datetime import datetime

# 🔌 Connexion MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # change si tu utilises un autre utilisateur
        password="",        # ajoute le mot de passe si besoin
        database="cinephoria2"
    )

# 📌 Charger les options de la base
def charger_options():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Récupérer les cinémas
    cursor.execute("SELECT DISTINCT cinema FROM seances")
    cinemas = [row[0] for row in cursor.fetchall()]

    # Récupérer les séances
    cursor.execute("SELECT id, nom FROM seances")
    seances = {row[1]: row[0] for row in cursor.fetchall()}

    cursor.close()
    conn.close()
    return cinemas, seances

# 💾 Enregistrer l'incident
def enregistrer_incident():
    cinema = combo_cinema.get()
    seance = combo_seance.get()
    incident = combo_incident.get()

    if not cinema or not seance or not incident:
        messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs.")
        return

    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO incidents (cinema, seance, description, date_creation) VALUES (%s, %s, %s, %s)"
    values = (cinema, seance, incident, datetime.now())
    cursor.execute(sql, values)

    conn.commit()
    cursor.close()
    conn.close()

    messagebox.showinfo("Succès", "Incident enregistré avec succès !")

# 🎨 Interface graphique
app = tk.Tk()
app.title("Gestion des incidents - Cinephoria")
app.geometry("400x300")

# Charger les données pour les menus
cinemas, seances = charger_options()

# Menu déroulant Cinéma
tk.Label(app, text="Cinéma :").pack(pady=5)
combo_cinema = ttk.Combobox(app, values=cinemas, state="readonly")
combo_cinema.pack(pady=5)

# Menu déroulant Séance
tk.Label(app, text="Séance :").pack(pady=5)
combo_seance = ttk.Combobox(app, values=list(seances.keys()), state="readonly")
combo_seance.pack(pady=5)

# Menu déroulant Inc
