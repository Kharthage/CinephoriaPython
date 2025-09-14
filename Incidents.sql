CREATE TABLE IF NOT EXISTS cinema (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100),
    ligne_adresse1 TEXT,
    ligne_adresse2 TEXT,
    code_postal VARCHAR(10),
    ville VARCHAR(100),
    pays VARCHAR(50),
    numero_gsm VARCHAR(20),
    horaires TEXT
);

CREATE TABLE IF NOT EXISTS salle (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_cinema INT NOT NULL,
    reference VARCHAR(20) NOT NULL,
    nb_places INT,
    nb_places_pmr INT DEFAULT 0,
    FOREIGN KEY (id_cinema) REFERENCES cinema(id)
);

CREATE TABLE IF NOT EXISTS place (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_salle INT NOT NULL,
    reference VARCHAR(10) NOT NULL,
    est_pmr BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_salle) REFERENCES salle(id)
);

CREATE TABLE IF NOT EXISTS incident (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_salle INT NOT NULL,
    id_employe INT NOT NULL,
    id_place INT DEFAULT NULL,
    equipement VARCHAR(100) DEFAULT NULL,
    description TEXT,
    statut ENUM('signale', 'en_cours', 'resolu', 'rejete') DEFAULT 'signale',
    date_incident DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_salle) REFERENCES salle(id),
    FOREIGN KEY (id_place) REFERENCES place(id)
);