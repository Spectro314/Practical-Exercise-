"""
Grade Calculator - Practical Class Exercise
"""


def calculate_average(grades):
    """Calculate the average of a list of grades."""
    if not grades:
        return 0.0
    return sum(grades) / len(grades)


def get_letter_grade(average):
    """Return the letter grade for a given average score."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


def get_student_result(name, grades):
    """Return a summary result for a student."""
    average = calculate_average(grades)
    letter = get_letter_grade(average)
    return {
        'name': name,
        'grades': grades,
        'average': round(average, 2),
        'letter_grade': letter,
    }


def print_report(students):
    """Print a grade report for a list of student results."""
    print("=" * 40)
    print("        STUDENT GRADE REPORT")
    print("=" * 40)
    for student in students:
        print(f"Name:         {student['name']}")
        print(f"Grades:       {student['grades']}")
        print(f"Average:      {student['average']}")
        print(f"Letter Grade: {student['letter_grade']}")
        print("-" * 40)


if __name__ == '__main__':
    students_data = [
        ('Alice', [92, 88, 95, 91]),
        ('Bob', [73, 65, 80, 70]),
        ('Carol', [55, 60, 58, 62]),
        ('David', [85, 90, 88, 92]),
    ]

    results = [get_student_result(name, grades) for name, grades in students_data]
    print_report(results)
