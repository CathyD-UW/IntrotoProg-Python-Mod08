# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-main file
# # Description: A file to handle the script and separate modules
# ChangeLog: (Who, When, What)
# CDuPuis,08.27.2024,Created Script
# ------------------------------------------------------------------------------------------------- #

from data_classes import Employee
from processing_classes import FileProcessor
from presentation_classes import IO
import traceback

# Data -------------------------------------------- #
FILE_NAME: str = "EmployeeRatings.json"
MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''
employees: list = []  # a table of employee data

# Main Body of Script  ---------------------------- #
def main():
    """
    Main program loop.
    """
    while True:
        IO.output_menu(MENU)
        menu_choice = IO.input_menu_choice()

        if menu_choice == '1':
            try:
                IO.output_employee_data(employees)
            except Exception as e:
                IO.output_error_messages("An error occurred while displaying employee data.", e)
                traceback.print_exc()

        elif menu_choice == '2':
            try:
                IO.input_employee_data(employees, Employee)
            except Exception as e:
                IO.output_error_messages("An error occurred while inputting employee data.", e)
                traceback.print_exc()

        elif menu_choice == '3':
            try:
                FileProcessor.write_employee_data_to_file(FILE_NAME, employees)
                print("Data saved successfully.")
            except Exception as e:
                IO.output_error_messages("An error occurred while saving data to file.", e)
                traceback.print_exc()

        elif menu_choice == '4':
            print("Exiting program...")
            break

        else:
            print("Please choose a valid option.")

if __name__ == "__main__":
    try:
        # Load initial data from file
        employees = FileProcessor.read_employee_data_from_file(FILE_NAME, employees, Employee)
    except Exception as e:
        IO.output_error_messages("An error occurred while loading employee data.", e)
        traceback.print_exc()

    # Start the main program loop
    main()
