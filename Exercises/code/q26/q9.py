class Student:
    """Given class"""

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __repr__(self):
        return f"<Student: {self.name} ({self.student_id})>"


class Professor:
    """Given class"""

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def __repr__(self):
        return f"<Professor: {self.name} ({self.employee_id})>"


class Department:
    def __init__(self, name):
        pass  # TODO

    def add_professor(self, professor):
        pass  # TODO

    def add_student(self, student):
        pass  # TODO


class University:
    def __init__(self, name):
        pass  # TODO

    def add_department(self, department):
        pass  # TODO

    def get_students_in_department(self, dept_name):
        pass  # TODO

    def get_all_students(selfself):
        pass  # TODO
