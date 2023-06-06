import pyodbc

from config import Config

pyodbc.pooling = False
pyodbc.tracelevel = 1


class MyDatabase:

    def __init__(self) -> None:
        self.database = Config.DB_NAME
        self.user = Config.DB_USERNAME
        self.password = Config.DB_USER_PASSWORD
        self.server = Config.DB_SERVER
        self.driver = Config.DB_DRIVER
        self.connection = None
        self.cursor = None

    def get_connection(self):
        try:
            server = self.server
            database = self.database
            username = self.user
            password = self.password
            driver = self.driver

            conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
            self.connection = pyodbc.connect(conn_str, autocommit=True)
            self.cursor = self.connection.cursor()

        except pyodbc.Error as e:
            self.connection = None
            self.cursor = None
            print(f"An error occurred while connecting to the database: {e}")

        else:
            print("Connection created successfully.")
            return self.cursor

    def close_connection(self):
        try:
            self.connection.close()
        except pyodbc.Error as e:
            print(
                f"An error occurred while closing the database connection: {e}")
