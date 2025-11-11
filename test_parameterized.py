import pytest
@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (4, 5, 9)])
def test_sample_data(a, b, expected):
    assert a+b == expected