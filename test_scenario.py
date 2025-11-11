import pandas as pd
import pytest

@pytest.fixture()
def source_dataSetup():
    df_src = pd.read_csv('emp_src.csv')
    print("This is before test execution - source file reading")
    yield df_src
    print("This is after test execution - source file reading")

@pytest.fixture()
def target_dataSetup():
    df_tgt = pd.read_csv('emp_tgt.csv')
    print("This is before test execution - Target file reading")
    yield df_tgt
    print("This is after test execution - Target file reading")

def test_compare_employees_data_usingPytest_test1(source_dataSetup,target_dataSetup):
    print("Test started ....")
    df_src = source_dataSetup
    df_tgt = target_dataSetup
    assert df_src.equals(df_tgt),"The data in src and tgt does not match"
    print("Test completed ....")