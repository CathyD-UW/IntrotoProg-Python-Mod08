# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-data_classes file
# Description: A file to handle data classes
# ChangeLog: (Who, When, What)
# CDuPuis,08.27.2024,Created Script
# ------------------------------------------------------------------------------------------------- #

from datetime import datetime, date

class Person:
    """
    A class representing person data.

    Properties:
    - first_name (str): The person's first name.
    - last_name (str): The person's last name.

    ChangeLog:
    - RRoot, 1.1.2030: Created the class.
    """

    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":
            self._first_name = value
        else:
            raise ValueError("First name must contain only letters.")

    @property
    def last_name(self):
        return self._last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":
            self._last_name = value
        else:
            raise ValueError("Last name must contain only letters.")

    def __str__(self):
        return f"{self.first_name},{self.last_name}"

class Employee(Person):
    """
    A class representing employee data, inheriting from Person.

    Properties:
    - review_date (datetime.date): The date of the review as a datetime.date object.
    - review_rating (int): The rating from the review.

    ChangeLog:
    - RRoot, 1.1.2030: Created the class.
    """
# Added defaults for review_date:datetime.date to 1900-01-01
# Added default for review_rating: into to 3

    def __init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01", review_rating: int = 3):
        super().__init__(first_name, last_name)
        self.review_date = self._convert_to_date(review_date)
        self.review_rating = review_rating

    def _convert_to_date(self, value):
        if isinstance(value, date):  # If it's already a date object, return it
            return value
        elif isinstance(value, str):  # If it's a string, convert to date
            return datetime.strptime(value, "%Y-%m-%d").date()
        else:
            raise ValueError("Review date must be a datetime.date object or a string in 'YYYY-MM-DD' format.")

    @property
    def review_date(self):
        return self._review_date

    @review_date.setter
    def review_date(self, value):
        self._review_date = self._convert_to_date(value)

    @property
    def review_rating(self):
        return self._review_rating

    @review_rating.setter
    def review_rating(self, value: int):
        if 1 <= value <= 5:
            self._review_rating = value
        else:
            raise ValueError("Review rating must be an integer between 1 and 5.")

    def __str__(self):
        return f"{super().__str__()},{self.review_date},{self.review_rating}"
