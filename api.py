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

# --- PUT ENDPOINTS ---

@app.put("/pupils/{pupil_id}")
def update_existing_pupil(pupil_id: int, pupil_data: schemas.PupilUpdate):
    update_pupil = pupils_manager.update_pupil(
        pupil_id = pupil_id,
        first_name = pupil_data.first_name,
        last_name = pupil_data.last_name,
        fathers_name = pupil_data.fathers_name,
        age = pupil_data.age,
        pupil_class = pupil_data.pupil_class,
        id_card = pupil_data.id_card
    )

    if not update_pupil:
        raise HTTPException(status_code=404, detail="Pupil not found.")
    
    return {"message": "Pupil updated successfully!"}

@app.put("/teachers/{teacher_id}")
def update_existing_teacher(teacher_id: int, teacher_data: schemas.TeacherUpdate):
    update_teacher = teachers_manager.update_teacher(
        teacher_id = teacher_id,
        first_name = teacher_data.first_name,
        last_name = teacher_data.last_name
    )

    if not update_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found.")

    return {"message": "Teacher updated successfully!", "teacher": updated_teacher.to_dict()}

@app.put("/lessons/{lesson_id}")
def update_existing_lesson(lesson_id: int, lesson_data: schemas.LessonUpdate):
    # Pass the data to the manager
    updated_lesson = lessons_manager.update_lesson(
        lesson_id=lesson_id,
        name=lesson_data.name
    )
    
    if not updated_lesson:
        raise HTTPException(status_code=404, detail="Lesson not found.")
        
    return {"message": "Lesson updated successfully!", "lesson": updated_lesson.to_dict()}

# --- DELETE ENDPOINTS ---

@app.delete("/pupils/{pupil_id}")
def delete_existing_pupil(pupil_id: int):
    # 1. Try to delete the pupil
    deleted_id = pupils_manager.delete_pupil(pupil_id)
    
    if not deleted_id:
        raise HTTPException(status_code=404, detail="Pupil not found.")
        
    # 2. Referential Integrity: Remove this pupil's ID from all lessons
    lessons_manager.remove_pupil_from_all(deleted_id)
    
    return {"message": f"Pupil with ID {deleted_id} was successfully deleted from the school and all lessons."}


@app.delete("/teachers/{teacher_id}")
def delete_existing_teacher(teacher_id: int):
    deleted_id = teachers_manager.delete_teacher(teacher_id)
    
    if not deleted_id:
        raise HTTPException(status_code=404, detail="Teacher not found.")
        
    # Referential Integrity: Remove this teacher's ID from all lessons
    lessons_manager.remove_teacher_from_all(deleted_id)
    
    return {"message": f"Teacher with ID {deleted_id} was successfully deleted from the school and all lessons."}


@app.delete("/lessons/{lesson_id}")
def delete_existing_lesson(lesson_id: int):
    success = lessons_manager.delete_lesson(lesson_id)
    
    if not success:
        raise HTTPException(status_code=404, detail="Lesson not found.")
        
    return {"message": f"Lesson with ID {lesson_id} was successfully deleted."}
