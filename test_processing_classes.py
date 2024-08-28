# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-test processing classes
# # Description: A test file for the processing classes
# ChangeLog: (Who, When, What)
# CDuPuis,08.27.2024,Created Script
# ------------------------------------------------------------------------------------------------- #

import unittest
from processing_classes import FileProcessor

# test checks that when a non-existent file is attempted to be read, the method returns an empty list instead of raising an exception.

class TestFileProcessor(unittest.TestCase):

    def test_read_file_not_found(self):
        file_name = 'non_existent_file.json'
        employee_data = []
        result = FileProcessor.read_employee_data_from_file(file_name, employee_data, None)
        self.assertEqual(result, [], "The result should be an empty list when the file is not found.")

    def test_read_file_format_error(self):
        # Additional test case for handling a file format error, if needed
        pass

    def test_write_file_success(self):
        # Additional test case for successfully writing to a file, if needed
        pass


if __name__ == '__main__':
    unittest.main()
