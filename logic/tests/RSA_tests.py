import pytest
from ..RSA_password import RSAPassword

@pytest.fixture
def rsa_generator():

    return RSAPassword()

def test_one_rsa_encrypt_password(rsa_generator) -> bool:
    password = "hello"
    assert isinstance(rsa_generator.encrypt(password), str)

#@pytest.mark.skip()
def test_one_rsa_decrypt_password(rsa_generator) -> bool:
    assert isinstance(rsa_generator.decrypt(), str)
