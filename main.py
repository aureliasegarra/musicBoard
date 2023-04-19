from fastapi import FastAPI
from core.config import Settings
from db.session import engine
from db.base import Base


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=Settings.PROJECT_TITLE, description=Settings.PROJECT_DESCRIPTION,
                  version=Settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()


@app.get("/")
async def root():
    return {"message": "Bienvenue sur Music Board"}
