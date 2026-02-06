import random
import os
from dotenv import dotenv_values
import pytest

@pytest.fixture
def random_email():
    return f"test{random.randint(1, 10000)}@example.com"

@pytest.fixture
def password():
    return "password_123"

@pytest.fixture
def weak_password():
    return "weak"

@pytest.fixture
def env() -> dict:
    return dotenv_values()