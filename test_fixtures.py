import pytest
@pytest.fixture
def sample_data():
    return {"name":"sowji","age":25}
def test_sample_data(sample_data):
    assert sample_data["name"] == "sowji"
    assert sample_data["age"] == 25

