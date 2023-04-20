from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.session import get_db
from db.models.musics import Music
from schemas.musics import MusicCreate, ShowMusic
from db.repository.musics import create_new_music

router = APIRouter()


@router.post("/create-music", response_model=ShowMusic)
def create_music(music: MusicCreate, db: Session = Depends(get_db)):
    owner_id = 1
    music = create_new_music(music=music, db=db, owner_id=owner_id)
    return music


