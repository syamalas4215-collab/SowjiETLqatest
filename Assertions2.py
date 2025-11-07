import pytest
import pytest_check as check

def test_compare_twoNumbers_soft_assertion():
    check.is_true(2==2,"Not equal 1")
    check.is_true(1 == 1, "not equal 2")
    check.equal(1,1,"numbers not equal 3")
    check.not_equal(1,2,"both numbers are equals")
    check.is_false(1==2,"both are numbers are equal 4")