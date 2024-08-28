# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-test presentation classes file
# # Description: A file to test application
# ChangeLog: (Who, When, What)
# CDuPuis,08.27.2024,Created Script
# ------------------------------------------------------------------------------------------------- #
import unittest
from io import StringIO
import sys
from presentation_classes import IO
from data_classes import Employee
from datetime import datetime

#test to check that menu display, user input and employee output data run ok

class TestIO(unittest.TestCase):

    def setUp(self):
        self.employee_data = [
            Employee("John", "Doe", datetime.strptime("2023-08-26", "%Y-%m-%d").date(), 4),
            Employee("Jane", "Doe", datetime.strptime("2023-08-26", "%Y-%m-%d").date(), 5)
        ]
        self.menu = '''
        ---- Employee Ratings ------------------------------
        Select from the following menu:
        1. Show current employee rating data.
        2. Enter new employee rating data.
        3. Save data to a file.
        4. Exit the program.
        --------------------------------------------------
        '''

    def test_output_menu(self):
        # Test the menu output without stdin
        IO.output_menu(self.menu)

    def test_input_menu_choice_valid(self):
        captured_input = StringIO('1\n')
        sys.stdin = captured_input  # Redirect stdin
        choice = IO.input_menu_choice()
        sys.stdin = sys.__stdin__  # Reset stdin
        self.assertEqual(choice, '1')

    def test_output_employee_data(self):
        # Test employee data output without capturing stdout
        IO.output_employee_data(self.employee_data)
        # Simple to avoid errors of stdout checks

if __name__ == '__main__':
    unittest.main()