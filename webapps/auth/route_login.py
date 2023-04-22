from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from core.security import create_access_token
from db.models.users import User
from db.session import get_db
from webapps.auth.forms import LoginForm
from apis.version1.route_login import login_for_access_token, get_current_user_from_token

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/login/")
def login(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})


@router.post("/login/")
async def login_post(request: Request, db: Session = Depends(get_db)):
    form = LoginForm(request)
    await form.load_data()
    if await form.is_valid():
        try:
            form.__dict__.update(msg="Login successful")
            response = templates.TemplateResponse("auth/login.html", form.__dict__)
            login_for_access_token(response=response, form_data=form, db=db)
            return response
        except HTTPException:
            form.__dict__.update(msg="")
            form.__dict__.get("errors").append("Invalid username or password")
            return templates.TemplateResponse("auth/login.html", form.__dict__)
    return templates.TemplateResponse("auth/login.html", form.__dict__)


@router.post("/logout/")
async def logout(request: Request, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    current_user.access_token = create_access_token({"sub": current_user.email})
    db.add(current_user)
    db.commit()
    response = templates.TemplateResponse("auth/login.html", {"request": request})
    response.delete_cookie("access_token")
    return response
