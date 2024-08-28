# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-processing classes file
# Description: A file to handle file data operations
# ChangeLog: (Who, When, What)
# CDuPuis,08.27.2024,Created Script
# ------------------------------------------------------------------------------------------------- #

import json
from datetime import datetime

class FileProcessor:
    """
    A class for processing file data.

    Methods:
    - read_employee_data_from_file(file_name, employee_data, employee_type): Reads data from a file into a list of employee objects.
    - write_employee_data_to_file(file_name, employee_data): Writes a list of employee objects to a file.

    ChangeLog:
    - RRoot, 1.1.2030: Created the class.
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: object):
        """
        Reads data from a file into a list of employee objects.

        :param file_name: The name of the file to read from.
        :param employee_data: The list to store the employee objects.
        :param employee_type: The class type of the employee objects.
        :return: A list of employee objects.
        """
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                for item in data:
                    employee = employee_type(
                        first_name=item.get("first_name"),
                        last_name=item.get("last_name"),
                        review_date=datetime.strptime(item.get("review_date"), "%Y-%m-%d").date(),  # Convert string to datetime.date
                        review_rating=item.get("review_rating")
                    )
                    employee_data.append(employee)
        except FileNotFoundError:
            print(f"Error: The file '{file_name}' was not found.")
            return []
        except json.JSONDecodeError as e:
            print(f"Error: The file '{file_name}' is not in the correct format. Exception: {str(e)}")
            return []
        except KeyError as e:
            print(f"Error: Missing key in the JSON data - {e}")
            return []
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            return []
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """
        Writes a list of employee objects to a file.

        :param file_name: The name of the file to write to.
        :param employee_data: The list of employee objects to write.
        :return: None
        """
        try:
            with open(file_name, 'w') as file:
                json.dump([{
                    "first_name": employee.first_name,
                    "last_name": employee.last_name,
                    "review_date": employee.review_date.strftime("%Y-%m-%d"),  # Convert datetime.date to string
                    "review_rating": employee.review_rating
                } for employee in employee_data], file, indent=4)
        except Exception as e:
            print(f"An error occurred while writing to the file: {str(e)}")
            return

            with open(file_name, 'w') as file:
                json.dump([{
                    "first_name": employee.first_name,
                    "last_name": employee.last_name,
                    "review_date": employee.review_date,  # Treat review_date as a string
                    "review_rating": employee.review_rating
                } for employee in employee_data], file, indent=4)
        except Exception as e:
            print(f"An error occurred while writing to the file: {str(e)}")
            return
