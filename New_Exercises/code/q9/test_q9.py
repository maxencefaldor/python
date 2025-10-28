from q9 import Student, Professor, Department, University


def test_university_structure():
    # Create students
    s1 = Student("Alice", "s101")
    s2 = Student("Bob", "s102")
    s3 = Student("Charlie", "s201")

    # Create professors
    p1 = Professor("Dr. Turing", "pA01")
    p2 = Professor("Dr. Hopper", "pB02")

    # Create departments
    cs_dept = Department("Computer Science")
    cs_dept.add_student(s1)
    cs_dept.add_student(s2)
    cs_dept.add_professor(p1)

    math_dept = Department("Mathematics")
    math_dept.add_student(s3)
    math_dept.add_professor(p1)  # Prof. Turing has joint appointment
    math_dept.add_professor(p2)

    # Create university
    uni = University("Imperial College")
    uni.add_department(cs_dept)
    uni.add_department(math_dept)

    # Test get_students_in_department
    cs_students = uni.get_students_in_department("Computer Science")
    print(f"CS Students: {cs_students}")
    assert set(cs_students) == {s1, s2}

    math_students = uni.get_students_in_department("Mathematics")
    print(f"Math Students: {math_students}")
    assert set(math_students) == {s3}

    physics_students = uni.get_students_in_department("Physics")
    print(f"Physics Students: {physics_students}")
    assert physics_students == []  # Test non-existent department

    # Test get_all_students
    all_students = uni.get_all_students()
    print(f"All Students: {all_students}")
    assert set(all_students) == {s1, s2, s3}


if __name__ == "__main__":
    test_university_structure()
