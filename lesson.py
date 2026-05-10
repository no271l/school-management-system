class Lesson:
    def __init__(self, name="", lesson_id=0, pupil_ids=None, teacher_ids=None):
        self.name = name
        self.lesson_id = lesson_id
        self.pupil_ids = pupil_ids if pupil_ids is not None else []
        self.teacher_ids = teacher_ids if teacher_ids is not None else []

    def from_dict(self, data_dict):
        self.lesson_id = data_dict.get("lesson_id", 0)
        self.name = data_dict.get("name", "")
        self.pupil_ids = data_dict.get("pupil_ids", [])
        self.teacher_ids = data_dict.get("teacher_ids", [])
    
    def to_dict(self):
        return {
            "lesson_id": self.lesson_id,
            "name": self.name,
            "pupil_ids": self.pupil_ids,
            "teacher_ids": self.teacher_ids
        }
    
    def __str__(self):
        return f"[ID Μαθήματος: {self.lesson_id}, Όνομα: {self.name}, Μαθητές: {len(self.pupil_ids)}, Καθηγητές: {len(self.teacher_ids)}]"
    
    