import pandas as pd
import pytest
from sqlalchemy import create_engine

@pytest.fixture()
def connect_to_mysql_database():
    mysql_engine = create_engine("mysql+pymysql://root:root@localhost:3306/sowjidb")
    conn_mysql = mysql_engine.connect()
    print("connection to db is established")
    yield conn_mysql
    print("closing the db connection")
    conn_mysql.close()

@pytest.fixture()
def read_source_data_from_source_file():
    print("source data is gettting prepared...")
    df_src = pd.read_csv("emp_src.csv")
    print("source data is prepared...")
    yield df_src
    print("closing the source data file..")

@pytest.fixture()
def read_source_data_from_target_file():
    print("target data is gettting prepared...")
    df_tgt = pd.read_csv("emp_tgt.csv")
    print("target data file is prepared..")
    yield df_tgt
    print("closing the source data file..")

# autouse = True allows every test to access this without explicitly calling in the test case
@pytest.fixture(autouse=True)
def print_message():
    print("This is before test check....")
    yield
    print("This is after test check....")