from fastapi import APIRouter

from apis.version1 import route_users
from apis.version1 import route_musics

api_router = APIRouter()
api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_musics.router, prefix="/music", tags=["music"])
