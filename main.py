#instalar el framework de fastapi 
#pip install fastapi

#instalacion del servidor de uvicorn
#pip install "uvicorn[standard]"

#instalacion del framework de fastapi 
#pip install fastapi[all]

#Importar el framework de fastapi
from fastapi import FastAPI, HTTPException

#Crear objeto a partir de la clase FastAPI
app = FastAPI()

#Utilizamos la (instancia) función get del framework FastAPI
@app.get("/imprimir")

#Crear la función asíncrona "impirmir"
async def imprimir():
    return "Hola mundo"

#Crear la función para Git
@app.get("/Git")
async def imprimir():
    return {"Git_curso: https://github.com/gtovarc/ModWeb0.git"}
#Activar el server de Uvicorn 
#uvicorn main:app --reload
#En el explorador utilizar la ip

#importar pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel, ValidationError

#Crear una lista de entidades con los siguientes atributos 
#{"id":3, "Nombre": "TOVAR CRUZ, GUADALUPE","Edad":"25"}
class Usuario(BaseModel):
    id: int
    Nombre: str
    Edad: int
    
#Crear una lista de usuarios
usuarios = [
    Usuario(id=1, Nombre="TOVAR CRUZ, GUADALUPE", Edad=25),
    Usuario(id=2, Nombre="TOVAR CRUZ, JUAN PABLO", Edad=22),
    Usuario(id=3, Nombre="TOVAR CRUZ, ELA LIZETH", Edad=12)
]

#definir la ruta para obtener todos los usuarios
@app.get("/usersclass/")
async def get_usuarios():
    return usuarios
#Colocar en el explorador la raíz /usersclass/

#---------------------------Actividad 1: API Solo Get ---------------------------------------------
import pandas as pd

#----------------------------------------------------------------------------------------------------------
#Ruta 1 = carrera/genero/promedio -----> 3 niveles
class Ruta1(BaseModel):
    nombre: str
    carrera: str
    genero: str
    promedio: float
   
#leer el csv 
df = pd.read_csv("BD_E6_v2.csv", sep=",", encoding="utf-8")    
        
#Definir la ruta para obtener los datos de Ruta1
@app.get("/carrera/genero/promedio")
async def get_ruta1(carrera: str = None, genero: str = None, promedio: float = None):
    ruta1_data = []
    for index, row in df.iterrows():
        if (carrera and row['Carrera'] != carrera):
            continue
        if (genero and row['Genero'] != genero):
            continue
        if (promedio and row['Promedio'] != promedio):
            continue
        try:
            usuario = Ruta1(
                nombre=row['Nombre'],
                carrera=row['Carrera'],
                genero=row['Genero'],
                promedio=row['Promedio']
            )
            ruta1_data.append(usuario.model_dump())
        except ValidationError as e:
            print(f"Error en la fila {index}: {e}")
    return ruta1_data

#----------------------------------------------------------------------------------------------------------
#Ruta 2 = matricula/edad/semestre -----> 3 niveles
class Ruta2(BaseModel):
    matricula: int
    edad: int
    semestre: int
#hay que leer el csv nuevamente
#df2 = pd.read_csv("BD_E6_v2.csv", sep=",", encoding="utf-8")    
 #No, puedo usar la misma lectura del csv, ya que es el mismo archivo


   
#Definir la ruta para obtener el set de datos de Ruta2
@app.get("/matricula/edad/semestre")
async def get_ruta2(matricula: int = None, edad: int =None, semestre: int = None):
    ruta2_data = []
    for index, row in df.iterrows():
        if (matricula and row['Matricula'] != matricula):
            continue
        if (edad and row['Edad'] != edad):
            continue
        if (semestre and row['Semestre'] != semestre):
            continue
        try:
            usuario = Ruta2(
                matricula=row['Matricula'],
                edad=row['Edad'],
                semestre=row['Semestre']
            )
            ruta2_data.append(usuario.model_dump())
        except ValidationError as e:
            print(f"Error en la fila {index}: {e}")    
    return ruta2_data   
                
  #----------------------------------------------------------------------------------------------------------
#Ruta 3 = matricula/edad/correo/genero -----> 4 niveles
class Ruta3(BaseModel):
    matricula: int
    edad: int
    correo: str
    genero: str
    
#Definir la ruta para obtener el set de datos de Ruta3
@app.get("/matricula/edad/correo/genero")
async def get_ruta3(matricula: int = None, edad: int = None, correo: str = None, genero: str = None):
    ruta3_data = []
    for index, row in df.iterrows():
        if (matricula and row['Matricula'] != matricula):
            continue
        if (edad and row['Edad'] != edad):
            continue
        if (correo and row['Correo'] != correo):
            continue
        if (genero and row['Genero'] != genero):
            continue
        try:
            usuario = Ruta3(
                matricula=row['Matricula'],
                edad=row['Edad'],
                correo=row['Correo'],
                genero=row['Genero']
            )
            ruta3_data.append(usuario.model_dump())
        except ValidationError as e:
            print(f"Error en la fila {index}: {e}")
    return ruta3_data    
#----------------------------------------------------------------------------------------------------------
#がんばって!         