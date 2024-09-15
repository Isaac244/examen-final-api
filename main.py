from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId


app = FastAPI()


#Conexion a Mongo
client = MongoClient("mongodb://localhost:27017")
db = client["fastapi"]
estudiante_collection = db["estudiante"]

#Model
class Estudiante(BaseModel):
    id: Optional[str]
    nombre: str
    apellido: str
    aprobado: bool
    nota: float
    fecha: datetime = None

class EstudianteCreate(BaseModel):
    nombre: str
    apellido: str
    aprobado: bool
    nota: float

def student_dict(student):
    return Estudiante(
        id=str(student["_id"]),
        nombre=student["nombre"],
        apellido=student["apellido"],
        aprobado=bool(student["aprobado"]),
        nota=student["nota"],
        fecha=student.get("fecha"),
    )

@app.get("/")
async def index():
    return JSONResponse(content={"message": "Welcome to the FINAL EXAM"})


#CRUD DEL METODO DE ESTUDIANTE
@app.get('/estudiantes', response_model=List[Estudiante], tags=['Estudiantes'], status_code=200)
def get_all_students():
    estudiantes = estudiante_collection.find()
    return [student_dict(student) for student in estudiantes]


@app.get('/estudiantes/{student_id}', response_model=Estudiante, tags=['Estudiantes'], status_code=200)
def get_student_id(student_id: str):
    student = estudiante_collection.find_one({"_id": ObjectId(student_id)})
    if student is None:
        raise HTTPException(status_code=404, detail="Nombre no encontrado")
    return student_dict(student)


@app.post('/estudiantes/create', response_model=Estudiante, tags=['Estudiantes'], status_code=201)
def create_student(student: EstudianteCreate):
    if not student.nombre:
        raise HTTPException(status_code=400, detail="El nombre es requerido")
    elif not student.apellido:
        raise HTTPException(status_code=400, detail="El apellido es necesario")
    elif student.aprobado is None:
        raise HTTPException(status_code=400, detail="El resultado es requerido")
    elif isinstance(student.aprobado, bool) is False:
        raise HTTPException(status_code=400, detail="El campo aprobado debe ser un booleano")
    elif student.nota is None:
        raise HTTPException(status_code=400, detail="La nota es requerida")
    
    fecha_time = datetime.now()
    new_student = {"nombre": student.nombre, "apellido": student.apellido, "aprobado": student.aprobado, "nota": student.nota, "fecha": fecha_time}
    resultado = estudiante_collection.insert_one(new_student)

    student_register = estudiante_collection.find_one({"_id": resultado.inserted_id})
    return student_dict(student_register)


@app.put('/estudiantes/edit/{student_id}', response_model=Estudiante, tags=['Estudiantes'], status_code=200)
def edit_one_student(student_id: str, student: EstudianteCreate):
    existing_student = estudiante_collection.find_one({"_id": ObjectId(student_id)})

    if existing_student is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    
    if not student.nombre:
        raise HTTPException(status_code=400, detail="El nombre es requerido")
    elif not student.apellido:
        raise HTTPException(status_code=400, detail="El apellido es necesario")
    elif student.aprobado is None:
        raise HTTPException(status_code=400, detail="El resultado es requerido")
    elif isinstance(student.aprobado, bool) is False:
        raise HTTPException(status_code=400, detail="El campo aprobado debe ser un booleano")
    elif student.nota is None:
        raise HTTPException(status_code=400, detail="La nota es requerida")
    
    update_student = {"nombre": student.nombre, "apellido": student.apellido, "aprobado": student.aprobado, "nota": student.nota}
    estudiante_collection.update_one({"_id":ObjectId(student_id)}, {"$set": update_student})

    update_student = estudiante_collection.find_one({"_id":ObjectId(student_id)})

    return student_dict(update_student)


@app.delete('/estudiantes/delete/{student_id}', response_model=dict, tags=['Estudiantes'], status_code=200)
def delete_one_student(student_id: str):
    student = estudiante_collection.find_one({"_id": ObjectId(student_id)})

    if student is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    
    estudiante_collection.delete_one({"_id":ObjectId(student_id)})
    return {"message": "Estudiante Borrado Exitosamente"}
