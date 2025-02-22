from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes.veterinaria import router as veterinaria_router

app = FastAPI()


app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(veterinaria_router)

@app.get("/")
async def read_root():
    return {"message": "Bienvenido a la Veterinaria"}