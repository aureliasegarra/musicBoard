from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    print(dir(request))
    return templates.TemplateResponse("musics/homepage.html", {"request": request})