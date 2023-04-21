from sqlalchemy.orm import Session
from schemas.musics import MusicCreate, ShowMusic
from db.models.musics import Music


""" FUNCTION TO POST NEW MUSIC """
def create_new_music(music: MusicCreate, db: Session, owner_id: int):
    music = Music(**music.dict(), owner_id=owner_id)
    db.add(music)
    db.commit()
    db.refresh(music)
    return music


""" FUNCTION TO GET MUSIC BY ID """
def retreive_music(id: int, db: Session):
    music = db.query(Music).filter(Music.is_active == True).all()
    return music


""" FUNCTION TO GET ALL MUSIC"""
def list_musics(db: Session):
    musics = db.query(Music).all()
    return musics


""" FUNCTION TO UPDATE MUSIC BY ID """
def update_music_by_id(id: int, music: MusicCreate, db: Session, owner_id: int):
    existing_music = db.query(Music).filter(Music.id == id)
    if not existing_music.first():
        return 0
    music.__dict__.update(owner_id=owner_id)
    existing_music.update(music.__dict__)
    db.commit()
    return 1


""" FUNCTION TO DELETE MUSIC BY ID """
def delete_music_by_id(id: int, db: Session, owner_id: int):
    existing_music = db.query(Music).filter(Music.id == id)
    if not existing_music.first():
        return 0
    existing_music.delete(synchronize_session=False)
    db.commit()
    return 1
