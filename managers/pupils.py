# Αρχείο: pupils.py
import json
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

    def update_pupil(self):
        print("\n--- Ενημέρωση Εγγραφής Μαθητή ---")
        try:
            p_id = int(input("Δώστε το ID του μαθητή προς ενημέρωση: "))
            target = self.search_pupil_by_id(p_id)
            
            if not target:
                print("Σφάλμα: Δεν βρέθηκε μαθητής με αυτό το ID.")
                return False

            print("\nΒρέθηκε ο μαθητής:")
            print(target)
            print("Ποιο πεδίο θέλετε να διορθώσετε;")
            print("1. Όνομα\n2. Επώνυμο\n3. Πατρώνυμο\n4. Ηλικία\n5. Τάξη\n6. Αρ. Ταυτότητας\n7. Ακύρωση")
            
            field_choice = input("Επιλέξτε πεδίο (1-7): ").strip()
            
            if field_choice == "1":
                target.first_name = input("Νέο Όνομα: ").strip()
            elif field_choice == "2":
                target.last_name = input("Νέο Επώνυμο: ").strip()
            elif field_choice == "3":
                target.fathers_name = input("Νέο Πατρώνυμο: ").strip()
            elif field_choice == "4":
                try:
                    target.age = int(input("Νέα Ηλικία: "))
                except ValueError:
                    print("Σφάλμα: Λάθος μορφή ηλικίας.")
                    return False
            elif field_choice == "5":
                try:
                    target.pupil_class = int(input("Νέα Τάξη: "))
                except ValueError:
                    print("Σφάλμα: Λάθος μορφή τάξης.")
                    return False
            elif field_choice == "6":
                new_id = input("Νέος Αρ. Ταυτότητας (Enter για κενό): ").strip()
                target.id_card = new_id if new_id else None
            elif field_choice == "7":
                return False
            else:
                print("Σφάλμα: Μη έγκυρη επιλογή.")
                return False
                
            self.save_pupils_data()
            print("Η ενημέρωση ολοκληρώθηκε επιτυχώς!")
            return True
            
        except ValueError:
            print("Σφάλμα: Το ID πρέπει να είναι αριθμός.")
            return False

    def delete_pupil(self):
        print("\n--- Διαγραφή Μαθητή ---")
        try:
            p_id = int(input("Δώστε το ID του μαθητή προς διαγραφή: "))
            for i, p in enumerate(self.pupils_list):
                if p.pupil_id == p_id:
                    del self.pupils_list[i]
                    self.save_pupils_data()
                    print(f"Επιτυχία! Ο μαθητής με ID {p_id} διαγράφηκε.")
                    return p_id
            print("Σφάλμα: Δεν βρέθηκε μαθητής με αυτό το ID.")
            return False
        except ValueError:
             print("Σφάλμα: Το ID πρέπει να είναι ακέραιος αριθμός.")
             return False

    def print_pupils_names(self):
        if not self.pupils_list:
            print("Δεν υπάρχουν μαθητές.")
            return
        print("\n--- Λίστα Ονομάτων Μαθητών ---")
        for p in self.pupils_list:
            print(f"{p.first_name} {p.fathers_name[0]}. {p.last_name}")