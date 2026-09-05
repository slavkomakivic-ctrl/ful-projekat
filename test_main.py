from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_prikazi_knjige():
    odgovor = client.get("/knjige")
    assert odgovor.status_code == 200
    assert "knjige" in odgovor.json()

def test_dodaj_autora():
    odgovor = client.post("/dodavanje_autora", json={"ime": "Test Autor"})
    assert odgovor.status_code == 401

def test_dodaj_autora_sa_tokenom():
    login_odgovor = client.post(
        "/login",
        data={"username": "brancica94", "password": "apotekab11"}
    )
    token = login_odgovor.json()["access_token"]
    
    odgovor = client.post(
        "/dodavanje_autora",
        json={"ime": "Test Autor Sa Tokenom"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert odgovor.status_code == 200