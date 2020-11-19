import pytest
from main_user_registration.user_registration import UserRegistration
from main_user_registration.user_registration_exception import InvalidInput


@pytest.fixture()
def instance_of_user_registration():
    user_registration = UserRegistration()
    return user_registration

def test_validate_name(instance_of_user_registration):
    result = instance_of_user_registration.validate_name("Anam")
    assert result == "Anam"

def test_validate_name_raises_exception_on_invalid_name(instance_of_user_registration):
    with pytest.raises(InvalidInput):
        instance_of_user_registration.validate_name("A3jhsfd")
