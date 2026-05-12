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

class PupilUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    fathers_name: Optional[str] = None
    age: Optional[int] = None
    pupil_class: Optional[int] = None
    id_card: Optional[str] = None

class TeacherUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class LessonUpdate(BaseModel):
    name: Optional[str] = None