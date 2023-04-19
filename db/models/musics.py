from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base


class Music(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    album = Column(String, nullable=False)
    release_date = Column(Date, nullable=False)
    is_favorite = Column(Boolean(), default=False)
    is_active = Column(Boolean(), default=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="musics")
