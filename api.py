from fastapi import FastAPI
from managers.pupils import Pupils
from managers.teachers import Teachers
from managers.lessons import Lessons

# Create FastAPI app
app = FastAPI(title="School Management API", description="API for managing school data")

# Initialize data managers
pupils_manager = Pupils()
teachers_manager = Teachers()
lessons_manager = Lessons()

@app.get("/")
def home():
    return {"message": "Welcome to the School Management API!"}

# --- GET ENDPOINTS ---
@app.get("/pupils")
def get_all_pupils():
    return [p.to_dict() for p in pupils_manager.pupils_list]

@app.get("/teachers")
def get_all_teachers():
    return [t.to_dict() for t in teachers_manager.teachers_list]

@app.get("/lessons")
def get_all_lessons():
    return [l.to_dict() for l in lessons_manager.lessons_list]

