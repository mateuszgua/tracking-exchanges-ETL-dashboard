import os
import pytest
import pyodbc


from dotenv import load_dotenv


@pytest.fixture(scope='session')
def sql_server_connection():
    load_dotenv('.env')

    server = os.getenv('DB_SERVER')
    database = os.getenv('DB_NAME')
    username = os.getenv('DB_USERNAME')
    password = os.getenv('DB_USER_PASSWORD')

    conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    conn = pyodbc.connect(conn_str, autocommit=True)

    yield conn

    conn.close()


def test_sql_server_connection(sql_server_connection):
    assert sql_server_connection is not None

    cursor = sql_server_connection.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    assert result[0] == 1

    cursor.close()


def test_create_database(sql_server_connection):
    cursor = sql_server_connection.cursor()
    cursor.execute("SET XACT_ABORT ON")
    cursor.execute("BEGIN TRANSACTION")

    cursor.execute("IF @@TRANCOUNT > 0 ROLLBACK")

    sql_create = f"""IF NOT EXISTS(SELECT 1 FROM sys.databases WHERE name='TestDatabase')
            CREATE DATABASE TestDatabase USE TestDatabase"""
    cursor.execute(sql_create)
    sql_server_connection.commit()

    cursor.execute(
        """SELECT COUNT(*) FROM sys.databases WHERE name = 'TestDatabase'""")
    count = cursor.fetchone()[0]

    assert count == 1

    cursor.close()


def test_create_table(sql_server_connection):
    cursor = sql_server_connection.cursor()

    cursor.execute("USE TestDatabase")

    cursor.execute("""IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[TestTable]') AND type in (N'U')) 
                    CREATE TABLE TestTable (Name VARCHAR(50), Age INT)""")

    sql_server_connection.commit()

    cursor.execute(
        """SELECT COUNT(*) FROM sys.tables WHERE name = 'TestTable'""")
    count = cursor.fetchone()[0]

    assert count == 1

    cursor.close()


def test_write_data_to_database(sql_server_connection):
    cursor = sql_server_connection.cursor()

    cursor.execute("USE TestDatabase")

    cursor.execute("DELETE FROM TestTable")

    data = [('John', 25), ('Alice', 30), ('Bob', 35)]

    cursor.executemany("INSERT INTO TestTable (Name, Age) VALUES (?, ?)", data)

    sql_server_connection.commit()

    cursor.execute("SELECT COUNT(*) FROM TestTable")
    count = cursor.fetchone()[0]

    assert count == len(data)

    cursor.close()


def test_read_data_from_database(sql_server_connection):
    cursor = sql_server_connection.cursor()

    cursor.execute("USE TestDatabase")

    cursor.execute(
        """SELECT COUNT(*) FROM sys.tables WHERE name = 'TestTable'""")
    rows = cursor.fetchall()

    assert len(rows) > 0

    for row in rows:
        print(row)

    cursor.close()
