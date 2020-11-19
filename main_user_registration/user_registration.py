import re
from main_user_registration.user_registration_exception import InvalidInput


class UserRegistration():

    def validate_name(self , name):
        pattern = re.compile(r'^[A-Z][a-z]{2,}$')
        match = pattern.search(name)
        if not match: raise InvalidInput('Please enter name with minimum 3 characters and beginning with upper case')
        else: return match.group()

    def validate_email(self , email):
        pattern = re.compile(r'^[A-Za-z0-9]+([-.+_]{1}[0-9A-Za-z]+)*@[A-Za-z0-9]+.[a-zA-Z]{2,4}([.,]{1}[a-z]{2,3}){0,1}$')
        match = pattern.search(email)
        if not match: return False
        else: return True