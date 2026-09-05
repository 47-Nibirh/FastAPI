from fastapi import FastAPI, HTTPException, Path
import json

app = FastAPI()


def load_data():
    with open("students.json", "r") as f:
        data = json.load(f)
    return data


@app.get("/")
def hello():
    return "Student Management System API"


@app.get("/about")
def about():
    return "A fully functional Student Management System API"


@app.get("/view")
def view_students():
    data = load_data()
    return data


@app.get("/view/{student_id}")
def view_students_by_id(
    student_id: str = Path(
        ...,
        description="Student ID of the student",
        example="S001"
    )
):
    data = load_data()

    if student_id in data:
        return data[student_id]

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )