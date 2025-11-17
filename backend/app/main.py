from fastapi import FastAPI
from app.routes.notes import router as notes_router

app = FastAPI()

app.include_router(notes_router) # Add all the routes from notes_router into this main app

@app.get("/")
def root():
    return {"Message": "Welcome to Notes App"}