import json
from models.lesson import Lesson

LESSONS_FILE = "data/lessons.json"

class Lessons:
    def __init__(self):
        self.lessons_list = []
        self._load_data()

    def _load_data(self):
        try:
            with open(LESSONS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    new_lesson = Lesson()
                    new_lesson.from_dict(item)
                    self.lessons_list.append(new_lesson)
        except (FileNotFoundError, json.JSONDecodeError):
            self.lessons_list = []

    def save_lessons_data(self):
        data_to_save = [lesson.to_dict() for lesson in self.lessons_list]
        with open(LESSONS_FILE, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)

    def __str__(self):
        if not self.lessons_list:
            return "Δεν υπάρχουν εγγεγραμμένα μαθήματα."
        result = "\n--- Λίστα Μαθημάτων ---\n"
        for l in self.lessons_list:
            result += str(l) + "\n"
        return result
    
    def next_id(self):
        if not self.lessons_list:
            return 1
        return max(l.lesson_id for l in self.lessons_list) + 1

    def search_lesson_by_id(self, lesson_id):
        for l in self.lessons_list:
            if l.lesson_id == lesson_id:
                return l
        return None
    
    def create_lesson(self, name: str):
        """Creates a new lesson directly from given name."""
        for l in self.lessons_list:
            if l.name.lower() == name.lower():
                return None  # Return None if it's a duplicate
                
        new_lesson = Lesson(name=name, lesson_id=self.next_id())
        self.lessons_list.append(new_lesson)
        self.save_lessons_data()
        return new_lesson
    
    def update_lesson(self, lesson_id: int, name: str = None):
        target = self.search_lesson_by_id(lesson_id)

        if not target:
            return None
        
        if name is not None:
            target.name = name
        
        self.save_lessons_data()
        return target

    def delete_lesson(self, lesson_id: int):
        """Deletes a lesson by ID."""
        for i, l in enumerate(self.lessons_list):
            if l.lesson_id == lesson_id:
                del self.lessons_list[i]
                self.save_lessons_data()
                return True
        return False
        
    def remove_pupil_from_all(self, p_id):
        for l in self.lessons_list:
            if p_id in l.pupil_ids:
                l.pupil_ids.remove(p_id)
        self.save_lessons_data()

    def remove_teacher_from_all(self, t_id):
        for l in self.lessons_list:
            if t_id in l.teacher_ids:
                l.teacher_ids.remove(t_id)
        self.save_lessons_data()