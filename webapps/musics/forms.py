from typing import List
from typing import Optional

from fastapi import Request


class MusicCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.title: Optional[str] = None
        self.artist: Optional[str] = None
        self.album: Optional[str] = None
        self.cover: Optional[str] = None
        self.release_date: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.title = form.get("title")
        self.artist = form.get("artist")
        self.album = form.get("album")
        self.cover = form.get("cover")
        self.release_date = form.get("release_date")

    def is_valid(self):
        if not self.title or not len(self.title) >= 4:
            self.errors.append("A valid title is required")
        if not self.artist or not len(self.artist) >= 4:
            self.errors.append("A valid artist is required")
        if not self.album or not len(self.album) >= 4:
            self.errors.append("A valid album is required")
        if not self.cover or not (self.cover.__contains__("http")):
            self.errors.append("A valid url is required")
        if not self.release_date or not len(self.release_date) >= 4:
            self.errors.append("A valid release date is required")
        if not self.errors:
            return True
        return False
