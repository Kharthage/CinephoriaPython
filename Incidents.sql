CREATE TABLE IF NOT EXISTS incidents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cinema VARCHAR(100),
    seance VARCHAR(100),
    description TEXT,
    date_creation DATETIME
);
