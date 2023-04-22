from fastapi import APIRouter, Request, Depends, responses, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db.repository.musics import list_musics, search_music
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.musics import MusicCreate
from fastapi.security.utils import get_authorization_scheme_param
from typing import Optional

from db.models.users import User
from db.repository.musics import create_new_music
from apis.version1.route_login import get_current_user_from_token
from webapps.musics.forms import MusicCreateForm

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    musics = list_musics(db=db)
    return templates.TemplateResponse("musics/homepage.html", {"request": request, "musics": musics})


@router.get("/post-a-music/")
def create_music(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("musics/create_music.html", {"request": request})


@router.post("/post-a-music/")
async def create_music(request: Request, db: Session = Depends(get_db)):
    form = MusicCreateForm(request)
    await form.load_data()
    if form.is_valid():
        try:
            token = request.cookies.get("access_token")
            scheme, param = get_authorization_scheme_param(token)
            # scheme will hold "Bearer" and param will hold actual token value
            current_user: User = get_current_user_from_token(token=param, db=db)
            music = MusicCreate(**form.__dict__)
            music = create_new_music(music=music, db=db, owner_id=current_user.id)
            return responses.RedirectResponse(
                f"/detail/{music.id}", status_code=status.HTTP_302_FOUND
            )
        except Exception as e:
            print(e)
            form.__dict__.get("errors").append(
                "You might not be logged in, In case problem persists please contact us."
            )
            return templates.TemplateResponse("musics/create_music.html", form.__dict__)
    return templates.TemplateResponse("musics/create_music.html", form.__dict__)


@router.get("/search/")
def search(
    request: Request, db: Session = Depends(get_db), query: Optional[str] = None
):
    jobs = search_music(query, db=db)
    return templates.TemplateResponse(
        "general_pages/homepage.html", {"request": request, "jobs": jobs}
    )


@router.get("/delete-music/")
def show_musics_to_delete(request: Request, db: Session = Depends(get_db)):
    musics = list_musics(db=db)
    print(musics)
    return templates.TemplateResponse("musics/show_musics_to_delete.html", {
        "request": request,
        "musics": musics
    })
