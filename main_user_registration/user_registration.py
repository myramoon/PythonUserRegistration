import re
from main_user_registration.user_registration_exception import InvalidInput


class UserRegistration():

    def validate_name(self , name):
        pattern = re.compile(r'^[A-Z][a-z]{2,}$')
        match = pattern.search(name)
        if not match: raise InvalidInput('Please enter name with minimum 3 characters and beginning with upper case')
        else: return match.group()

