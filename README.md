# Cinephoria Python

Application Python pour la gestion de Cinephoria : films, salles, séances et incidents.  

Ce projet permet notamment de **gérer les incidents** dans les salles et de les enregistrer dans la base de données.

---

## Prérequis

- Python 3.12+  
- MySQL (ou autre base de données configurée)  
- Modules Python requis :

pip install mysql-connector-python
Installation
Cloner le dépôt :

bash
Copier le code
git clone https://github.com/Kharthage/CinephoriaPython.git
cd CinephoriaPython
Installer les dépendances si nécessaire :

bash
Copier le code
pip install -r requirements.txt
Si requirements.txt n’existe pas, installe seulement mysql-connector-python.

Configurer la connexion à la base de données dans les scripts si besoin (hôte, utilisateur, mot de passe, nom de la base).

Utilisation de l’application
Tester la connexion à la base
Avant tout, vérifiez que la connexion à la base fonctionne :

bash
Copier le code
python test_connexion.py
Vous devriez voir :

csharp
Copier le code
✅ Connexion à la base de données réussie!
Nombre de cinémas dans la base: X
Gérer les incidents
Pour enregistrer de nouveaux incidents dans la base :

bash
Copier le code
python gestion_incidents.py
Le script utilise l’ID de l’employé actif (modifiable dans le code).

Les incidents sont automatiquement insérés dans la table incidents.

L’historique des incidents est restauré et affiché au lancement du script.

Autres scripts utiles
incidents_app.py : fonctions additionnelles pour gérer les incidents.

test_dbuser.py et test_mysql.py : scripts de test de la base ou des droits utilisateurs.

Notes
Les dossiers dist/ et build/ contiennent les fichiers compilés/exécutables (générés via PyInstaller). Ils ne sont pas nécessaires pour utiliser l’application en Python.

.gitignore est configuré pour ignorer les caches Python, fichiers temporaires et environnements virtuels.
