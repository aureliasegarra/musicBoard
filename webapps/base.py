from fastapi import APIRouter
from webapps.musics import route_musics
from webapps.users import route_users
from webapps.auth import route_login

api_router = APIRouter()

api_router.include_router(route_musics.router, prefix="", tags=["homepage"])
api_router.include_router(route_users.router, prefix="", tags=["users"])
api_router.include_router(route_login.router, prefix="", tags=["auth"])
