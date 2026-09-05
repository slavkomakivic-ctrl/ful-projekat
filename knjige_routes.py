from fastapi import APIRouter, HTTPException, Depends
from database import kursor, konekcija
from models import Knjige, Autori
from auth_dependency import trenutni_korisnik

router = APIRouter()

@router.post("/dodavanje_autora")
def dodaj_autora(autor: Autori, korisnik: str = Depends(trenutni_korisnik)):
    kursor.execute("INSERT INTO autori (ime) VALUES (?)", (autor.ime, ))
    konekcija.commit()
    return {"poruka": f"Dodan autor: {autor.ime}"}

@router.post("/dodavanje_knjige")
def dodaj_knjigu(knjiga: Knjige, autor_id: int, korisnik: str = Depends(trenutni_korisnik)):
    kursor.execute("SELECT * FROM autori WHERE id = ?", (autor_id,))
    autor = kursor.fetchone()
    
    if autor is None:
        raise HTTPException(status_code=404, detail="Autor sa tim id-jem ne postoji")
    
    kursor.execute(
        "INSERT INTO knjige (naslov, godina, ocjena, autor_id) VALUES (?, ?, ?, ?)",
        (knjiga.naslov, knjiga.godina, knjiga.ocjena, autor_id)
    )
    konekcija.commit()
    return {"poruka": f"Dodana knjiga {knjiga.naslov} ({knjiga.godina})"}

@router.put("/knjige/{id}")
def azuriraj_knjigu(id: int, knjiga: Knjige, autor_id: int, korisnik: str = Depends(trenutni_korisnik)):
    kursor.execute("SELECT * FROM knjige WHERE id = ?", (id,))
    postoji = kursor.fetchone()

    if postoji is None:
        raise HTTPException(status_code=404, detail="knjiga sa tim brojem id ne postoji")
    
    kursor.execute("SELECT * FROM autori WHERE id = ?", (autor_id,))
    autor = kursor.fetchone()
        
    if autor is None:
        raise HTTPException(status_code=404, detail="Autor sa tim id-jem ne postoji")

    kursor.execute(
        "UPDATE knjige SET naslov = ?, godina = ?, ocjena = ?, autor_id = ? WHERE id = ?",
        (knjiga.naslov, knjiga.godina, knjiga.ocjena, autor_id, id)
    )
    konekcija.commit()
    return {"poruka": f"Azurirana knjiga sa id {id}"}

@router.get("/knjige")
def prikazi_sve():
    kursor.execute("""
        SELECT knjige.naslov, knjige.godina, autori.ime
        FROM knjige
        INNER JOIN autori ON knjige.autor_id=autori.id 
        ORDER BY autori.ime
    """)
    rezultati = kursor.fetchall()
    return {"knjige": rezultati}

@router.get("/autori")
def prikazi_sve_autore():
    kursor.execute("SELECT * FROM autori")
    rezultati = kursor.fetchall()
    return {"autori": rezultati}

@router.delete("/autori/{id}")
def obrisi_autora(id: int, korisnik: str = Depends(trenutni_korisnik)):
    kursor.execute("SELECT * FROM autori WHERE id = ?", (id,))
    postoji = kursor.fetchone()

    if postoji is None:
        raise HTTPException(status_code=404, detail="Autor sa tim id brojem ne postoji")
        
    kursor.execute("DELETE FROM knjige WHERE autor_id = ?", (id,))
    kursor.execute("DELETE FROM autori WHERE id = ?", (id,))
    konekcija.commit()
    return {"poruka": "Autor i sve njegove knjige obrisani"}

@router.delete("/knjige/{id}")
def obrisi_knjigu(id: int, korisnik: str = Depends(trenutni_korisnik)):
    kursor.execute("SELECT * FROM knjige WHERE id = ?", (id,))
    postoji = kursor.fetchone()

    if postoji is None:
        raise HTTPException(status_code=404, detail="Knjiga sa tim brojem id ne postoji")

    kursor.execute(
        "DELETE FROM knjige WHERE id = ?", (id, )
    )
    konekcija.commit()
    return {"poruka": f"Obrisana knjiga sa id {id}"}