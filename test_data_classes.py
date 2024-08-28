# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-test data classes file
# # Description: A file to test data classes
# ChangeLog: (Who, When, What)
# CDuPuis,08.27.2024,Created Script
# ------------------------------------------------------------------------------------------------- #

import unittest
from data_classes import Person, Employee
from datetime import datetime


# test that Person object is correctly initialized with valid first and last names
# first_name and last_name properties are set and returned as expected

class TestPerson(unittest.TestCase):

    def test_person_initialization(self):
        person = Person("John", "Doe")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Doe")

#  Tests that a ValueError is raised if the first_name contains invalid characters (e.g., numbers).
#  Person class enforces the rule that names must only contain alphabetic characters.

    def test_person_invalid_first_name(self):
        with self.assertRaises(ValueError):
            Person("John123", "Doe")

#  Tests that a ValueError is raised if the last_name contains invalid characters (e.g., numbers).
#  Person class enforces the rule that names must only contain alphabetic characters.

    def test_person_invalid_last_name(self):
        with self.assertRaises(ValueError):
            Person("John", "Doe123")

# Tests that an Employee object is correctly initialized with valid data: first name, last name, review date, and review rating.
# Confirms that review_date is properly converted to a datetime.date object and that all properties are correctly assigned.

class TestEmployee(unittest.TestCase):
    
    def test_employee_initialization(self):
        employee = Employee("Jane", "Doe", datetime.strptime("2023-08-26", "%Y-%m-%d").date(), 4)
        self.assertEqual(employee.first_name, "Jane")
        self.assertEqual(employee.last_name, "Doe")
        self.assertEqual(employee.review_date, datetime.strptime("2023-08-26", "%Y-%m-%d").date())
        self.assertEqual(employee.review_rating, 4)

# Tests that a ValueError is raised if an invalid review rating is provided (e.g., a rating outside the range of 1-5).

    def test_employee_invalid_rating(self):
        with self.assertRaises(ValueError):
            Employee("Jane", "Doe", datetime.strptime("2023-08-26", "%Y-%m-%d").date(), 6)

if __name__ == '__main__':
    unittest.main()
