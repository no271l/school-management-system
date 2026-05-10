# Αρχείο: pupil.py

class Pupil:
    # 1. Η __init__ με default τιμές (αντί για name/surname βάλαμε first_name/last_name)
    def __init__(self, first_name="", last_name="", fathers_name="", age=0, pupil_class=0, id_card=None, pupil_id=0):
        self.first_name = first_name
        self.last_name = last_name
        self.fathers_name = fathers_name
        self.age = age
        self.pupil_class = pupil_class
        self.id_card = id_card
        self.pupil_id = pupil_id

    # 2. Η from_dict φορτώνει τα δεδομένα από το λεξικό που προκύπτει από το JSON αρχείο
    def from_dict(self, data_dict):
        self.first_name = data_dict.get("first_name", "")
        self.last_name = data_dict.get("last_name", "")
        self.fathers_name = data_dict.get("fathers_name", "")
        self.age = data_dict.get("age", 0)
        self.pupil_class = data_dict.get("class", 0)  # Το κλειδί "class" διατηρείται στο JSON αν θέλεις
        self.id_card = data_dict.get("id_card", None)
        self.pupil_id = data_dict.get("pupil_id", 0)

    # 3. Η to_dict μετατρέπει τον μαθητή σε λεξικό για αποθήκευση στο JSON[cite: 8]
    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "fathers_name": self.fathers_name,
            "age": self.age,
            "class": self.pupil_class, 
            "id_card": self.id_card,
            "pupil_id": self.pupil_id
        }

    # 4. Η dunder method __str__ αντικαθιστά την παλιά "print_pupil"[cite: 8]
    def __str__(self):
        id_info = self.id_card if self.id_card else "Δεν υπάρχει"
        # Επιστρέφουμε ένα String, ΔΕΝ κάνουμε print εδώ μέσα. Η print() θα καλέσει αυτή τη μέθοδο!
        return (f"\n[ID: {self.pupil_id}] {self.first_name} {self.last_name} του {self.fathers_name}\n"
                f"Ηλικία: {self.age} | Τάξη: {self.pupil_class} | Αρ. Ταυτότητας: {id_info}\n"
                f"----------------------------------------")