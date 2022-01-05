import pytest
from ..password_hash import HashedPassword

@pytest.fixture
def crypt_generator():

    return HashedPassword()

@pytest.mark.skip()    
def test_one_crypt_generator(crypt_generator) -> bool:
    string_test = "4334233"
    
    assert crypt_generator.hashing_password(string_test)

@pytest.mark.skip()
def test_two_crypt_generator(crypt_generator) -> bool:
    string_test = 323
    
    assert crypt_generator.hashing_password(string_test)

@pytest.mark.skip()
def test_three_crypt_generator(crypt_generator) -> bool:
    string_test = 442
    
    assert crypt_generator.hashing_password(string_test) is False

@pytest.mark.skip()
def test_one_crypt_generator_shape(crypt_generator) -> bool:
    string_test = "slipknot83"
    hashed_password = "$2b$12$ETKnD3NThFEDIaYSzuosOu.fVApofHmNJevyLj/Dv/1JvHLRVic4q"

    assert crypt_generator.shape_password(string_test, hashed_password)

def test_two_crypt_generator_shape(crypt_generator) -> bool:
    string_test = "slipknot833"
    hashed_password = "$2b$12$ETKnD3NThFEDIaYSzuosOu.fVApofHmNJevyLj/Dv/1JvHLRVic4q"

    assert crypt_generator.shape_password(string_test, hashed_password) is False
