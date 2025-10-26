'''import oracledb

# Basic (Thin mode - no Oracle Client required)
conn = oracledb.connect(
    user="system",
    password="qazwsxEDC!23",
    dsn="localhost:1521/orclpdb.lan"
)

print("✅ Connected to Oracle Database")

# Test a simple query
cursor = conn.cursor()
cursor.execute("SELECT sysdate FROM dual")
for row in cursor:
    print("Current date/time from DB:", row[0])

cursor.close()
conn.close()'''

import oracledb

''''# Initialize thick mode pointing to your Oracle Home bin directory
oracledb.init_oracle_client(lib_dir=r"C:\Users\syama\Downloads\WINDOWS.X64_193000_db_home\bin")

conn = oracledb.connect(
    user="system",
    password="qazwsxEDC!23",
    dsn="localhost:1521/orclpdb.lan"
)

print("✅ Connected successfully!")

with conn.cursor() as cur:
    cur.execute("select * from employee where EMPID = 'E002'")
    print("employee details:", cur.fetchone()[0])

conn.close()'''
with conn.cursor() as cur:
    cur.execute("""
        select sys_context('USERENV','CON_NAME') pdb,
               sys_context('USERENV','SESSION_USER') usr
        from dual
    """)
    print(cur.fetchone())


