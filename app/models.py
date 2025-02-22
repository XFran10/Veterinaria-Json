from pydantic import BaseModel

class veterinaria(BaseModel):
    codigo: int
    nombremascota: str
    especie: str
    raza: str
    edad: int
    peso: int
    diagnostico: str

    class Config:
        orm_mode = True  # Esta opción permite trabajar con datos de bases de datos o diccionarios
