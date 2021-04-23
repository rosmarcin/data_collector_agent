import psycopg2
from psycopg2 import Error

WORKING_DIR = ''
CONFIG_FILE_NAME = ''
FILE_NAME = 'output.json'
DEFAULT_SQL = 'select * from rsm_country;'

def records2file(input_list):
    json_str = {
        'id':'',
        'Col1':'',
        'Col2':''
    }

    f = open(FILE_NAME, mode='w')
    for i in input_list:
        json_str['id'] = i[0]
        json_str['Col1'] = i[1]
        json_str['Col2'] = i[2]
        
        f.write(str(json_str) + '\n')
    f.close()

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="admin",
                                  password="Admin123!",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="sales_models")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    query=input("Enter query to execute : ")
    print('Your query is: '+ query)
    cursor.execute(str(query))
    records = cursor.fetchall()
    print('Number of records: ' + str(len(records)))
    print(str(records))
    records2file(records)
    
except (Exception, Error) as error:
    print("Error: ", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")