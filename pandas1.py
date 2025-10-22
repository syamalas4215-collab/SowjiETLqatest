import oracledb
print(oracledb.__version__)
conn = oracledb.connect(user="scott", password="tiger", dsn="dbhost:1521/orclpdb1")
with conn.cursor() as cur:
    cur.execute("select 1 from dual")
    print(cur.fetchone())
