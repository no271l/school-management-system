# File: managers/lessons.py
from models.lesson import Lesson
from database import lessons_collection

class Lessons:
    def __init__(self):
        pass

    def next_id(self):
        """Finds the highest lesson_id in the database and adds 1."""
        last_lesson = lessons_collection.find_one(sort=[("lesson_id", -1)])
        if last_lesson and "lesson_id" in last_lesson:
            return last_lesson["lesson_id"] + 1
        return 1

    def create_lesson(self, name: str):
        """Creates a new lesson directly in MongoDB."""
        exists = lessons_collection.find_one({"name": name})
        
        if exists:
            return None
            
        new_lesson = Lesson(name=name, lesson_id=self.next_id())
        
        lesson_dict = new_lesson.to_dict()
        lessons_collection.insert_one(lesson_dict)
        
        return new_lesson

    def get_all_lessons(self):
        """Retrieves all lessons from the database."""
        return list(lessons_collection.find({}, {"_id": 0}))

    def update_lesson(self, lesson_id: int, name: str = None):
        """Updates an existing lesson."""
        if name is None:
            return None

        result = lessons_collection.update_one(
            {"lesson_id": lesson_id}, 
            {"$set": {"name": name}}
        )

        if result.matched_count == 0:
            return None
            
        return lessons_collection.find_one({"lesson_id": lesson_id}, {"_id": 0})

    def delete_lesson(self, lesson_id: int):
        """Deletes a lesson from the database."""
        result = lessons_collection.delete_one({"lesson_id": lesson_id})
        return result.deleted_count > 0

    # --- Referential Integrity Methods ---
    
    def remove_pupil_from_all(self, p_id: int):
        """Removes a pupil's ID from the pupil_ids list of ALL lessons."""
        # The {} means "match all documents". 
        # $pull removes the specified value from the array.
        lessons_collection.update_many(
            {}, 
            {"$pull": {"pupil_ids": p_id}}
        )

    def remove_teacher_from_all(self, t_id: int):
        """Removes a teacher's ID from the teacher_ids list of ALL lessons."""
        lessons_collection.update_many(
            {}, 
            {"$pull": {"teacher_ids": t_id}}
        )