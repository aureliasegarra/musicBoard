from sqlalchemy.orm import Session

from schemas.musics import MusicCreate, ShowMusic
from db.models.musics import Music


def create_new_music(music: MusicCreate, db: Session, owner_id: int):
    music = Music(**music.dict(), owner_id=owner_id)
    db.add(music)
    db.commit()
    db.refresh(music)
    return music
