import sqlite3

konekcija1 = sqlite3.connect("korisnici.db", check_same_thread=False)
kursor1 = konekcija1.cursor()

kursor1.execute("""
    CREATE TABLE IF NOT EXISTS korisnici (
        id INTEGER PRIMARY KEY,
        korisnicko_ime TEXT UNIQUE,
        lozinka_hash TEXT
    )
""")
konekcija1.commit()

konekcija = sqlite3.connect("baza_knjige_autori.db", check_same_thread=False)
kursor = konekcija.cursor()

kursor.execute("""
    CREATE TABLE IF NOT EXISTS autori(
        id INTEGER PRIMARY KEY,
        ime TEXT
    )
""")

kursor.execute("""
    CREATE TABLE IF NOT EXISTS knjige (
        id INTEGER PRIMARY KEY,
        naslov TEXT,
        godina INTEGER,
        ocjena INTEGER,
        autor_id INTEGER,
        FOREIGN KEY (autor_id) REFERENCES autori(id)        
    )
""")
konekcija.commit()