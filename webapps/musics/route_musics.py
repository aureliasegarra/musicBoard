from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db.repository.musics import list_musics
from sqlalchemy.orm import Session
from db.session import get_db


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    musics = list_musics(db=db)
    return templates.TemplateResponse("musics/homepage.html", {"request": request, "musics": musics})
