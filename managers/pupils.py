# File: managers/pupils.py
from models.pupil import Pupil
from database import pupils_collection

class Pupils:
    def __init__(self):
        # We no longer need to load JSON files or keep lists in memory!
        pass

    def next_id(self):
        """Finds the highest pupil_id in the database and adds 1."""
        # Sort by pupil_id descending (-1) and get the first result
        last_pupil = pupils_collection.find_one(sort=[("pupil_id", -1)])
        if last_pupil and "pupil_id" in last_pupil:
            return last_pupil["pupil_id"] + 1
        return 1000  # Starting ID if the collection is empty

    def create_pupil(self, first_name: str, last_name: str, fathers_name: str, age: int, pupil_class: int, id_card: str = None):
        """Creates a new pupil directly in MongoDB."""
        # 1. Check for duplicates using a database query
        exists = pupils_collection.find_one({
            "first_name": first_name,
            "last_name": last_name,
            "fathers_name": fathers_name
        })
        
        if exists:
            return None  # Duplicate found
            
        # 2. Create the OOP object to utilize its logic
        new_pupil = Pupil(first_name, last_name, fathers_name, age, pupil_class, id_card, self.next_id())
        
        # 3. Convert to dictionary and insert into MongoDB
        pupil_dict = new_pupil.to_dict()
        pupils_collection.insert_one(pupil_dict)
        
        return new_pupil

    def get_all_pupils(self):
        """Retrieves all pupils from the database."""
        # find() returns all documents. 
        # We exclude the MongoDB specific '_id' field because it causes JSON errors in FastAPI
        return list(pupils_collection.find({}, {"_id": 0}))

    def update_pupil(self, pupil_id: int, first_name: str = None, last_name: str = None, 
                     fathers_name: str = None, age: int = None, pupil_class: int = None, id_card: str = None):
        """Updates an existing pupil directly in the database."""
        # Build a dictionary of only the fields that are provided
        updates = {}
        if first_name is not None: updates["first_name"] = first_name
        if last_name is not None: updates["last_name"] = last_name
        if fathers_name is not None: updates["fathers_name"] = fathers_name
        if age is not None: updates["age"] = age
        if pupil_class is not None: updates["class"] = pupil_class
        if id_card is not None: updates["id_card"] = id_card

        if not updates:
            return None

        # Perform the update in MongoDB ($set modifies only the specified fields)
        result = pupils_collection.update_one(
            {"pupil_id": pupil_id}, 
            {"$set": updates}
        )

        if result.matched_count == 0:
            return None
            
        # Return the updated document from the database
        return pupils_collection.find_one({"pupil_id": pupil_id}, {"_id": 0})

    def delete_pupil(self, pupil_id: int):
        """Deletes a pupil from the database by ID."""
        result = pupils_collection.delete_one({"pupil_id": pupil_id})
        
        if result.deleted_count > 0:
            return pupil_id
        return None