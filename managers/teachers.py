# File: managers/teachers.py
from models.teacher import Teacher
from database import teachers_collection

class Teachers:
    def __init__(self):
        # No more lists or JSON files needed!
        pass

    def next_id(self):
        """Finds the highest teacher_id in the database and adds 1."""
        last_teacher = teachers_collection.find_one(sort=[("teacher_id", -1)])
        if last_teacher and "teacher_id" in last_teacher:
            return last_teacher["teacher_id"] + 1
        return 1  # Starting ID if the collection is empty

    def create_teacher(self, first_name: str, last_name: str):
        """Creates a new teacher directly in MongoDB."""
        # 1. Check for duplicates
        exists = teachers_collection.find_one({
            "first_name": first_name,
            "last_name": last_name
        })
        
        if exists:
            return None
            
        # 2. Create the OOP object
        new_teacher = Teacher(first_name, last_name, self.next_id())
        
        # 3. Insert into MongoDB
        teacher_dict = new_teacher.to_dict()
        teachers_collection.insert_one(teacher_dict)
        
        return new_teacher

    def get_all_teachers(self):
        """Retrieves all teachers from the database."""
        return list(teachers_collection.find({}, {"_id": 0}))

    def update_teacher(self, teacher_id: int, first_name: str = None, last_name: str = None):
        """Updates an existing teacher directly in the database."""
        updates = {}
        if first_name is not None: updates["first_name"] = first_name
        if last_name is not None: updates["last_name"] = last_name

        if not updates:
            return None

        result = teachers_collection.update_one(
            {"teacher_id": teacher_id}, 
            {"$set": updates}
        )

        if result.matched_count == 0:
            return None
            
        return teachers_collection.find_one({"teacher_id": teacher_id}, {"_id": 0})

    def delete_teacher(self, teacher_id: int):
        """Deletes a teacher from the database by ID."""
        result = teachers_collection.delete_one({"teacher_id": teacher_id})
        
        if result.deleted_count > 0:
            return teacher_id
        return None