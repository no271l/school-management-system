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
        # Επιστρέφει το αντικείμενο Teacher με βάση το ID[cite: 7]
        for t in self.teachers_list:
            if t.teacher_id == teacher_id:
                return t
        return None

    def update_teacher(self, teacher_id):
        # Ενημερώνει τα στοιχεία του καθηγητή ρωτώντας τον χρήστη[cite: 7]
        target_teacher = self.read_teacher(teacher_id)
        if not target_teacher:
            print("Δεν βρέθηκε καθηγητής με αυτό το ID.")
            return False

        print("\nΒρέθηκε ο καθηγητής:")
        target_teacher.print_teacher()
        print("\nΤι θέλετε να ενημερώσετε;")
        print("1. Όνομα")
        print("2. Επώνυμο")
        
        choice = input("Επιλογή (1-2): ").strip()
        
        if choice == "1":
            new_name = input("Δώστε νέο όνομα: ").strip()
            if new_name:
                target_teacher.first_name = new_name
                self.save_teachers_data()
                print("Ενημερώθηκε επιτυχώς!")
                return True
        elif choice == "2":
            new_last_name = input("Δώστε νέο επώνυμο: ").strip()
            if new_last_name:
                target_teacher.last_name = new_last_name
                self.save_teachers_data()
                print("Ενημερώθηκε επιτυχώς!")
                return True
        else:
            print("Λάθος επιλογή.")
        return False

    def delete_teacher(self):
        # Ζητάει το ID και διαγράφει τον καθηγητή[cite: 7]
        try:
            t_id = int(input("Δώστε το ID του καθηγητή προς διαγραφή: "))
            for i, t in enumerate(self.teachers_list):
                if t.teacher_id == t_id:
                    del self.teachers_list[i]
                    self.save_teachers_data()
                    print(f"Ο καθηγητής με ID {t_id} διαγράφηκε επιτυχώς.")
                    return t_id
            print("Δεν βρέθηκε καθηγητής με αυτό το ID.")
            return False
        except ValueError:
             print("Σφάλμα: Το ID πρέπει να είναι ακέραιος αριθμός.")
             return False