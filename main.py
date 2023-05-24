from fastapi import FastAPI, HTTPException
from typing import Union
from pydantic import BaseModel

class Student(BaseModel):
    first_name: str
    last_name: str
    age: int

students = []
app = FastAPI()

@app.post("/student/", status_code=200)
async def post(student: Student):
    students.append(student)
    return student

@app.put("/students/{student_id}", status_code=200)
async def update(student_id: int, student: Student):
    if len(students) <= student_id:
        raise HTTPException(status_code=404, detail="Student not found")
    elif student.first_name == int or student.last_name == int:
        raise HTTPException(status_code=404, detail="Student not found")
    elif student.first_name == 0 or student.last_name == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    students[student_id] = student
    return {"student_id": student_id}

@app.get("/students/{student_id}", status_code=200)
async def get_student(student_id: int):
    return students[student_id]