#!/usr/bin/env python3

# load libraries
import mysql.connecto
from mysql.connector import Error

create_database_query = "CREATE DATABASE comm_app"
create_database(connection, create_database_query)

def create_connection(host_name, user_name, user_password, db_name):
	connection = None
	try: 
		connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
            database=db_name
        )
		print("Connection to MySQL DB successful")
	except Error as e:
		print(f"The error '{e}' occured")
	
	return connection 

connection = create_connection("localhost", "root", "")

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

create_EMSData_table = """
CREATE TABLE IF NOT EXISTS EMSData (
    service VARCHAR NOT NULL,
    priority VARCHAR NOT NULL,
    priority_desc VARCHAR NOT NULL,
    call_year INTEGER NOT NULL,
    description_short VARCHAR NOT NULL,
    city_name VARCHAR NOT NULL,
    PRIMARY KEY(geoid)
    ENGINE = InnoDB
)
"""

execute_query(connection, create_EMSData_table)