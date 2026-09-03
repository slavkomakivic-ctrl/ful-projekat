from fastapi import APIRouter, HTTPException, Depends
from database import kursor, konekcija
from models import Knjiga
from auth_dependency import trenutni_korisnik

router = APIRouter()
