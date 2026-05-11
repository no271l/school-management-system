from pydantic import BaseModel
from typing import Optional

class PupilCreate(BaseModel):
    first_name: str
    last_name: str
    fathers_name: str
    age: int
    pupil_class: int
    id_card: Optional[str] = None

class TeacherCreate(BaseModel):
    first_name: str
    last_name: str

class LessonCreate(BaseModel):
    name: str