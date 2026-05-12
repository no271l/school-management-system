# Αρχείο: teachers.py
import json
from models.teacher import Teacher

TEACHERS_FILE = "data/teachers_data.json"

class Teachers:
    def __init__(self):
        # Η λίστα που θα κρατάει αντικείμενα τύπου Teacher[cite: 7]
        self.teachers_list = []
        self._load_data()

    def _load_data(self):
        # Διαβάζει από το JSON και γεμίζει τη λίστα με αντικείμενα Teacher[cite: 7]
        try:
            with open(TEACHERS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    new_teacher = Teacher()
                    new_teacher.from_dict(item)
                    self.teachers_list.append(new_teacher)
        except FileNotFoundError:
            self.teachers_list = []

    def save_teachers_data(self):
        # Μετατρέπει τα αντικείμενα Teacher σε λεξικά και τα σώζει στο JSON[cite: 7]
        data_to_save = [teacher.to_dict() for teacher in self.teachers_list]
        with open(TEACHERS_FILE, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)

    def next_id(self):
        # Βρίσκει το επόμενο διαθέσιμο ID[cite: 7]
        if not self.teachers_list:
            return 1
        return max(t.teacher_id for t in self.teachers_list) + 1

    def create_teacher(self, first_name, last_name):
        # Δημιουργεί νέο καθηγητή αν δεν υπάρχει ήδη[cite: 7]
        for t in self.teachers_list:
            if t.first_name.lower() == first_name.lower() and t.last_name.lower() == last_name.lower():
                return False

        new_teacher = Teacher(first_name=first_name, last_name=last_name, teacher_id=self.next_id())
        self.teachers_list.append(new_teacher)
        self.save_teachers_data()
        return new_teacher

    def read_teacher(self, teacher_id):
        for t in self.teachers_list:
            if t.teacher_id == teacher_id:
                return t
        return None

    def update_teacher(self, teacher_id, first_name=None, last_name=None):
        # Update an existing teacher.
        target = self.read_teacher(teacher_id)
        if not target:
            return None

        if first_name is not None:
            target.first_name = first_name
        if last_name is not None:
            target.last_name = last_name

        self.save_teachers_data()
        return True

    def delete_teacher(self, teacher_id: int):
        """Deletes a teacher by ID and returns the deleted ID if successful."""
        for i, t in enumerate(self.teachers_list):
            if t.teacher_id == teacher_id:
                del self.teachers_list[i]
                self.save_teachers_data()
                return teacher_id
        return None