# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-presentation classes file
# Description: A file to handle input/output operations
# ChangeLog: (Who, When, What)
# CDuPuis,08.27.2024,Created Script
# ------------------------------------------------------------------------------------------------- #

from datetime import datetime


class IO:
    """
    A class for handling input/output operations.

    Methods:
    - output_error_messages(message, error): Displays error messages.
    - output_menu(menu): Displays a menu to the user.
    - input_menu_choice(): Gets the user's menu choice.
    - output_employee_data(employee_data): Displays the employee data.
    - validate_date_format (review date): Checks for proper date format.
    - input_employee_data(employee_data, employee_type): Prompts the user for employee data.

    ChangeLog:
    - RRoot, 1.1.2030: Created the class.
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Displays error messages.

        :param message: The error message to display.
        :param error: The exception object (optional).
        :return: None
        """
        print(f"Error: {message}")
        if error:
            print(f"Exception: {str(error)}")
        return

    @staticmethod
    def output_menu(menu: str):
        """
        Displays a menu to the user.

        :param menu: The menu string to display.
        :return: None
        """
        print(menu)
        return

    @staticmethod
    def input_menu_choice():
        """
        Gets the user's menu choice.

        :return: The user's menu choice as a string.
        """
        try:
            choice = input("Please choose an option [1 to 4]: ")
            if not choice.isdigit() or choice not in ['1', '2', '3', '4']:
                raise ValueError("Invalid menu choice. Please enter a number between 1 and 4.")
            return choice
        except ValueError as e:
            IO.output_error_messages("Invalid menu choice. Please enter a valid number.", e)
            return None

    @staticmethod
    def output_employee_data(employee_data: list):
        """
        Displays the employee data.

        :param employee_data: A list of employee object data to display.
        :return: None
        """
        try:
            if not employee_data:
                print("No employee data available.")
                return
            print()
            print("-" * 50)
            for employee in employee_data:
                if employee.review_rating == 5:
                    message = " {} {} (Review Date: {}) is rated as 5 (Leading)"
                elif employee.review_rating == 4:
                    message = " {} {} (Review Date: {}) is rated as 4 (Strong)"
                elif employee.review_rating == 3:
                    message = " {} {} (Review Date: {}) is rated as 3 (Solid)"
                elif employee.review_rating == 2:
                    message = " {} {} (Review Date: {}) is rated as 2 (Building)"
                elif employee.review_rating == 1:
                    message = " {} {} (Review Date: {}) is rated as 1 (Not Meeting Expectations)"
                print(
                    message.format(employee.first_name, employee.last_name, employee.review_date.strftime("%Y-%m-%d")))
            print("-" * 50)
            print()
        except Exception as e:
            IO.output_error_messages("An error occurred while displaying employee data.", e)
            return

    @staticmethod
    def validate_date_format(date_str: str):
        """
        Validates if the input string is in the YYYY-MM-DD format.

        :param date_str: The date string to validate.
        :return: True if valid, False otherwise.
        """
        if len(date_str) != 10:
            return False
        if date_str[4] != '-' or date_str[7] != '-':
            return False
        year, month, day = date_str.split('-')
        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            return False
        if not (1 <= int(month) <= 12):
            return False
        if not (1 <= int(day) <= 31):  # Simplified day range; does not account for month-specific days
            return False
        return True

    @staticmethod
    def input_employee_data(employee_data: list, employee_type: object):
        """
        Prompts the user for employee data and adds it to the list.

        :param employee_data: The list to store the employee objects.
        :param employee_type: The class type of the employee objects.
        :return: None
        """
        try:
            # Validate first name
            while True:
                first_name = input("Enter the employee's first name: ")
                try:
                    employee = employee_type(first_name=first_name)
                    break  # Exit loop if name is valid
                except ValueError as e:
                    IO.output_error_messages("Invalid first name. Please enter a valid name containing only letters.",
                                             e)

            # Validate last name
            while True:
                last_name = input("Enter the employee's last name: ")
                try:
                    employee.last_name = last_name
                    break  # Exit loop if name is valid
                except ValueError as e:
                    IO.output_error_messages("Invalid last name. Please enter a valid name containing only letters.", e)

            # Validate review date
            while True:
                review_date = input("Enter the review date (YYYY-MM-DD): ")
                if isinstance(review_date, str) and IO.validate_date_format(review_date):
                    employee.review_date = datetime.strptime(review_date, "%Y-%m-%d").date()
                    break  # Exit loop if date is valid
                else:
                    IO.output_error_messages("Invalid date format. Please enter the date in 'YYYY-MM-DD' format.")

            # Validate review rating
            while True:
                try:
                    review_rating = int(input("Enter the review rating (1-5): "))
                    employee.review_rating = review_rating
                    break  # Exit loop if rating is valid
                except ValueError as e:
                    IO.output_error_messages("Invalid rating. Please enter a number between 1 and 5.", e)

            # Append validated employee data to the list
            employee_data.append(employee)

        except Exception as e:
            IO.output_error_messages("An unexpected error occurred while adding employee data.", e)
            return
