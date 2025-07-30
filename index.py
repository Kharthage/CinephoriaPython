import tkinter as tk
from tkinter import messagebox

# Fonction pour enregistrer l'incident
def enregistrer_incident():
    # Récupérer les données saisies
    cinema = entry_cinema.get()
    seance = entry_seance.get()
    incident = text_incident.get("1.0", tk.END).strip()

    # Vérifier que tous les champs sont remplis
    if not cinema or not seance or not incident:
        messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs.")
        return

    # Enregistrer l'incident dans un fichier texte
    with open("incidents.txt", "a") as fichier:
        fichier.write(f"Cinéma: {cinema}\n")
        fichier.write(f"Séance: {seance}\n")
        fichier.write(f"Incident: {incident}\n")
        fichier.write("-" * 30 + "\n")

    # Afficher un message de confirmation
    messagebox.showinfo("Succès", "L'incident a été enregistré avec succès.")

    # Effacer les champs après enregistrement
    entry_cinema.delete(0, tk.END)
    entry_seance.delete(0, tk.END)
    text_incident.delete("1.0", tk.END)

# Créer la fenêtre principale
app = tk.Tk()
app.title("Gestion des incidents - Cinépholia")
app.geometry("400x300")

# Ajouter des widgets
label_cinema = tk.Label(app, text="Cinéma :")
label_cinema.pack(pady=5)
entry_cinema = tk.Entry(app, width=40)
entry_cinema.pack(pady=5)

label_seance = tk.Label(app, text="Séance :")
label_seance.pack(pady=5)
entry_seance = tk.Entry(app, width=40)
entry_seance.pack(pady=5)

label_incident = tk.Label(app, text="Description de l'incident :")
label_incident.pack(pady=5)
text_incident = tk.Text(app, width=40, height=10)
text_incident.pack(pady=5)

button_enregistrer = tk.Button(app, text="Enregistrer l'incident", command=enregistrer_incident)
button_enregistrer.pack(pady=10)

# Lancer l'application
app.mainloop()
