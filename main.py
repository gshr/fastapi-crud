from fastapi import FastAPI
from sqlmodel import SQLModel
from base.auth import router
from database.db import create_db_and_tables



create_db_and_tables()
app =FastAPI()
app.include_router(router)




