from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

applicacion = FastAPI()

applicacion.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://127.0.0.1:5500"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

class Persona(BaseModel):
    nombre: str
    edad: int

fakedata = {
    "1":{
         "nombre":"adan",
         "edad":35
    },
    "2":{
         "nombre":"Eduardo",
         "edad": 25
    },
    "3":{
        "nombre":"Maria",
         "edad": 31
    },

}

@applicacion.get("/")
def index():
    return{
        "mensaje":"Hola como estas"
    }
@applicacion.get("/persona/{id}")
def get_nombre_edad_id(id: int):
    return fakedata[id]

@applicacion.get("/persona")
def get_nombre_edad():
    return fakedata

@applicacion.post("/insert/persona")
def insert_persona(persona:Persona):
    last_id=0
    for id in fakedata.keys():
        last_id = id

    fakedata[str(int(last_id)+1)]= persona