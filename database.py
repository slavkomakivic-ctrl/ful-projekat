from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

konekcija1 = psycopg2.connect(
    dbname="ful_korisnici_db",
    user="postgres",
    password= os.getenv("SIFRA"),
    host="localhost",
    port="5432"
    )
kursor1 = konekcija1.cursor()

kursor1.execute("""
    CREATE TABLE IF NOT EXISTS korisnici (
        id SERIAL PRIMARY KEY,
        korisnicko_ime TEXT UNIQUE,
        lozinka_hash TEXT
    )
""")
konekcija1.commit()

konekcija = psycopg2.connect(
    dbname="ful_projekat_db",
    user="postgres",
    password= os.getenv("SIFRA"),
    host="localhost",
    port="5432"
)
kursor = konekcija.cursor()

kursor.execute("""
    CREATE TABLE IF NOT EXISTS autori(
        id SERIAL PRIMARY KEY,
        ime TEXT
    )
""")

kursor.execute("""
    CREATE TABLE IF NOT EXISTS knjige (
        id SERIAL PRIMARY KEY,
        naslov TEXT,
        godina INTEGER,
        ocjena INTEGER,
        autor_id INTEGER,
        FOREIGN KEY (autor_id) REFERENCES autori(id)        
    )
""")
konekcija.commit()