class Student:
    """Given class"""

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __repr__(self):
        return f"<Student: {self.name} ({self.student_id})>"

    # Added for set comparison in tests
    def __hash__(self):
        return hash(self.student_id)

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False


class Professor:
    """Given class"""

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def __repr__(self):
        return f"<Professor: {self.name} ({self.employee_id})>"


class Department:
    def __init__(self, name):
        self.name = name
        self.professors = []
        self.students = []

    def add_professor(self, professor):
        self.professors.append(professor)

    def add_student(self, student):
        self.students.append(student)


class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def get_students_in_department(self, dept_name):
        # Find the department and return its students
        for dept in self.departments:
            if dept.name == dept_name:
                return dept.students
        # Return an empty list if department is not found
        return []

    def get_all_students(self):
        all_students = []
        # Go through each department and extend the main list
        for dept in self.departments:
            all_students.extend(dept.students)
        return all_students
