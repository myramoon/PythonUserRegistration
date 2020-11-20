import re
from main_user_registration.user_registration_exception import InvalidInput


class UserRegistration:
    REGEX_NAME = r'^[A-Z][a-z]{2,}$'
    REGEX_PHONE_NUMBER = r'^([1-9][0-9]){1}[-\s][1-9]{1}[0-9]{9}$'
    REGEX_EMAIL = r'^[A-Za-z0-9]+([-.+_]{1}[0-9A-Za-z]+)*@[A-Za-z0-9]+.[a-zA-Z]{2,4}([.,]{1}[a-z]{2,3}){0,1}$'
    REGEX_PASSWORD = r'^(?=.*[A-Z](?=.*\d))(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    def match_pattern(self, user_input, regex):
        """
        method to match pattern
        :param user_input:
        :param regex:
        :return: match object
        """
        pattern = re.compile(regex)
        return pattern.search(user_input)

    def validate_name(self, name):
        """
        :param name:
        :return: matched group
        """
        match = self.match_pattern(name, self.REGEX_NAME)
        if not match:
            raise InvalidInput('Please enter name with minimum 3 characters and beginning with upper case')
        else:
            return match.group()

    def validate_phone_number(self, phone_number):
        """
        :param phone_number:
        :return: matched group
        """
        match = self.match_pattern(phone_number, self.REGEX_PHONE_NUMBER)
        if not match:
            raise InvalidInput(
                'Please enter number in proper format: [2-digit country code](space/-) [10 digit mobile number]')
        else:
            return match.group()

    def validate_email(self, email):
        """
        :param email:
        :return: bool depending on match status
        """
        match = self.match_pattern(email, self.REGEX_EMAIL)
        if not match:
            return False
        else:
            return True

    def validate_password(self, password):
        """
        :param password:
        :return: bool depending on match status
        """
        match = self.match_pattern(password, self.REGEX_PASSWORD)
        if not match:
            return False
        else:
            return True
