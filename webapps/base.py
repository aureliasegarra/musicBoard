from fastapi import APIRouter

from webapps.musics import route_musics

api_router = APIRouter()

api_router.include_router(route_musics.router, prefix="", tags=["homepage"])
