"""
Tests for grade_calculator.py
"""
import unittest
from unittest.mock import patch
from io import StringIO
from grade_calculator import calculate_average, get_letter_grade, get_student_result, print_report


class TestCalculateAverage(unittest.TestCase):
    def test_normal_grades(self):
        self.assertAlmostEqual(calculate_average([80, 90, 100]), 90.0)

    def test_single_grade(self):
        self.assertEqual(calculate_average([75]), 75.0)

    def test_empty_grades(self):
        self.assertEqual(calculate_average([]), 0.0)

    def test_decimal_average(self):
        self.assertAlmostEqual(calculate_average([85, 90]), 87.5)


class TestGetLetterGrade(unittest.TestCase):
    def test_a_grade(self):
        self.assertEqual(get_letter_grade(95), 'A')
        self.assertEqual(get_letter_grade(90), 'A')

    def test_b_grade(self):
        self.assertEqual(get_letter_grade(85), 'B')
        self.assertEqual(get_letter_grade(80), 'B')

    def test_c_grade(self):
        self.assertEqual(get_letter_grade(75), 'C')
        self.assertEqual(get_letter_grade(70), 'C')

    def test_d_grade(self):
        self.assertEqual(get_letter_grade(65), 'D')
        self.assertEqual(get_letter_grade(60), 'D')

    def test_f_grade(self):
        self.assertEqual(get_letter_grade(59), 'F')
        self.assertEqual(get_letter_grade(0), 'F')


class TestGetStudentResult(unittest.TestCase):
    def test_student_result_structure(self):
        result = get_student_result('Alice', [92, 88, 95, 91])
        self.assertEqual(result['name'], 'Alice')
        self.assertEqual(result['grades'], [92, 88, 95, 91])
        self.assertEqual(result['average'], 91.5)
        self.assertEqual(result['letter_grade'], 'A')

    def test_student_failing(self):
        result = get_student_result('Bob', [50, 55, 45])
        self.assertEqual(result['letter_grade'], 'F')


class TestPrintReport(unittest.TestCase):
    def test_report_output(self):
        students = [get_student_result('Alice', [90, 100])]
        with patch('sys.stdout', new_callable=StringIO) as mock_out:
            print_report(students)
            output = mock_out.getvalue()
        self.assertIn('Alice', output)
        self.assertIn('95.0', output)
        self.assertIn('A', output)


if __name__ == '__main__':
    unittest.main()
