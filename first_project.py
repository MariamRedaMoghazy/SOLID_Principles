class Student:
    """Class to represent a student."""
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def __str__(self):
        return f"{self.name}_{self.student_id} (Grade: {self.grade})"

class StudentAdder:
    """Class to add students to the database."""
    def __init__(self, database):
        self.database = database

    def add_student(self, student):
        """Add a student to the database."""
        self.database.append(student)
        print(f"Student '{student.name}' added successfully!")

class StudentRemover:
    """Class to remove students from the database."""
    def __init__(self, database):
        self.database = database

    def remove_student(self, student_id):
        """Remove a student from the database by ID."""
        for student in self.database:
            if student.student_id == student_id:
                self.database.remove(student)
                print(f"Student with ID '{student_id}' removed successfully!")
                return
        print(f"Student with ID '{student_id}' not found!")

class StudentLister:
    """Class to list all students in the database."""
    def __init__(self, database):
        self.database = database

    def list_students(self):
        """List all students in the database."""
        if not self.database:
            print("No students in the database.")
        else:
            print("Students in the database:")
            for student in self.database:
                print(f"- {student}")


    # Database (list of students)
database = []

    # Create instances for adding, removing, and listing students
student_adder = StudentAdder(database)
student_remover = StudentRemover(database)
student_lister = StudentLister(database)

    # Create some students
student1 = Student("Alice", 101, "A")
student2 = Student("Bob", 102, "B")

    # Add students
student_adder.add_student(student1)
student_adder.add_student(student2)

    # List students
student_lister.list_students()

    # Remove a student by ID
student_remover.remove_student(101)

    # List students again
student_lister.list_students()
