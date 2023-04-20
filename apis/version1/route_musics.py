from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.session import get_db
from db.models.musics import Music
from schemas.musics import MusicCreate, ShowMusic
from db.repository.musics import create_new_music, retreive_music, list_musics, update_music_by_id
from typing import List

router = APIRouter()


@router.post("/create-music", response_model=ShowMusic)
def create_music(music: MusicCreate, db: Session = Depends(get_db)):
    owner_id = 1
    music = create_new_music(music=music, db=db, owner_id=owner_id)
    return music


@router.get("/get/{id}", response_model=ShowMusic)
def retreive_music_by_id(id: int, db: Session = Depends(get_db)):
    music = retreive_music(id=id, db=db)
    if not music:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The music with the id {id} is not available")
    return music


@router.get("/all", response_model=List[ShowMusic])
def retreive_all_musics(db: Session = Depends(get_db)):
    musics = list_musics(db=db)
    return musics


@router.put("/update/{id}")
def update_music(id:int, music:MusicCreate, db:Session=Depends(get_db)):
    owner_id = 1
    message = update_music_by_id(id=id, music=music, db=db, owner_id=owner_id)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The music with the id {id} is not available")
    return {"detail": "Music updated successfully"}


