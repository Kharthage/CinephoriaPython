import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from datetime import datetime


import os
os.environ['LANG'] = 'en_US.UTF-8'

# Connexion à la base de données
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cinephoria2"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Erreur de connexion", f"Impossible de se connecter à la base de données:\n{err}")
        return None

# Charger les données depuis la base
def charger_donnees():
    conn = get_db_connection()
    if conn is None:
        return [], [], []
    
    cursor = conn.cursor(dictionary=True)
    
    # Charger les cinémas
    cursor.execute("SELECT id, nom FROM cinema")
    cinemas = [(row['id'], row['nom']) for row in cursor.fetchall()]
    
    # Charger les types d'équipements
    equipements = ["Siège", "Projecteur", "Éclairage", "Climatisation", "Écran", "Son", "Autre"]
    
    # Charger les statuts
    statuts = ["Signalé", "En cours", "Résolu", "Rejeté"]
    
    cursor.close()
    conn.close()
    
    return cinemas, equipements, statuts

# Charger les salles d'un cinéma
def charger_salles(event=None):
    cinema_id = combo_cinema.get().split(" - ")[0] if combo_cinema.get() else None
    
    if not cinema_id:
        return
    
    conn = get_db_connection()
    if conn is None:
        return
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT s.id, s.reference, c.nom as cinema_nom 
        FROM salle s 
        JOIN cinema c ON s.id_cinema = c.id 
        WHERE s.id_cinema = %s
        ORDER BY s.reference
    """, (cinema_id,))
    
    salles = []
    for row in cursor.fetchall():
        salles.append(f"{row['id']} - {row['reference']} ({row['cinema_nom']})")
    
    combo_salle['values'] = salles
    
    cursor.close()
    conn.close()

# Charger les places d'une salle
def charger_places(event=None):
    salle_id = combo_salle.get().split(" - ")[0] if combo_salle.get() else None
    
    if not salle_id:
        return
    
    conn = get_db_connection()
    if conn is None:
        return
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT id, reference, est_pmr 
        FROM place 
        WHERE id_salle = %s 
        ORDER BY reference
    """, (salle_id,))
    
    places = ["Aucune (problème général)"]
    for row in cursor.fetchall():
        pmr_info = " (PMR)" if row['est_pmr'] else ""
        places.append(f"{row['id']} - {row['reference']}{pmr_info}")
    
    combo_place['values'] = places
    
    cursor.close()
    conn.close()

# Enregistrer un nouvel incident
def enregistrer_incident():
    # Récupération des valeurs
    salle_text = combo_salle.get()
    equipement = combo_equipement.get()
    place_text = combo_place.get()
    description = text_description.get("1.0", tk.END).strip()
    
    # Validation
    if not salle_text or not equipement or not description:
        messagebox.showwarning("Champs manquants", "Veuillez sélectionner une salle, un équipement et fournir une description.")
        return
    
    # Extraction des IDs
    salle_id = salle_text.split(" - ")[0]
    place_id = place_text.split(" - ")[0] if place_text != "Aucune (problème général)" else None
    
    # Connexion et insertion
    conn = get_db_connection()
    if conn is None:
        return
    
    try:
        cursor = conn.cursor()
        
        # 🔍 Trouver un employé valide (role = 'employe' ou 'admin')
        cursor.execute("SELECT id FROM utilisateur WHERE role IN ('employe', 'admin') LIMIT 1")
        result = cursor.fetchone()
        
        if not result:
            messagebox.showerror("Erreur", "Aucun employé trouvé dans la base de données. Veuillez contacter l'administrateur.")
            return
            
        employe_id = result[0]  # Premier élément du tuple
        print(f"Utilisation de l'employé ID: {employe_id}")
        
        # 📝 Insérer l'incident
        cursor.execute("""
            INSERT INTO incident (id_salle, id_employe, id_place, equipement, description, statut, date_incident)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (salle_id, employe_id, place_id, equipement, description, 'signale', datetime.now()))
        
        conn.commit()
        messagebox.showinfo("Succès", "Incident enregistré avec succès.")
        
        # 🔄 Réinitialisation du formulaire
        combo_salle.set('')
        combo_equipement.set('')
        combo_place.set('')
        text_description.delete("1.0", tk.END)
        
    except mysql.connector.Error as err:
        messagebox.showerror("Erreur", f"Erreur lors de l'enregistrement:\n{err}")
        print(f"Erreur détaillée: {err}")
    finally:
        cursor.close()
        conn.close()

# Interface graphique
app = tk.Tk()
app.title("Gestion des Incidents - Cinéphoria")
app.geometry("600x500")
app.configure(padx=20, pady=20)

# Titre
label_titre = tk.Label(app, text="Signalement d'Incident", font=("Arial", 16, "bold"))
label_titre.grid(row=0, column=0, columnspan=2, pady=10)

# Cinéma
label_cinema = tk.Label(app, text="Cinéma:")
label_cinema.grid(row=1, column=0, sticky="w", pady=5)

cinemas, equipements, statuts = charger_donnees()
combo_cinema = ttk.Combobox(app, values=[f"{id} - {nom}" for id, nom in cinemas], state="readonly")
combo_cinema.grid(row=1, column=1, sticky="ew", pady=5, padx=5)
combo_cinema.bind("<<ComboboxSelected>>", charger_salles)

# Salle
label_salle = tk.Label(app, text="Salle:")
label_salle.grid(row=2, column=0, sticky="w", pady=5)

combo_salle = ttk.Combobox(app, state="readonly")
combo_salle.grid(row=2, column=1, sticky="ew", pady=5, padx=5)
combo_salle.bind("<<ComboboxSelected>>", charger_places)

# Équipement
label_equipement = tk.Label(app, text="Équipement:")
label_equipement.grid(row=3, column=0, sticky="w", pady=5)

combo_equipement = ttk.Combobox(app, values=equipements, state="readonly")
combo_equipement.grid(row=3, column=1, sticky="ew", pady=5, padx=5)

# Place
label_place = tk.Label(app, text="Place (si applicable):")
label_place.grid(row=4, column=0, sticky="w", pady=5)

combo_place = ttk.Combobox(app, state="readonly")
combo_place.grid(row=4, column=1, sticky="ew", pady=5, padx=5)

# Description
label_description = tk.Label(app, text="Description du problème:")
label_description.grid(row=5, column=0, sticky="nw", pady=5)

text_description = tk.Text(app, height=8, width=40)
text_description.grid(row=5, column=1, sticky="ew", pady=5, padx=5)

# Bouton d'enregistrement
button_frame = tk.Frame(app)
button_frame.grid(row=6, column=0, columnspan=2, pady=20)

btn_enregistrer = tk.Button(button_frame, text="Enregistrer l'incident", command=enregistrer_incident, bg="#4CAF50", fg="white")
btn_enregistrer.pack(pady=10)

# Configuration des colonnes pour l'expansion
app.columnconfigure(1, weight=1)

app.mainloop()