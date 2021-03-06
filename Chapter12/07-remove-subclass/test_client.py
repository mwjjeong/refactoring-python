import pytest

from client import get_number_of_males
from person import create_person


@pytest.fixture
def data():
    return [
        {"name": "Person1", "gender": "M"},
        {"name": "Person2", "gender": "M"},
        {"name": "Person3", "gender": "F"},
        {"name": "Person4", "gender": "F"},
        {"name": "Person5", "gender": "M"},
        {"name": "Person6", "gender": "X"},
    ]


@pytest.fixture
def people(data):
    return [create_person(record) for record in data]


def test_get_number_of_males(people):
    assert get_number_of_males(people) == 3
