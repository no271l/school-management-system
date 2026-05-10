class Teacher:
    def __init__(self, first_name = "", last_name="", teacher_id = 0):
        # Αρχικοποιεί τα πεδία του καθηγητή με τις τιμές που παρέχονται ή με προεπιλεγμένες τιμές
        self.first_name = first_name
        self.last_name = last_name
        self.teacher_id = teacher_id

    def from_dict(self, data_dict):
        # Ενημερώνει τα πεδία του αντικειμένου με βάση το λεξικό που παρέχεται
        self.first_name = data_dict.get("first_name", "")
        self.last_name = data_dict.get("last_name", "")
        self.teacher_id = data_dict.get("teacher_id", 0)
    
    def to_dict(self):        # Επιστρέφει ένα λεξικό που αντιπροσωπεύει τα πεδία του καθηγητή
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "teacher_id": self.teacher_id
        }
    
    def print_teacher(self):
        # Εκτυπώνει τα στοιχεία του καθηγητή με ευανάγνωστο τρόπο
        print(f"ID: {self.teacher_id}, Name: {self.first_name} {self.last_name}")