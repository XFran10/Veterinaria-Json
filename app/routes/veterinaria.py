from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
import os

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Ruta del archivo JSON
data_file = "app/data/veterinaria.json"

# Función para cargar los datos del archivo JSON
def load_data():
    if not os.path.exists(data_file):
        with open(data_file, "w") as file:
            json.dump([], file)
    with open(data_file, "r") as file:
        return json.load(file)

# Función para guardar los datos en el archivo JSON
def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

# Ruta para leer todos los pacientes
@router.get("/", response_class=HTMLResponse)
async def read_veterinaria(request: Request):
    veterinaria = load_data()
    return templates.TemplateResponse("index.html", {"request": request, "veterinaria": veterinaria})

# Ruta para mostrar el formulario de creación de paciente
@router.get("/crear", response_class=HTMLResponse)
async def crear_paciente_form(request: Request):
    return templates.TemplateResponse("crear_paciente.html", {"request": request})

# Ruta para crear un nuevo paciente
@router.post("/crear")
async def crear_paciente(veterinaria: dict):
    data = load_data()
    # Añadimos el nuevo paciente a los datos
    data.append(veterinaria)  # Usamos el diccionario recibido del formulario
    save_data(data)
    return {"message": "Paciente creado exitosamente"}

# Ruta para buscar un paciente específico por ID
@router.get("/buscar")
async def buscar_paciente(request: Request, codigo: int):
    veterinaria = load_data()
    veterinaria = next((e for e in veterinaria if e["codigo"] == codigo), None)
    if veterinaria:
        return templates.TemplateResponse("buscar_paciente.html",  {"request": request, "veterinaria": veterinaria})
    else:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
