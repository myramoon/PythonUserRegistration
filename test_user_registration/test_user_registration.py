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


def test_validate_phone_number(instance_of_user_registration):
    result = instance_of_user_registration.validate_phone_number("91 8927142222")
    assert result == "91 8927142222"


def test_validate_phone_number_raises_exception_on_invalid_name(instance_of_user_registration):
    with pytest.raises(InvalidInput):
        instance_of_user_registration.validate_phone_number("91 09142222")


@pytest.mark.parametrize("input , expected" , [
                ("abc@yahoo.com", True),
                ("abc-100@yahoo.com", True),
                ("abc.100@yahoo.com", True),
                ("abc111@abc.com", True),
                ("abc-100@abc.net", True),
                ("abc.100@abc.com.au", True),
                ("abc@1.com", True),
                ("abc@gmail.com.com", True),
                ("abc+100@gmail.com", True),
                ("abc", False),
                ("abc@.com.my", False),
                ("abc123@.com", False),
                ("abc123@.com.com", False),
                ("abc123@gmail.a", False),
                (".abc@abc.com", False),
                ("abc()*@gmail.com", False),
                ("abc@%*.com", False),
                ("abc..2002@gmail.com", False),
                ("abc.@gmail.com", False),
                ("abc@abc@gmail.com", False),
                ("abc@gmail.com.1a", False),
                ("abc@gmail.com.aa.au", False)
])
def test_validate_email(input ,expected , instance_of_user_registration):
    result = instance_of_user_registration.validate_email(input)
    assert result == expected


@pytest.mark.parametrize("input , expected" , [
                ("Abgth1x!c", True),
                ("AAHJJcwhq1$", True),
                ("abc", False),
                ("abcdefgh", False),
                ("abcdefgH", False),
                ("abcdefG1", False),
                ("$ajwbD1" , False)
])
def test_validate_password(input , expected , instance_of_user_registration):
    result = instance_of_user_registration.validate_password(input)
    assert result == expected