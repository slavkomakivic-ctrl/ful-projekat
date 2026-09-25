# Ful Projekat — FastAPI CRUD API sa autentifikacijom

Backend API napravljen u Pythonu (FastAPI), sa JWT autentifikacijom i PostgreSQL bazom podataka.

🔗 **Live demo:** https://ful-projekat.onrender.com/docs

## Šta radi

- Registracija i prijava korisnika (JWT tokeni)
- CRUD operacije za knjige i autore, sa relacijom preko FOREIGN KEY
- Zaštićene rute (dodavanje/izmena/brisanje zahtevaju prijavu)
- Automatska validacija podataka (Pydantic)
- Testirano sa pytest (javne rute, zaštita, kompletan tok prijave)

## Tehnologije

- **Backend:** Python, FastAPI
- **Baza podataka:** PostgreSQL (produkcija), SQLite (razvoj)
- **Autentifikacija:** JWT (python-jose), bcrypt heš lozinki
- **Testiranje:** pytest
- **Deployment:** Docker, Render

## Pokretanje lokalno

\`\`\`bash
git clone https://github.com/tvoje-korisnicko-ime/ful-projekat.git
cd ful-projekat
pip install -r requirements.txt
uvicorn main:app --reload
\`\`\`

Otvori `http://127.0.0.1:8000/docs` za interaktivnu dokumentaciju.

## Napomena

Ovo je vežbeni/portfolio projekat, napravljen kao deo učenja backend developmenta.