import pytest
from ..generate_password import *

@pytest.fixture
def generator_password():
    pass_size = 8
    password_generator = PasswordGenerator()
    
    return password_generator.generate_password(pass_size)

@pytest.mark.skip()
def test_one_pass_generator(generator_password):
    assert generator_password == False

def test_two_pass_generator(generator_password):
    assert generator_password == True
