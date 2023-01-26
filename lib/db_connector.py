import mysql.connector
import json
import pandas as pd

class DbConnector:

    def __init__(self, db_engine = "mysql", db_name = "speakql_university", config_dir = "", verbose = False):
        
        print("Initializing DbConnector class for a", db_engine, " connection to", db_name)

        self.verbose = verbose
        self.db_name = db_name
        self.db_engine = db_engine
        self.config_dir = config_dir
        self.connection = self.get_mysql_database_connector(db_name)

        print("DBCONNECTOR: Connected to", self.connection.get_server_info())



    def get_db_name(self):
        return self.db_name



    def get_db_engine(self):
        return self.db_engine


    def do_single_insert_query_into_dataframe(self, query):

        if self.verbose:
            print("DBCONNECTOR: Executing query '", query, "' in database", self.db_name)

        if self.db_engine == "mysql":
            cursor = self.connection.cursor()
            try:
                cursor.execute(query)
                self.connection.commit()
            except mysql.connector.Error as error:
                print("Failed to INSERT in MySQL: {}".format(error))



    # Only use this internally. Do not integrate with API calls from the frontend.
    def do_single_select_query_into_dataframe(self, query):

        if self.verbose:
            print("DBCONNECTOR: Executing query '", query, "' in database", self.db_name)

        query.replace(";", "")
        
        if self.db_engine == "mysql":
            result_df = pd.DataFrame()
            try:
                cursor = self.connection.cursor()
                cursor.execute(query)
                result_df = pd.DataFrame(
                    columns = cursor.column_names,
                    data = cursor.fetchall()
                    )
            except mysql.connector.ProgrammingError as pe:
                print(pe)
                result_df = pd.DataFrame()
            finally:
                # cursor.close()
                return result_df



    # Simple select / project query generation using provided parameters.
    # Use this instead of do_single_select_query_into_dataframe
    # when exposing to APIs
    def do_select_from_parameters(self, schema = '', columns = [], table = [], where = []):
        select_statement = "SELECT _COLUMNS_ FROM _TABLE_ WHERE _PREDICATES_"

        if len(schema) > 0:
            schema = schema + "."
        
        select_statement = select_statement.replace('_COLUMNS_', ', '.join(columns))

        select_statement = select_statement.replace('_TABLE_', ', '.join([schema + t for t in table]))

        if len(where) == 0:
            select_statement = select_statement.replace("_PREDICATES_", "")
            select_statement = select_statement.replace("WHERE", "")
        else:
            select_statement = select_statement.replace('_PREDICATES_', ' AND '.join(where))

        if self.db_engine == "mysql":
            cursor = self.connection.cursor()
            try:
                cursor.execute(select_statement)
                result_df = pd.DataFrame(
                    columns = cursor.column_names,
                    data = cursor.fetchall()
                )
            except mysql.connector.ProgrammingError as pe:
                print(pe)
                result_df = pd.DataFrame()
            cursor.close()
            return result_df



    def get_mysql_database_connector(self, db_name):

        print("Attempting to connect to", db_name)

        filepath = './lib/'

        if len(self.config_dir) > 0:
            filepath = self.config_dir + filepath.replace("./", "/")

        db_info = json.load(open(filepath + db_name + "_db_info.json"))

        config = {
            'user': db_info["user"],
            'password': db_info["password"],
            'host': db_info["host"],
            'database': db_info["database"],
            'raise_on_warnings': True
        }

        return mysql.connector.connect(**config)

    #Static method (deprecated) keeps insert_data_into_db.py happy until we refactor that.
    def get_speakql_university_connector(self, database = 'default'):
        db_info = json.load(open('./lib/db_info.json'))

        config = {
            'user': db_info["user"],
            'password': db_info["password"],
            'host': db_info["host"],
            'database': db_info["database"],
            'raise_on_warnings': True
        }

        if database != 'default':
            config['database'] = database
        
        cnx = mysql.connector.connect(**config)
        return cnx


