from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

class DatabaseConnection:
    def __init__(self, db_type, host, database, user, password, port=None):
        self.db_type = db_type
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.engine = None
        self.session = None
        self.connect()

    def connect(self):
        """Establishes a connection to the database using SQLAlchemy."""
        try:
            if self.db_type == "postgresql" or self.db_type == "pg":
                port = self.port if self.port else 5432
                self.engine = create_engine(f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{port}/{self.database}")
            elif self.db_type == "mysql":
                port = self.port if self.port else 3306
                self.engine = create_engine(f"mysql+mysqlconnector://{self.user}:{self.password}@{self.host}:{port}/{self.database}")
            else:
                raise ValueError("Unsupported database type. Use 'postgresql' or 'mysql'.")

            # Create a session
            session = sessionmaker(bind=self.engine)
            self.session = session()

            print(f"Connection to {self.db_type} database established successfully.")
        except SQLAlchemyError as e:
            print(f"Error connecting to {self.db_type} database: {e}")
            raise

    def execute_query(self, query, params=None):
        """Executes a SQL query (SELECT, INSERT, UPDATE, DELETE)."""
        try:
            with self.engine.connect() as connection:
                connection.execute(text(query), params)
            print("Query executed successfully.")
        except SQLAlchemyError as e:
            print(f"Error executing query: {e}")
            raise

    def fetch_results(self, query, params=None):
        """Executes a SELECT query and returns the fetched results."""
        try:
            with self.engine.connect() as connection:
                result = connection.execute(text(query), params)
                return result.fetchall()
        except SQLAlchemyError as e:
            print(f"Error fetching data: {e}")
            raise

    def close_connection(self):
        """Closes the connection to the database."""
        if self.session:
            self.session.close()
        if self.engine:
            self.engine.dispose()
        print(f"Connection to {self.db_type} database closed.")
    
    def validation_query(self):
        if self.db_type == 'mysql':
            query = "SHOW TABLES;"
        else:
            query = '''SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public';'''
        res = self.fetch_results(query)
        print(res)
