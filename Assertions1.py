import pytest
import pytest_check as check
def test_compare_two_number_hard_assertion():
    print("Test started.....")
    num1 = 10
    num2 = 20
    assert num1 < num2, "num1 is lesser than num2"
    assert num1 == num2, "Two numbers are not equal"
    assert num1 != num2, "Two numbers are not equal"
    print("Test completed...")
