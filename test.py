import pandas as pd
import pytest
@pytest.mark.skip
def test_compare_data(read_source_data_from_source_file,read_source_data_from_target_file):
    print("test case 1 started.....")
    #print("expected data :", read_source_data_from_source_file)
    # #print("actual data :", read_source_data_from_target_file)
    assert read_source_data_from_source_file.equals(read_source_data_from_target_file), "data between source and target does not match"
    print("test case 1 completed.....")

def test_product_data_count(connect_to_mysql_database):
    print("Count test started..")
    query = """select * from product"""
    df = pd.read_sql(query,connect_to_mysql_database)
    #print(df)
    print(df.empty)
    assert df.empty == False,"No data in the product table"
    print("Count test completed..")

@pytest.fixture(autouse=True)
def setup_and_teardown():
    print("Runs before each test")
    yield
    print("Runs after each test")