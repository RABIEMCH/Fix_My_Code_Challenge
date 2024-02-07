#!/usr/bin/python3
""" 
User class
"""

class User():
    """A simple user class"""

    def __init__(self):
        """Initialize the user with default values"""
        self._email = None

    @property
    def email(self):
        """Getter method for email"""
        return self._email

    @email.setter
    def email(self, value):
        """Setter method for email"""
        if not isinstance(value, str):
            raise TypeError("Email must be a string")
        self._email = value

if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)

