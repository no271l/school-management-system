# Αρχείο: pupils.py
import json
from models import pupil
from models.pupil import Pupil

PUPILS_FILE = "data/pupils_data.json"

class Pupils:
    def __init__(self):
        self.pupils_list = []
        self._load_data()

    def _load_data(self):
        try:
            with open(PUPILS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    new_pupil = Pupil()
                    new_pupil.from_dict(item)
                    self.pupils_list.append(new_pupil)
        except FileNotFoundError:
            self.pupils_list = []

    def save_pupils_data(self):
        data_to_save = [pupil.to_dict() for pupil in self.pupils_list]
        with open(PUPILS_FILE, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)

    def __str__(self):
        if not self.pupils_list:
            return "Δεν υπάρχουν εγγεγραμμένοι μαθητές."
        result = "--- Αναλυτική Κατάσταση Μαθητών ---\n"
        for p in self.pupils_list:
            result += str(p) 
        return result

    def next_id(self):
        if not self.pupils_list:
            return 1000
        return max(p.pupil_id for p in self.pupils_list) + 1

    def search_pupil_by_id(self, pupil_id):
        for p in self.pupils_list:
            if p.pupil_id == pupil_id:
                return p
        return None

    def create_pupil(self, first_name: str, last_name: str, fathers_name: str, age: int, pupil_class: int, id_card: str = None):
        """Creates a new pupil directly from given parameters, without terminal inputs."""

        for p in self.pupils_list:
            if p.first_name.lower() == first_name.lower() and \
                p.last_name.lower() == last_name.lower() and \
                p.fathers_name.lower() == fathers_name.lower():
                return None
            
            new_pupil = Pupil(first_name, last_name, fathers_name, age, pupil_class, id_card, self.next_id())
            self.pupils_list.append(new_pupil)
            self.save_pupils_data()
            return new_pupil

    def update_pupil(self, pupil_id:int, first_name: str = None, last_name: str = None, fathers_name: str = None, age: int = None, pupil_class: int = None, id_card: str = None):
        target = self.search_pupil_by_id(pupil_id)
        if not target:
            print("Σφάλμα: Δεν βρέθηκε μαθητής με αυτό το ID.")
            return False
        
        if first_name is not None:
            target.first_name = first_name
        if last_name is not None:
            target.last_name = last_name
        if fathers_name is not None:
            target.fathers_name = fathers_name
        if age is not None:
            target.age = age
        if pupil_class is not None:
            target.pupil_class = pupil_class
        if id_card is not None:
            target.id_card = id_card
        
        self.save_pupils_data()
        print(f"Επιτυχία! Ο μαθητής με ID {pupil_id} ενημερώθηκε.")
        return True

    def delete_pupil(self, pupil_id: int):
        """Deletes a pupil by ID and returns the deleted ID if successful."""
        for i, p in enumerate(self.pupils_list):
            if p.pupil_id == pupil_id:
                del self.pupils_list[i]
                self.save_pupils_data()
                return pupil_id
        return None  # Return None if not found

    def print_pupils_names(self):
        if not self.pupils_list:
            print("Δεν υπάρχουν μαθητές.")
            return
        print("\n--- Λίστα Ονομάτων Μαθητών ---")
        for p in self.pupils_list:
            print(f"{p.first_name} {p.fathers_name[0]}. {p.last_name}")