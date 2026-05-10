# Αρχείο: main.py
from managers.pupils import Pupils
from managers.teachers import Teachers
from managers.lessons import Lessons

def main():
    # Οι τρεις διαχειριστές της βάσης μας
    pupils_manager = Pupils() 
    teachers_manager = Teachers()
    lessons_manager = Lessons()
    
    print("Τα δεδομένα του συστήματος φορτώθηκαν επιτυχώς.")

    while True:
        print("\n" + "=" * 40)
        print("      Σύστημα Διαχείρισης Σχολείου")
        print("=" * 40)
        print("--- ΜΑΘΗΤΕΣ ---")
        print("1. Δημιουργία Εγγραφής Μαθητή")
        print("2. Εκτύπωση όλων των Μαθητών")
        print("3. Ενημέρωση Εγγραφής Μαθητή")
        print("4. Διαγραφή Εγγραφής Μαθητή")
        
        print("\n--- ΚΑΘΗΓΗΤΕΣ ---")
        print("5. Εισαγωγή καθηγητή")
        print("6. Διάβασμα καθηγητή (μέσω ID)")
        print("7. Ενημέρωση καθηγητή")
        print("8. Διαγραφή καθηγητή")

        print("\n--- ΜΑΘΗΜΑΤΑ ---")
        print("9. Δημιουργία Μαθήματος")
        print("10. Προβολή Λίστας Μαθημάτων")
        print("11. Ενημέρωση Μαθήματος (Προσθήκη/Αφαίρεση Μαθητών & Καθηγητών)")
        print("12. Διαγραφή Μαθήματος")
        
        print("\n0. Έξοδος")

        choice = input("\nΕπιλέξτε μια επιλογή (0-12): ").strip()

        if choice == "0":
            print("Έξοδος από το σύστημα. Αντίο!")
            break

        # --- ΜΑΘΗΤΕΣ ---
        elif choice == "1":
            pupils_manager.create_pupil()
        elif choice == "2":
            print(pupils_manager)
        elif choice == "3":
            pupils_manager.update_pupil()
        elif choice == "4":
            deleted_p_id = pupils_manager.delete_pupil()
            if deleted_p_id:
                lessons_manager.remove_pupil_from_all(deleted_p_id)

        # --- ΚΑΘΗΓΗΤΕΣ ---
        elif choice == "5":
            first_name = input("Όνομα: ").strip()
            last_name = input("Επώνυμο: ").strip()
            new_t = teachers_manager.create_teacher(first_name, last_name)
            if new_t:
                print(f"Επιτυχία! Το ID του είναι: {new_t.teacher_id}")
        elif choice == "6":
            try:
                t_id = int(input("ID καθηγητή: "))
                t = teachers_manager.read_teacher(t_id)
                if t: print(t)
                else: print("Δεν βρέθηκε.")
            except ValueError:
                print("Λάθος ID.")
        elif choice == "7":
            try:
                t_id = int(input("ID καθηγητή προς ενημέρωση: "))
                teachers_manager.update_teacher(t_id)
            except ValueError:
                print("Λάθος ID.")
        elif choice == "8":
            deleted_t_id = teachers_manager.delete_teacher()
            if deleted_t_id:
                lessons_manager.remove_teacher_from_all(deleted_t_id)

        # --- ΜΑΘΗΜΑΤΑ ---
        elif choice == "9":
            lessons_manager.create_lesson()
        elif choice == "10":
            print(lessons_manager)
        elif choice == "11":
            lessons_manager.update_lesson()
        elif choice == "12":
            lessons_manager.delete_lesson()

        else:
            print("\nΜη έγκυρη επιλογή. Παρακαλώ πληκτρολόγησε έναν αριθμό από το 0 έως το 12.")

if __name__ == "__main__":
    main()