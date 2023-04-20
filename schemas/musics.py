from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


class MusicBase(BaseModel):
    title: Optional[str] = None
    artist: Optional[str] = None
    album: Optional[str] = None
    cover: Optional[str] = None
    release_date: Optional[date] = datetime.now().date()


class MusicCreate(MusicBase):
    title: str
    artist: str
    album: str
    cover: str


class ShowMusic(MusicBase):
    title: str
    artist: str

    class Config():
        orm_mode = True
