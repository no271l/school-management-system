from fastapi import FastAPI, HTTPException
from managers.pupils import Pupils
from managers.teachers import Teachers
from managers.lessons import Lessons

import schemas

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

# --- POST ENDPOINTS ---
@app.post("/pupils")
def create_new_pupil(pupil_data: schemas.PupilCreate):
    new_pupil = pupils_manager.create_pupil(
        first_name = pupil_data.first_name,
        last_name = pupil_data.last_name,
        fathers_name = pupil_data.fathers_name,
        age = pupil_data.age,
        pupil_class = pupil_data.pupil_class,
        id_card = pupil_data.id_card
    )

    if not new_pupil:
        raise HTTPException(status_code=400, detail="A pupil with the same name already exists.")
    
    return {"message": "Pupil created successfully", "pupil": new_pupil.to_dict()}

@app.post("/teachers")
def create_new_teacher(teacher_data: schemas.TeacherCreate):
    new_teacher = teachers_manager.create_teacher(
        first_name=teacher_data.first_name,
        last_name=teacher_data.last_name
    )
    
    if not new_teacher:
        raise HTTPException(status_code=400, detail="Teacher already exists.")
        
    return {"message": "Teacher created successfully!", "teacher": new_teacher.to_dict()}


@app.post("/lessons")
def create_new_lesson(lesson_data: schemas.LessonCreate):
    new_lesson = lessons_manager.create_lesson(name=lesson_data.name)
    
    if not new_lesson:
        raise HTTPException(status_code=400, detail="Lesson already exists.")
        
    return {"message": "Lesson created successfully!", "lesson": new_lesson.to_dict()}