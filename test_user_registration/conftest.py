import pytest
from main_user_registration.user_registration import UserRegistration


@pytest.fixture()
def instance_of_user_registration():
    user_registration = UserRegistration()
    return user_registration