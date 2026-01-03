import sys

def calculate_average(marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)


def assign_grade(avg):
    if 90 <= avg <= 100:
        return "Grade S"
    elif 80 <= avg <= 89:
        return "Grade A"
    elif 65 <= avg <= 79:
        return "Grade B"
    elif 50 <= avg <= 64:
        return "Grade C"
    elif 40 <= avg <= 49:
        return "Grade D"
    else:
        return "Grade F"


def scholarship_status(avg):
    if avg >= 85:
        return "Eligible for Scholarship"
    else:
        return "Not Eligible for Scholarship"


if __name__ == "__main__":

    script_name = sys.argv[0]

    if len(sys.argv) > 5:
        student_name = sys.argv[1]
        department = sys.argv[2]
        semester = sys.argv[3]
        marks = list(map(int, sys.argv[4:7]))
        print("User provided student details:")
    else:
        student_name = "Shreya"
        department = "Computer Science"
        semester = "5"
        marks = [78, 85, 90]
        print("No input given - using default values:")

    avg_marks = calculate_average(marks)
    grade = assign_grade(avg_marks)
    scholarship = scholarship_status(avg_marks)

    print("\n========== Student Academic Report ==========")
    print("Script Name   :", script_name)
    print("Student Name  :", student_name)
    print("Department    :", department)
    print("Semester      :", semester)
    print("Marks         :", marks)
    print("Average Marks :", avg_marks)
    print("Grade         :", grade)
    print("Scholarship   :", scholarship)