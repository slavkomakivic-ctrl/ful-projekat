from pydantic import BaseModel, Field

class Korisnik(BaseModel):
    korisnicko_ime: str = Field(min_length=1, max_length=30)
    lozinka: str = Field(min_length=1, max_length=50)

class Autori(BaseModel):
    ime: str = Field(min_length=1, max_length=100)

class Knjige(BaseModel):
    naslov: str = Field(min_length=1, max_length=200)
    godina: int = Field(gt=1, le=2026)
    ocjena: int = Field(ge=1, le=10)