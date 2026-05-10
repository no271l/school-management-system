import json
from lesson import Lesson

LESSONS_FILE = "lessons.json"

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
    
    def create_lesson(self):
        print("\n--- Δημιουργία Νέου Μαθήματος ---")
        name = input("Όνομα Μαθήματος: ").strip()
        
        for l in self.lessons_list:
            if l.name.lower() == name.lower():
                print("Σφάλμα: Το μάθημα υπάρχει ήδη.")
                return False
                
        new_lesson = Lesson(name=name, lesson_id=self.next_id())
        self.lessons_list.append(new_lesson)
        self.save_lessons_data()
        print(f"Επιτυχία! Το μάθημα δημιουργήθηκε με ID: {new_lesson.lesson_id}")
        return True
    
    def update_lesson(self):
        print("\n--- Ενημέρωση Μαθήματος (Προσθήκη/Αφαίρεση Μελών) ---")
        try:
            l_id = int(input("Δώστε το ID του μαθήματος: "))
            target = self.search_lesson_by_id(l_id)
            
            if not target:
                print("Σφάλμα: Δεν βρέθηκε μάθημα με αυτό το ID.")
                return False

            print(f"\nΕπιλεγμένο Μάθημα: {target.name}")
            print(f"Τρέχοντα IDs Μαθητών: {target.pupil_ids}")
            print(f"Τρέχοντα IDs Καθηγητών: {target.teacher_ids}")
            print("\nΕπιλογές:")
            print("1. Αλλαγή ονόματος μαθήματος")
            print("2. Προσθήκη Μαθητή (μέσω ID)")
            print("3. Αφαίρεση Μαθητή (μέσω ID)")
            print("4. Προσθήκη Καθηγητή (μέσω ID)")
            print("5. Αφαίρεση Καθηγητή (μέσω ID)")
            print("6. Ακύρωση")
            
            choice = input("Επιλογή (1-6): ").strip()

            if choice == "1":
                target.name = input("Νέο Όνομα: ").strip()
                print("Το όνομα ενημερώθηκε.")
            elif choice == "2":
                p_id = int(input("Δώστε το ID του Μαθητή για προσθήκη: "))
                if p_id not in target.pupil_ids:
                    target.pupil_ids.append(p_id)
                    print("Ο μαθητής προστέθηκε στο μάθημα.")
                else:
                    print("Σφάλμα: Ο μαθητής είναι ήδη εγγεγραμμένος σε αυτό το μάθημα.")
            elif choice == "3":
                p_id = int(input("Δώστε το ID του Μαθητή για αφαίρεση: "))
                if p_id in target.pupil_ids:
                    target.pupil_ids.remove(p_id)
                    print("Ο μαθητής αφαιρέθηκε από το μάθημα.")
                else:
                    print("Σφάλμα: Ο μαθητής δεν βρέθηκε στη λίστα του μαθήματος.")
            elif choice == "4":
                t_id = int(input("Δώστε το ID του Καθηγητή για προσθήκη: "))
                if t_id not in target.teacher_ids:
                    target.teacher_ids.append(t_id)
                    print("Ο καθηγητής προστέθηκε στο μάθημα.")
                else:
                    print("Σφάλμα: Ο καθηγητής διδάσκει ήδη το μάθημα.")
            elif choice == "5":
                t_id = int(input("Δώστε το ID του Καθηγητή για αφαίρεση: "))
                if t_id in target.teacher_ids:
                    target.teacher_ids.remove(t_id)
                    print("Ο καθηγητής αφαιρέθηκε από το μάθημα.")
                else:
                    print("Σφάλμα: Ο καθηγητής δεν βρέθηκε στη λίστα του μαθήματος.")
            elif choice == "6":
                return False
            else:
                print("Μη έγκυρη επιλογή.")
                return False

            self.save_lessons_data()
            return True

        except ValueError:
            print("Σφάλμα: Πρέπει να δώσετε ακέραιο αριθμό για το ID.")
            return False

    def delete_lesson(self):
        print("\n--- Διαγραφή Μαθήματος ---")
        try:
            l_id = int(input("Δώστε το ID του μαθήματος προς διαγραφή: "))
            for i, l in enumerate(self.lessons_list):
                if l.lesson_id == l_id:
                    del self.lessons_list[i]
                    self.save_lessons_data()
                    print(f"Επιτυχία! Το μάθημα με ID {l_id} διαγράφηκε.")
                    return True
            print("Σφάλμα: Δεν βρέθηκε μάθημα με αυτό το ID.")
            return False
        except ValueError:
             print("Σφάλμα: Το ID πρέπει να είναι ακέραιος αριθμός.")
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