import pytest
from data.queries import Queries

@pytest.fixture
def generate_queries():
    
    queries = Queries()    
    return queries

@pytest.mark.skip()
def test_one_insert_user(generate_queries):
    name = "Diego"
    surnames = "Duarte Fernández"
    age = "22"
    email = "diegoduarte8343@gmail.com"
    password = "slipknot83"
    user_name = "diecode14"
    query = generate_queries.insert_user(name, surnames, age, email, password, user_name)
    
    assert query

def test_one_verify_user(generate_queries):
    user_name = "diegocode14"
    password = "slipknot83"
    query = generate_queries.verify_user(user_name, password)

    assert query is True