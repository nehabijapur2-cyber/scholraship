from student_grade import calculate_average, assign_grade, scholarship_status

def test_average_marks():
    assert calculate_average([70, 80, 90]) == 80

def test_average_empty():
    assert calculate_average([]) == 0

def test_grade_s():
    assert assign_grade(95) == "Grade S"

def test_grade_a():
    assert assign_grade(85) == "Grade A"

def test_grade_b():
    assert assign_grade(70) == "Grade B"

def test_grade_f():
    assert assign_grade(35) == "Grade F"

def test_scholarship_eligible():
    assert scholarship_status(88) == "Eligible for Scholarship"

def test_scholarship_not_eligible():
    assert scholarship_status(70) == "Not Eligible for Scholarship"