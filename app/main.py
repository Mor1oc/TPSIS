from fastapi import FastAPI

from app.database.base import Base, engine
from app.routs.client import router as rout_client
from app.routs.logist import router as rout_logist
from app.routs.warehouse import router as rout_warehouse

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(rout_client)
app.include_router(rout_logist)
app.include_router(rout_warehouse)
