import pytest
from data.connection import ConnectionDataBase

@pytest.fixture
def generate_connection():
    connect = ConnectionDataBase("localhost", "diego", "diegoduarteslipknot", "generatordb")
    
    return connect.connection()

def test_one_connection(generate_connection):
    assert generate_connection

@pytest.mark.skip()   
def test_two_connection(generate_connection):
    print(generate_connection)
    assert isinstance(generate_connection, str)

